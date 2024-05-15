import pytest


def test_init(headhunter_api_1):
    """
    Проверка инициализации класса HeadHunterAPI
    """
    assert headhunter_api_1._HeadHunterAPI__url == 'https://api.hh.ru/vacancies'
    assert headhunter_api_1._HeadHunterAPI__params == {'text': '', 'page': 0, 'per_page': '100', 'area': ''}
    assert headhunter_api_1._HeadHunterAPI__vacancies == []


def test_repr(headhunter_api_1):
    """
    Проверка метода __repr__ класса HeadHunterAPI
    """
    assert repr(headhunter_api_1) == "url = https://api.hh.ru/vacancies, params = text: , page: 0, per_page: 100, area: "


def test_get_params(headhunter_api_1, headhunter_api_2):
    """
    Проверка getter`а и setter`а для атрибута __params класса HeadHunterAPI
    """
    assert headhunter_api_1.get_params == {'text': '', 'page': 0, 'per_page': '100', 'area': ''}
    assert headhunter_api_2.get_params == {'text': 'python', 'page': 0, 'per_page': '100', 'area': 113}


def test_load_vacancies(headhunter_api_3):
    """
    Проверка метода load_vacancies класса HeadHunterAPI
    """
    vacancies_list = headhunter_api_3
    assert type(vacancies_list) == list
    assert vacancies_list is not False


def test_cast_to_object_list(headhunter_api_1, headhunter_api_3):
    """
    Проверка метода cast_to_object_list класса HeadHunterAPI
    """
    vacancies = headhunter_api_3
    assert type(headhunter_api_1.cast_to_object_list(vacancies)) == list
    with pytest.raises(AttributeError):
        for vacancy in vacancies:
            vacancy.get("salary").get("from")
