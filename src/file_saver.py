import json
from pathlib import Path
from abc import ABC, abstractmethod
from src.vacancy import Vacancy
from src.exceptions import VacancyAddException, VacancyDelException


class JSONSaver(ABC):
    """
    Класс сохраняющий вакансии в файл, загружающий вакансии из файла, удаляющий вакансию в файле
    """

    @abstractmethod
    def vacancy_add(self, vacancies):
        """
        Добавление вакансии в файл JSON
        """
        pass

    @abstractmethod
    def vacancy_load(self):
        """
        Загрузка вакансий из файла JSON
        """
        pass

    @abstractmethod
    def vacancy_del(self, vacancy):
        """
        Удаление вакансии из файла JSON
        """
        pass


class HHSaver(JSONSaver):
    """
    Класс работающий с вакансиями из HeadHunterAPI`а
    """

    def __init__(self):
        """
        Инициализация класса HHSaver
        """
        self.__vacancies_json = []

    @property
    def get_vacancies_json(self) -> list:
        """
        Возвращает список вакансий(Vacancy)
        """
        return self.__vacancies_json

    @get_vacancies_json.setter
    def get_vacancies_json(self, value: Vacancy):
        """
        Внесение изменений в атрибут __vacancies_json
        """
        self.__vacancies_json.append({
            "published_at": value.published_at,
            "name": value.name,
            "alternate_url": value.alternate_url,
            "area": value.area,
            "currency": value.currency,
            "salary_for": value.salary_for,
            "salary_to": value.salary_to,
            "schedule": value.schedule,
            "requirement": value.requirement,
            "responsibility": value.responsibility
        })

    def vacancy_add(self, vacancies: (list, Vacancy)):
        """
        Запись вакансии HeadHunter в файл JSON
        """
        if type(vacancies) is list:
            for vacancy in vacancies:
                self.get_vacancies_json = vacancy
        elif isinstance(vacancies, Vacancy):
            self.get_vacancies_json = vacancies
        else:
            raise VacancyAddException
        with open(Path(__file__).parent.parent.joinpath("data").joinpath("vacancies_hh"), "w", encoding="utf-8") as file:
            json.dump(self.__vacancies_json, file, ensure_ascii=False, indent=10)

    def vacancy_load(self) -> list:
        """
        Выводит пользователю список всех вакансий HeadHunter'а из файла в виде объекта
        """
        with (open(Path(__file__).parent.parent.joinpath("data").joinpath("vacancies_hh"), encoding="utf-8") as file):
            vacancies = json.load(file)
            vacancies_list = []
            for vacancy_1 in vacancies:
                vacancies_list.append(Vacancy(**vacancy_1))
            return vacancies_list

    def vacancy_del(self, vacancy: str):
        """
        Удаляет вакансию HeadHunter'а из файла.
        В случае отсутствия удаляемой вакансии в файле выдает ошибку VacancyDelException
        !!! Удаление происходит по точному названию вакансии!!!
        :param vacancy: Передаваемая вакансия
        """
        with open(Path(__file__).parent.parent.joinpath("data").joinpath("vacancies_hh"), encoding="utf-8") as file:
            vacancies_list = json.load(file)
            for vac in vacancies_list:
                if vacancy == vac["name"]:
                    del vacancies_list[vacancies_list.index(vac)]
                    break
            else:
                raise VacancyDelException
            with open(Path(__file__).parent.parent.joinpath("data").joinpath("vacancies_hh"), "w", encoding="utf-8") as file_1:
                json.dump(vacancies_list, file_1, ensure_ascii=False, indent=10)
