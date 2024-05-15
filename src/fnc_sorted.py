import requests
from src.file_saver import HHSaver
from src.fnc_color import out_emphasized_text, out_incorrect_input_text
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
                print("Подождите, идет загрузка ...")
                return response_json[value]['id']
        else:  # если введенная страна отсутствует в базе данных
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
    indicator = True  # индикатор цикла
    while indicator:
        currency = input("\nВведите интересующие валюты зарплаты: (По умолчанию RUR), KZT, BYR, UZS, USD, KGS): ").replace(",", " ").upper().strip(" ,.:;!-").split()
        if not len(currency):  # если пользователь не ввел информацию
            print(out_emphasized_text("Применена валюта по умолчанию"))
            return vacancies
        else:  # если пользователь ввел информацию
            for item in currency:
                if item in (",", "-", ".", ":", ";"):
                    currency.remove(item)
            for value in currency:
                if value in ("RUR", "KZT", "BYR", "UZS", "USD", "KGS"):  # если введенная информация соответствует
                    indicator = False  # индикатор для остановки цикла
                    for vacancy in vacancies:
                        if value == vacancy.currency:
                            vacancies_sort.append(vacancy)
                else:  # если введенная информация не соответствует
                    indicator = True  # индикатор цикла
                    vacancies_sort = []
                    print(out_incorrect_input_text("Введена некорректная валюта!\n"))
                    break
    return vacancies_sort


def sort_salary(vacancies: list) -> list:
    """
    Сортировка вакансий по указанному пользователем диапазону зарплаты
    :param vacancies: список вакансий
    :return: сортированный список вакансий
    """
    indicator = 1  # индикатор цикла
    while indicator:
        try:
            #  Цифровое значение
            salary = input("\nВведите минимальную зарплату: ").replace(" ", "").strip(" ,.:;!-")
            if salary == "":  # если пользователь не ввел информацию
                print(out_emphasized_text("Применены параметры по умолчанию"))
                salary_for = 0
            else:  # если пользователь ввел информацию
                salary_for = int(salary)
        except ValueError:  # если введено не число
            print(out_incorrect_input_text("Введите число!"))
        else:
            sort_vacancies = []
            for vacancy in vacancies:
                if salary_for <= vacancy.salary_for:
                    sort_vacancies.append(vacancy)
            indicator -= 1  # индикатор для остановки цикла
            return sort_vacancies


def sort_schedule(vacancies: list) -> list:
    """
    Сортировка по графику работы
    :param vacancies: Список вакансий
    :return: Сортированный список вакансий
    """
    sort_vacancies = []
    indicator = 1  # индикатор цикла
    while indicator:
        schedule = input("\nВведите желаемый график работы (Полный, Сменный, Гибкий, Удаленная) По умолчанию - Все: ").replace(",", " ").title().strip(" ,.:;!-").split()
        if not len(schedule):  # если пользователь не ввел информацию
            print(out_emphasized_text("Применен параметр по умолчанию"))
            indicator -= 1  # индикатор для остановки цикла
            return vacancies
        else:  # если пользователь ввел информацию
            for item in schedule:
                if item in (",", "-", ".", ":", ";"):
                    schedule.remove(item)
            for value in schedule:
                if value in ("Полный", "Сменный", "Гибкий", "Удаленная"):  # если введен корректный график
                    for vacancy in vacancies:
                        vacancy_split = vacancy.schedule.split()
                        if vacancy_split[0] == value:
                            sort_vacancies.append(vacancy)
                    indicator = 0  # индикатор для остановки цикла
                else:  # если введен некорректный график
                    indicator = 1  # индикатор цикла
                    sort_vacancies = []
                    print(out_incorrect_input_text("Введен некорректный график!\n"))
    return sort_vacancies


def sort_top(vacancies):
    """
    Сортировка списка по количеству вакансий который указал пользователь.
    По умолчанию выводит все найденные.
    :param vacancies: Список вакансий
    :return: Список вакансий с количеством который указал пользователь
    """
    while True:
        top_user = input("Сколько показать вакансий? По умолчанию - Все; ").strip(" ,.:;")
        if not top_user:  # если пользователь не ввел число
            print(f"{out_emphasized_text("Применен параметр по умолчанию")}\n\nПоказаны все найденные вакансии.")
            return vacancies
        else:  # если пользователь ввел число в диапазоне найденных вакансий
            try:
                top = int(top_user)
            except ValueError:
                print(out_incorrect_input_text("Введите число!\n"))
            else:
                if top > len(vacancies):  # если пользователь ввел число больше чем найдено вакансий
                    print("Показаны все найденные вакансии.")
                    return vacancies
                else:
                    print(f"\nПоказано ТОП-{top}:")
                    return vacancies[:top]


def print_vacancies():
    """
    Загрузка списка по указанной пользователем профессии и параметрам.
    Вывод пользователю
    """
    job_title = input("\nВведите название профессии которую ищите: ")
    area = id_area()  # индекс страны
    hh = HeadHunterAPI()
    hh.get_params = [job_title, area]  # Применение параметров пользователя для запроса в API
    hh_vacancies = hh.load_vacancies()  # Запрос вакансий
    vacancies_convert = hh.cast_to_object_list(hh_vacancies)  # Перевод запроса в список из объектов вакансий
    file_saver = HHSaver()
    file_saver.vacancy_add(vacancies_convert)  # Добавление вакансий в файл vacancies_hh
    load_vacancies = file_saver.vacancy_load()  # Загрузка данных о вакансиях из файла
    sorted_currency = sort_currency(load_vacancies)  # фильтрация по валюте
    sorted_salary = sort_salary(sorted_currency)  # фильтрация по зарплате
    sorted_schedule = sort_schedule(sorted_salary)  # фильтрация по графику работы
    if len(sorted_schedule) != 0:  # если найдены вакансии
        print(f"\nПо вашему запросу найдено {len(sorted_schedule)} вакансий.")
        sorted_top = sort_top(sorted(sorted_schedule, reverse=True))  # сортировка по убыванию зарплаты
        for number in range(0, len(sorted_top)):
            print(f"\nВакансия № {number + 1}:\n{sorted_top[number]}")
    else:  # если вакансий не найдено
        print("\nПо вашему запросу вакансий не найдено")



