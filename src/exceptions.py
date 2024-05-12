class VacancyAddException(Exception):
    """
    Исключение в случае добавления в файл не экземпляр Vacancy
    """
    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else "Добавить в файл можно только вакансии!"

    def __str__(self):
        return self.message


class VacancyDelException(VacancyAddException):
    """
    Исключение в случае удаления из файла отсутствующей вакансии
    """
    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else "Указанная вакансия для удаления отсутствует в файле!"


class SortJobTitleException(VacancyAddException):
    """
    Исключение в случае если вакансии не найдены
    """
    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else "Найдено 0 вакансий"


