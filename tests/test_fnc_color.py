from src.fnc_color import out_blue_text, out_red_text, out_emphasized_text, out_incorrect_input_text


def test_out_red_text():
    """
    Проверка функции out_red_text
    """
    assert out_red_text("text") == "\x1b[3m\x1b[5m\x1b[31mtext\x1b[0m"


def test_out_blue_text():
    """
    Проверка функции out_blue_text
    """
    assert out_blue_text("text") == "\x1b[1m\x1b[34mtext\x1b[0m"


def test_out_emphasized_text():
    """
    Проверка функции out_emphasized_text
    """
    assert out_emphasized_text("text") == "\x1b[3m\x1b[4mtext\x1b[0m"


def test_out_incorrect_input_text():
    """
    Проверка функции out_incorrect_input_text
    """
    assert out_incorrect_input_text("text") == "\x1b[31mtext\x1b[0m"