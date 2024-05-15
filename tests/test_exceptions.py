def test_VacancyAddException_init(ExceptionAdd_1, ExceptionAdd_2):
    assert ExceptionAdd_1.message == "Добавить в файл можно только вакансии!"
    assert ExceptionAdd_2.message == "TEST"


def test_VacancyAddException_str(ExceptionAdd_1):
    assert str(ExceptionAdd_1) == "Добавить в файл можно только вакансии!"


def test_VacancyDelException_init(ExceptionDel_1, ExceptionDel_2):
    assert ExceptionDel_1.message == "Указанная вакансия для удаления отсутствует в файле!"
    assert ExceptionDel_2.message == "TEST"
