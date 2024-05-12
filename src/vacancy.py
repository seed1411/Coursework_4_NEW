from datetime import date, datetime


class Vacancy:
    """
    Вакансия, включающая в себя информацию дате публикации вакансии, названии вакансии,
    ссылки на вакансию, место работы (город), валюта оплаты, зарплата от, зарплата до,
    график работы, требования к работнику, обязанности по вакансии
    """
    __slots__ = (
        'published_at', 'name', 'alternate_url', 'area', 'currency', 'salary_for', "salary_to", 'schedule', 'requirement', 'responsibility')

    def __init__(self, published_at, name, alternate_url, area, currency, salary_for, salary_to, schedule, requirement,
                 responsibility):
        self.published_at = self.published_at_correct(published_at)  # дата публикации
        self.name = name if name is not None else "Не указана" # Должность
        self.alternate_url = alternate_url if alternate_url is not None else "Не указана"  # Ссылка на вакансию
        self.area = area if area is not None else "Не указано"  # место работы (город)
        self.currency = currency if currency is not None else "Не указана"  # валюта
        self.salary_for = salary_for if isinstance(salary_for, int) else 0  # Зарплата "от"
        self.salary_to = salary_to if isinstance(salary_to, int) else 0  # Зарплата "от"
        self.schedule = schedule if schedule is not None else "Не указан"  # график занятости
        self.requirement = requirement if requirement is not None else "Не указано"  # требования к работнику
        self.responsibility = responsibility if responsibility is not None else "Не указаны"  # обязанности по вакансии

    def __repr__(self):
        return f"""{self.__class__.__name__}({self.published_at},{self.name}, {self.alternate_url}, {self.area}, {self.currency}, {self.salary_for}, {self.salary_to}, {self.schedule}, {self.requirement}, {self.responsibility})"""

    def __str__(self):
        salary_range = f"Зарплата от {self.salary_for} до {self.salary_to} {self.currency }"
        if not self.salary_for:
            salary_range = f"Зарплата до {self.salary_to} {self.currency}"
        elif not self.salary_to:
            salary_range = f"Зарплата от {self.salary_for} {self.currency}"
        elif self.salary_for == 0 and self.salary_to == 0:
            salary_range = "Зарплата не указана"
        try:
            days = ""
            if int(self.published_at[1]) in range(5, 21) or int(self.published_at[1]) in range(1005, 1021) or int(self.published_at[1]) % 10 in range(5,10) or int(self.published_at[1]) % 10 == 0:
                days = "дней"
            elif int(self.published_at[1]) % 10 in (2, 3, 4):
                days = "дня"
            elif int(self.published_at[1]) % 10 in (1, 1001):
                days = "день"
        except ValueError:
            pass
        finally:
            return (f'Вакансия опубликована {self.published_at[1]} {days} назад.\n'
                    f'Дата публикации: {self.published_at[0]} года;\n\n'
                    f'Должность: {self.name};\n'
                    f'Ссылка на вакансию: {self.alternate_url};\n'
                    f'Город: {self.area};\n'
                    f'{salary_range};\n'
                    f'График работы: {self.schedule};\n'
                    f'Требования к кандидату: {self.requirement};\n'
                    f'Обязанности: {self.responsibility};\n\n\n')

    def __eq__(self, other):
        return self.salary_for == other.salary_for

    def __lt__(self, other):
        return self.salary_for < other.salary_for

    def __gt__(self, other):
        return self.salary_for > other.salary_for

    @staticmethod
    def published_at_correct(value):
        """
        Преобразует дату публикации в нужный формат
        :param value: Исходное значение даны, загруженное из HeadHunter API
        :return: кортеж из двух значений дату в формате ДД.ММ.ГГ и сколько дней назад выложено
        """
        published_at = value
        date_convert = date(int(published_at[:4]), int(published_at[5:7]), int(published_at[8:10]))
        date_now = date.today()
        day_difference = str(date_now - date_convert).split()
        return date_convert.strftime("%d.%m.%Y"), day_difference[0]
