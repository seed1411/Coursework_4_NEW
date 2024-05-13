import requests
from src.file_saver import HHSaver
from src.headhunter_api import HeadHunterAPI


def id_area() -> str:
    """
    Функция проверки веденного пользователем страны, региона, города.
    :return: id страны, в которой пользователь ищет работу
    """
    indicator = 1
    while indicator:
        country = input(f"Введите страну в которой ищите работу: ").title().strip()
        response = requests.get('https://api.hh.ru/areas')
        response_json = response.json()
        for value in range(len(response_json) - 1):
            if country in response_json[value]['name'] and len(response_json[value]['areas']) != 0:
                indicator -= 1
                return response_json[value]['id']
        else:
            print("Вакансий для трудоустройства в данной стране нет. Повторите ввод.\n")
            continue


def sort_currency(vacancies) -> list:
    """
    Сортирует вакансии по заданной пользователем валюте.
    По умолчанию валюта: RUR
    :param vacancies: список вакансий
    :return: отсортированный список вакансий
    """
    currency = input("Введите валюту зарплаты (RUR, KZT, BYR, UZS). По умолчанию: RUR: ").upper().strip()
    if currency in ("RUR", "KZT", "BYR", "UZS"):
        currency_correct = currency
    else:
        print("Введена некорректная валюта. Применена валюта по умолчанию: RUR")
        currency_correct = "RUR"
    vacancies_sort = [vacancy for vacancy in vacancies if vacancy.currency == currency_correct]
    return vacancies_sort


def sort_salary(vacancies: list) -> list:
    """
    Сортировка вакансий по указанному пользователем диапазону зарплаты
    :param vacancies: список вакансий
    :return: сортированный список вакансий
    """
    sindicator = True
    sort_vacancies = []
    while indicator:
        try:
            #  Цифровое значение
            salary_for, salary_to = input("Введите диапазон желаемой зарплаты в формате 'от - до':\n").split("-")
            salary_for = int(salary_for)
            salary_to = int(salary_to)
        except ValueError:
            print("Данные внесены не корректно. Введите диапазон зарплаты в формате 'от - до'")
        else:
            if salary_for < salary_to:
                indicator = False  # индикатор для остановки цикла
                for vacancy in vacancies:
                    if salary_for > vacancy["salary_for"] or salary_for == 0:
                        if salary_to < vacancy["salary_to"] or vacancy["salary_to"] == 0:
                            sort_vacancies.append(vacancy)
                            return sort_vacancies

            else:
                print("Введен некорректный диапазон зарплаты.")
                continue




def sort_schedule(vacancies: list) -> list:
    """
    Сортировка по графику работы
    :param vacancies: Список вакансий
    :return: Сортированный список вакансий
    """
    sort_vacancies = []
    indicator = True
    while indicator:
        schedule = input("Введите желаемый график работы (Полный, Сменный, Гибкий):\n").title().strip()
        if schedule in ("Полный", "Сменный", "Гибкий"):
            indicator = False  # индикатор для остановки цикла
            for vacancy in vacancies:
                vacancy_split = vacancy.schedule.split()
                if vacancy_split[0] == schedule:
                    sort_vacancies.append(vacancy)
                    return sort_vacancies
        else:
            print("Введен некорректный график.\n")


def sort_job_title() -> list:
    """
    Загрузка списка по указанной пользователем профессии
    :param API: откуда изымать данные
    :return: конвертированный список вакансий
    """
    job_title = input("Введите название профессии которую ищите: ")
    id = id_area()
    hh = HeadHunterAPI()
    hh.get_params = [job_title, id]
    hh_vacancies = hh.load_vacancies()
    vacancies_convert = hh.cast_to_object_list(hh_vacancies)
    file_saver = HHSaver()
    file_saver.vacancy_add(vacancies_convert)
    load_vacancies = file_saver.vacancy_load()
    if len(load_vacancies) != 0:
        sorted_currency = sort_currency(load_vacancies)
        sorted_salary = sort_salary(sorted_currency)
        print(sorted_salary)
        sorted_schedule = sort_schedule(sorted_salary)
        print(sorted_schedule)
        for vacancy in sorted(sorted_schedule):
            print(vacancy)
    else:
        print("По вашему запросу вакансий не найдено")
        quit()
