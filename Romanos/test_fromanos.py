import fromanos

# def test_simbolos_sencillos():
#     assert fromanos.to_roman(1) == "I", "número incorrecto"
#     assert fromanos.to_roman(500) == "D", "número incorrecto"

# def test_doble_repeticion():
#     assert fromanos.to_roman(2) == "II"
#     assert fromanos.to_roman(200) == "CC"

def test_break_down():
    assert fromanos.break_down(0, "9") == 9
    assert fromanos.break_down(1, "3") == 30
    assert fromanos.break_down(2, "9") == 900
    assert fromanos.break_down(3, "1") == 1000

def test_translate():
    assert fromanos.translate(9) == "IX"
    assert fromanos.translate(30) == "XXX"
    assert fromanos.translate(900) == "CM"
    assert fromanos.translate(1000) == "M"

def test_to_roman_many():
    assert fromanos.to_roman(1939) == "MCMXXXIX"