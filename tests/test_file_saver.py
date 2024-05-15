import json
from pathlib import Path
import pytest
from src.exceptions import VacancyAddException, VacancyDelException


def test_init(file_saver_1):
    """
    Проверка инициализации класса HHSaver
    """
    assert file_saver_1._HHSaver__vacancies_json == []


def test_get_vacancies_json(file_saver_1, vacancy_1):

    """
    Проверка getter'а и setter'а атрибута vacancies_json класса HHSaver
    """
    file_saver = file_saver_1
    assert file_saver.get_vacancies_json == []
    file_saver.get_vacancies_json = vacancy_1
    assert len(file_saver.get_vacancies_json) == 1


def test_vacancy_add(file_saver_2, vacancy_1, vacancy_2, headhunter_api_1):
    """
    Проверка метода vacancy_add класса HHSaver
    """
    file_saver = file_saver_2
    file_saver.vacancy_add(vacancy_1)
    with open(Path(__file__).parent.parent.joinpath("data").joinpath("vacancies_hh"), encoding="utf-8") as file:
        profile_1 = file.read()
    assert len(profile_1) > 1

    file_saver = file_saver_2
    vacancies = [vacancy_1,  vacancy_2]
    file_saver.vacancy_add(vacancies)
    with open(Path(__file__).parent.parent.joinpath("data").joinpath("vacancies_hh"), encoding="utf-8") as file:
        profile_1 = file.read()
    assert len(profile_1) > 1

    with pytest.raises(VacancyAddException):
        file_saver.vacancy_add(headhunter_api_1)


def test_vacancy_load(file_saver_1):
    """
    Проверка метода vacancy_load класса HHSaver
    """
    assert type(file_saver_1.vacancy_load()) == list


def test_vacancy_del(file_saver_2, vacancy_1):
    """
    Проверка метода vacancy_del класса HHSaver
    """
    file_saver = file_saver_2
    file_saver.vacancy_add(vacancy_1)

    with pytest.raises(VacancyDelException):
        file_saver.vacancy_del("sdf")

    file_saver.vacancy_del("test_1")
    with open(Path(__file__).parent.parent.joinpath("data").joinpath("vacancies_hh"), encoding="utf-8") as file:
        profile_1 = json.load(file)
    assert len(profile_1) == 0

