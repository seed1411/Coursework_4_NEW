from pathlib import Path
from pytest import fixture
from src.vacancy import Vacancy
from src.headhunter_api import HeadHunterAPI
from src.file_saver import HHSaver
from src.exceptions import VacancyAddException, VacancyDelException


@fixture
def vacancy_1():
    return Vacancy("2024-01-01", "test_1", "test_1", "test_1", "RUR", 0, 0, "Полный", "test_1", "test_1")


@fixture
def vacancy_2():
    return Vacancy("ff", "test_2", "test_2", "test_2", "USD", 0, 1, "Сменный", "test_2", "test_2")


@fixture
def vacancy_3():
    return Vacancy("2024-02-05", "test_3", "test_3", "test_3", "USD", 1, 0, "Гибкий", "test_3", "test_4")


@fixture
def vacancy_4():
    return Vacancy("2024-02-05", "test_4", "test_4", "test_4", "USD", 1, 1, "Удаленный", "test_4", "test_4")


@fixture
def vacancy_5():
    return Vacancy("TEST", "test_4", "test_4", "test_4", "USD", 1, 1, "Удаленный", "test_4", "test_4")

@fixture
def headhunter_api_1():
    return HeadHunterAPI()


@fixture
def headhunter_api_2():
    headhunter = HeadHunterAPI()
    headhunter.get_params = ["python", 113]
    return headhunter


@fixture
def headhunter_api_3():
    headhunter = HeadHunterAPI()
    headhunter.get_params = ["python", 113]
    vacancies_list = headhunter.load_vacancies()
    return vacancies_list


@fixture
def exception_add_1():
    return VacancyAddException()


@fixture
def exception_add_2():
    return VacancyAddException("TEST")


@fixture
def exception_del_1():
    return VacancyDelException()


@fixture
def exception_del_2():
    return VacancyDelException("TEST")


@fixture
def file_saver_1():
    return HHSaver()


@fixture
def file_saver_2():
    hh_saver = HHSaver()
    with open(Path(__file__).parent.parent.joinpath("data").joinpath("vacancies_hh"), "w", encoding="utf-8") as file:
        file.write("")
        return hh_saver
