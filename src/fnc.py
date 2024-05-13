import requests
from src.file_saver import HHSaver
from src.headhunter_api import HeadHunterAPI


def id_area() -> str:
    """
    Функция проверки веденного пользователем страны, региона, города.
    :return: Id страны, в которой пользователь ищет работу
    """
    indicator = 1
    while indicator:
        country = input(f"\nВведите страну в которой ищите работу: ").title().strip()
        response = requests.get('https://api.hh.ru/areas')
        response_json = response.json()
        for value in range(len(response_json) - 1):
            if country in response_json[value]['name'] and len(response_json[value]['areas']) != 0:
                indicator -= 1
                return response_json[value]['id']
        else:
            print("Вакансий для трудоустройства в данной стране нет. Выберите другую страну: ")
            continue


def sort_currency(vacancies) -> list:
    """
    Сортирует вакансии по заданной пользователем валюте.
    По умолчанию валюта: RUR
    :param vacancies: список вакансий
    :return: отсортированный список вакансий
    """
    vacancies_sort = []
    indicator = True
    while indicator:
        currency = input("\nВведите интересующие валюты зарплаты: (По умолчанию RUR), KZT, BYR, UZS, USD, KGS): ").replace(",", " ").upper().strip().split()

        if len(currency) == 0:
            print("Применена валюта по умолчанию.")
            return vacancies
        else:
            for value in currency:
                if value in ("RUR", "KZT", "BYR", "UZS", "USD", "KGS"):
                    indicator = False
                    for vacancy in vacancies:
                        if value == vacancy.currency:
                            vacancies_sort.append(vacancy)
                else:
                    indicator = True
                    vacancies_sort = []
                    print("\nВведена некорректная валюта", end="")
                    break
    return vacancies_sort


def sort_salary(vacancies: list) -> list:
    """
    Сортировка вакансий по указанному пользователем диапазону зарплаты
    :param vacancies: список вакансий
    :return: сортированный список вакансий
    """
    indicator = 1
    while indicator:
        try:
            #  Цифровое значение
            salary = input("\nВведите диапазон зарплаты в формате 'от - до':\n").replace(" ", "").split("-")
            if not len(salary) == 0:
                salary_for = 0
                salary_to = 10000000000
            else:
                salary_for = int(salary[0])
                salary_to = int(salary[1])
        except ValueError:
            print("Данные внесены не корректно.")
        else:
            if salary_for < salary_to:
                sort_vacancies = []
                for vacancy in vacancies:
                    if salary_for <= vacancy.salary_for or salary_for == 0:
                        if salary_to <= vacancy.salary_to or vacancy.salary_to == 0:
                            sort_vacancies.append(vacancy)
                indicator -= 1  # индикатор для остановки цикла
                return sort_vacancies
            else:
                print("\nВведен некорректный диапазон зарплаты.", sep="")


def sort_schedule(vacancies: list) -> list:
    """
    Сортировка по графику работы
    :param vacancies: Список вакансий
    :return: Сортированный список вакансий
    """
    indicator = 1
    while indicator:
        schedule = input("Введите желаемый график работы (Полный, Сменный, Гибкий, Удаленный) По умолчанию все валюты: ").title().strip()
        if not schedule:
            print("Применен параметр по умолчанию.")
            indicator -= 1
            return vacancies
        if schedule in ("Полный", "Сменный", "Гибкий", "Удаленный"):
            sort_vacancies = []
            for vacancy in vacancies:
                vacancy_split = vacancy.schedule.split()
                if vacancy_split[0] == schedule:
                    sort_vacancies.append(vacancy)
            indicator -= 1  # индикатор для остановки цикла
            return sort_vacancies
        else:
            print("Введен некорректный график.\n")


def sort_job_title():
    """
    Загрузка списка по указанной пользователем профессии и вывод пользователю
    """
    job_title = input("\nВведите название профессии которую ищите: ")
    area = id_area()
    hh = HeadHunterAPI()
    hh.get_params = [job_title, area]
    hh_vacancies = hh.load_vacancies()
    vacancies_convert = hh.cast_to_object_list(hh_vacancies)
    file_saver = HHSaver()
    file_saver.vacancy_add(vacancies_convert)
    load_vacancies = file_saver.vacancy_load()
    sorted_currency = sort_currency(load_vacancies)
    sorted_salary = sort_salary(sorted_currency)
    sorted_schedule = sort_schedule(sorted_salary)
    if len(sorted_schedule) != 0:
        print(f"\n\nПо вашему запросу найдено {len(sorted_schedule)} вакансий:")
        sorted_vacancies = sorted(sorted_schedule, reverse=True)
        for number in range(0, len(sorted_vacancies)):
            print(f"\nВакансия № {number + 1}:")
            print(f"{sorted_vacancies[number]}")
    else:
        print("\nПо вашему запросу вакансий не найдено")
        quit()
