from pytest import fixture
from src.vacancy import Vacancy



@fixture
def vacancy_1():
    return Vacancy("2024-01-01", "test_1", "test_1", "test_1", "RUR", 0, 0, "Полный", "test_1", "test_1")


@fixture
def vacancy_2():
    return Vacancy("2024-02-05", "test_2", "test_2", "test_2", "USD", 0, 1, "Сменный", "test_2", "test_2")


@fixture
def vacancy_3():
    return Vacancy("2024-02-05", "test_3", "test_3", "test_3", "USD", 1, 0, "Гибкий", "test_3", "test_4")


@fixture
def vacancy_4():
    return Vacancy("2024-02-05", "test_4", "test_4", "test_4", "USD", 1, 1, "Удаленный", "test_4", "test_4")
