def test_VacancyAddException_init(exception_add_1, exception_add_2):
    assert exception_add_1.message == "Добавить в файл можно только вакансии!"
    assert exception_add_2.message == "TEST"


def test_VacancyAddException_str(exception_add_1):
    assert str(exception_add_1) == "Добавить в файл можно только вакансии!"


def test_VacancyDelException_init(exception_del_1, exception_del_2):
    assert exception_del_1.message == "Указанная вакансия для удаления отсутствует в файле!"
    assert exception_del_2.message == "TEST"
