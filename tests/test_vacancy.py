from datetime import date


def test_init(vacancy_1):
    assert vacancy_1.published_at == "2024-01-01"
    assert vacancy_1.name == "test_1"
    assert vacancy_1.alternate_url == "test_1"
    assert vacancy_1.area == "test_1"
    assert vacancy_1.currency == "RUR"
    assert vacancy_1.salary_for == 0
    assert vacancy_1.salary_to == 0
    assert vacancy_1.schedule == "Полный"
    assert vacancy_1.requirement == "test_1"
    assert vacancy_1.responsibility == "test_1"


def test_repr(vacancy_1):
    assert repr(vacancy_1) == 'Vacancy(2024-01-01, test_1, test_1, test_1, RUR, 0, 0, Полный, test_1, test_1)'


def test_published_at_correct(vacancy_1):
    today = (date.today() - date(2024, 1, 1)).days
    assert vacancy_1.published_at_correct(vacancy_1.published_at) == ("01.01.2024", today)


def test_str_salary(vacancy_1, vacancy_2, vacancy_3, vacancy_4):
    assert str(vacancy_1) != False
    assert "{'\\x1b[1m\\x1b[34mЗарплата не указана;\\x1b[0m'};\n" in str(vacancy_1)
    assert '\x1b[1m\x1b[34mЗарплата:\x1b[0m до 1 USD;\n' in str(vacancy_2)
    assert '\x1b[1m\x1b[34mЗарплата:\x1b[0m от 1 USD;\n' in str(vacancy_3)
    assert '\x1b[1m\x1b[34mЗарплата:\x1b[0m от 1 до 1 USD;\n' in str(vacancy_4)


def test_eq(vacancy_1, vacancy_2, vacancy_3, vacancy_4):
    assert vacancy_3 == vacancy_4
    assert vacancy_2 != vacancy_3


def test_lt(vacancy_1, vacancy_3):
    assert vacancy_1 < vacancy_3


def test_gt(vacancy_4, vacancy_2):
    assert vacancy_4 > vacancy_2
