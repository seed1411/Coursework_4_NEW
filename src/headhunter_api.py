import requests
from abc import ABC, abstractmethod
from src.vacancy import Vacancy


class HH(ABC):
    """
    Выгрузка вакансий из сторонних API
    """
    @abstractmethod
    def load_vacancies(self):
        pass


class HeadHunterAPI(HH):
    """
    Класс загрузки вакансий с HeadHunter`а
    """
    __slots__ = ()

    def __init__(self):
        """
        Инициализация класса HeadHunterAPI
        """
        self.__url = 'https://api.hh.ru/vacancies'
        self.__params = {'text': '', 'page': 0, 'per_page': '100', 'area': ''}
        self.__vacancies = []  # список из вакансий (Объекты класса Vacancy)

    def __repr__(self):
        return f'url = {self.__url}, params = text: {self.__params["text"]}, page: {self.__params["page"]}, per_page: {self.__params["per_page"]}, area: {self.__params["area"]}'

    @property
    def get_params(self):
        return self.__params

    @get_params.setter
    def get_params(self, value):
        self.__params['text'] = value[0]
        self.__params['area'] = value[1]

    def load_vacancies(self) -> list:
        """
        Подключение к API HeadHunter`а и выгрузка информации о вакансиях
        :return: список из вакансий не конвертированный
        """
        vacancies_list = []
        while self.__params['page'] != 20:
            response = requests.get(self.__url, params=self.__params)
            vacancies = response.json()['items']
            vacancies_list.extend(vacancies)
            self.__params['page'] += 1
        return vacancies_list

    def cast_to_object_list(self, vacancies: list):
        """
        Создание конвертированного списка вакансий в виде объектов
        :param vacancies: список из вакансий не конвертированный
        """
        for vac in vacancies:
            try:
                vacancy = Vacancy(vac.get('published_at'),
                                  vac.get('name'),
                                  vac.get('alternate_url'),
                                  vac.get('area').get('name'),
                                  vac.get('salary').get('currency'),
                                  vac.get("salary").get("from"),
                                  vac.get("salary").get("to"),
                                  vac.get("schedule").get("name"),
                                  vac.get('snippet').get('requirement'),
                                  vac["snippet"]["responsibility"]
                                  )
            except AttributeError:
                pass
            else:
                self.__vacancies.append(vacancy)
        return self.__vacancies
