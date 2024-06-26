from datetime import date
from src.fnc_color import out_red_text, out_blue_text


class Vacancy:
    """
    Вакансия, включающая в себя информацию дате публикации вакансии, названии вакансии,
    ссылки на вакансию, место работы (город), валюта оплаты, зарплата от, зарплата до,
    график работы, требования к работнику, обязанности по вакансии
    """
    __slots__ = ('published_at', 'name', 'alternate_url', 'area', 'currency', 'salary_for', "salary_to", 'schedule', 'requirement', 'responsibility')

    def __init__(self, published_at, name, alternate_url, area, currency, salary_for, salary_to, schedule, requirement, responsibility):
        """
        Инициализация класса Vacancy
        """
        # Дата публикации
        self.published_at = published_at
        # Должность
        self.name = name if name is not None else "Не указана"
        # Ссылка на вакансию
        self.alternate_url = alternate_url if alternate_url is not None else "Не указана"
        # место работы (город)
        self.area = area if area is not None else "Не указано"
        # Валюта
        self.currency = currency if currency is not None else "Не указана"
        # Зарплата "от"
        self.salary_for = salary_for if isinstance(salary_for, int) else 0
        # Зарплата "до"
        self.salary_to = salary_to if isinstance(salary_to, int) else 0
        # График занятости
        self.schedule = schedule if schedule is not None else "Не указан"
        # Требования к работнику
        self.requirement = requirement if requirement is not None else "Не указано"
        # Обязанности по вакансии
        self.responsibility = responsibility if responsibility is not None else "Не указаны"

    def __repr__(self) -> str:
        """
        Отладочный вывод класса и атрибутов экземпляра класса
        """
        return f"""{self.__class__.__name__}({self.published_at}, {self.name}, {self.alternate_url}, {self.area}, {self.currency}, {self.salary_for}, {self.salary_to}, {self.schedule}, {self.requirement}, {self.responsibility})"""

    def __str__(self) -> str:
        """
        Вывод пользователю информации о вакансии,
        с учетом склонения окончаний и количестве дней публикации
        """
        salary_range = f"{out_blue_text("Зарплата:")} от {self.salary_for} до {self.salary_to} {self.currency}"
        if self.salary_for == 0 and self.salary_to == 0:
            salary_range = {out_blue_text("Зарплата не указана;")}
        elif not self.salary_for:
            salary_range = f"{out_blue_text("Зарплата:")} до {self.salary_to} {self.currency}"
        elif not self.salary_to:
            salary_range = f"{out_blue_text("Зарплата:")} от {self.salary_for} {self.currency}"

        published_at = self.published_at_correct(self.published_at)
        days_ago = None
        if not published_at:
            days_ago = "Дата публикации не указана.\n\n"
        else:
            day = int(published_at[1])

            if day == 0:
                days_ago = f"Опубликовано сегодня. {out_red_text("БУДЬ ПЕРВЫМ!!!")}\nДата публикации: {published_at[0]} года;\n\n"
            elif day in range(5, 21) or day in range(1005, 1021) or day % 10 in range(5, 10) or day % 10 == 0:
                days_ago = f"Опубликовано {published_at[1]} дней назад.\nДата публикации: {published_at[0]} года;\n\n"
            elif day % 10 in (2, 3, 4):
                days_ago = f"Опубликовано {published_at[1]} дня назад.\nДата публикации: {published_at[0]} года;\n\n"
            elif day % 10 in (1, 1001):
                days_ago = f"Опубликовано {published_at[1]} день назад.\nДата публикации: {published_at[0]} года;\n\n"
        return (f'{days_ago}'
                f'{out_blue_text("Должность:")} {self.name};\n'
                f'{out_blue_text("Ссылка на вакансию:")} {self.alternate_url};\n'
                f'{out_blue_text("Город:")} {self.area};\n'
                f'{salary_range};\n'
                f'{out_blue_text("График работы:")} {self.schedule};\n'
                f'{out_blue_text("Требования к кандидату:")} {self.requirement};\n'
                f'{out_blue_text("Обязанности:")} {self.responsibility};\n\n\n')

    def __eq__(self, other) -> bool:
        """
        Проверка зарплат вакансий на равенство
        """
        return self.salary_for == other.salary_for

    def __lt__(self, other) -> bool:
        """
        Проверка зарплат вакансий на то что одна меньше другой
        """
        return self.salary_for < other.salary_for

    def __gt__(self, other) -> bool:
        """
        Проверка зарплат вакансий на то что одна больше другой
        """
        return self.salary_for > other.salary_for

    @staticmethod
    def published_at_correct(value) -> tuple:
        """
        Преобразует дату публикации в нужный формат
        :param value: Исходное значение даты, загруженное из HeadHunter API
        :return: кортеж из двух значений дату в формате ДД.ММ.ГГ и сколько дней назад выложено
        """
        published_date = value
        try:
            date_convert = date(int(published_date[:4]), int(published_date[5:7]), int(published_date[8:10]))
        except ValueError:
            return 0
        else:
            date_now = date.today()
            day_difference = (date_now - date_convert).days
            return date_convert.strftime("%d.%m.%Y"), day_difference
