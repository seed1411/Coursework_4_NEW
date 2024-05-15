def out_red_text(text) -> str:
    """
    Преобразовывает текст в курсив, красный цвет
    :param text: Текст который нужно преобразовать
    :return: преобразованный текст
    """
    return "\033[3m\033[5m\033[31m{}\033[0m".format(text)


def out_blue_text(text) -> str:
    """
    Преобразовывает текст в синий цвет, жирный шрифт
    :param text: Текст который нужно преобразовать
    :return: преобразованный текст
    """
    return "\033[1m\033[34m{}\033[0m".format(text)


def out_emphasized_text(text) -> str:
    """
    Преобразовывает текст в подчеркнутый
    :param text: Текст который нужно преобразовать
    :return: преобразованный текст
    """
    return "\033[3m\033[4m{}\033[0m".format(text)


def out_incorrect_input_text(text) -> str:
    """
    Преобразовывает текст в красный
    :param text: Текст который нужно преобразовать
    :return: преобразованный текст
    """
    return "\033[31m{}\033[0m".format(text)
