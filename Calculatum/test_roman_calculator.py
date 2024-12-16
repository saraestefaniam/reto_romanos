from Calculatum import roman_calculator
import pytest

def test_valid_option():
    assert roman_calculator.select(5) == input("Opción incorrecta, vuelve a ingresar opción válida")
    #tengo duda si esto es así

def test_sum():
    assert roman_calculator.sum_roman(3, 4) == "VII"
    assert roman_calculator.sum_roman("III", "IV") == "VII"
    
def test_multiply():
    assert roman_calculator.mult_roman(2, 5) == "X"
    assert roman_calculator.mult_roman("II", "V") == "X"

def test_rest():
    assert roman_calculator.rest_roman(3, 1) == "II"
    assert roman_calculator.rest_roman("III", "I") == "II"

def test_divide():
    assert roman_calculator.divide_roman(10, 2) == "V"
    assert roman_calculator.divide_roman("X", "II") == "V"

def test_division_0():
    assert roman_calculator.divide_roman(10, 0) == None

def test_negative_result():
    with pytest.raises(ValueError) as contexto:
        roman_calculator.rest_roman(2, 6)
        assert str(contexto.value).endswith("operación no permitida")

