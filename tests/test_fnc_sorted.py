from src.fnc_sorted import id_area, sort_currency, sort_salary, sort_schedule, print_vacancies
import builtins
from mock import patch

from src.vacancy import Vacancy


def test_id_area():
    """
    Проверка функции id_area
    """
    with patch.object(builtins, 'input', lambda _: "Россия"):
        assert id_area() == "113"


def test_sort_currency(list_sorted):
    """
    Проверка функции sort_currency
    """
    with patch.object(builtins, 'input', lambda _: "RUR.,"):
        assert sort_currency(list_sorted) == [Vacancy("2024-01-01", "test_1", "test_1", "test_1", "RUR", 1000, 2000, "Полный день", "test_1", "test_1")]


def test_sort_salary(list_sorted):
    """
    Проверка функции sort_salary
    """
    with patch.object(builtins, 'input', lambda _: "4000"):
        assert sort_salary(list_sorted) == [Vacancy("2024-02-05", "test_4", "test_4", "test_4", "USD", 4000, 5000, "Удаленная работа", "test_4", "test_4")]


def test_sort_schedule(list_sorted):
    """
    Проверка функции sort_schedule
    """
    with patch.object(builtins, 'input', lambda _: "Удаленная,."):
        assert sort_schedule(list_sorted) == [Vacancy("2024-02-05", "test_4", "test_4", "test_4", "USD", 4000, 5000, "Удаленная работа", "test_4", "test_4")]

    with patch.object(builtins, 'input', lambda _: ""):
        assert sort_schedule(list_sorted) == list_sorted


def test_sort_top(list_sorted):
    """
    Проверка функции sort_top
    """
    with patch.object(builtins, 'input', lambda _: ""):
        assert type(sort_schedule(list_sorted)) == list


def test_print_vacancies():
    """
    Проверка функции print_vacancies
    """
    with patch.object(builtins, 'input', lambda _: ""):
        assert print_vacancies() is None

