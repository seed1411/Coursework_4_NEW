from src.fnc_color import out_blue_text, out_red_text
def test_out_red_text():
    assert out_red_text("text") == "\x1b[3m\x1b[5m\x1b[31mtext\x1b[0m"

def test_out_blue_text():
    assert out_blue_text("text") == "\x1b[1m\x1b[34mtext\x1b[0m"