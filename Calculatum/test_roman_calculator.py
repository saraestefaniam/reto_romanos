from Calculatum import roman_calculator
from Romanos import fromanos2
import pytest

def test_constructor_entero_clase_Romana():
    rn = roman_calculator.Roman_Number(8)
    assert rn.valor == 8
    assert rn.representation == "VIII"

def test_str_romanos():
    rn = roman_calculator.Roman_Number(9)
    assert str(rn) == "IX"

def test_compara_iguales():
    assert roman_calculator.Roman_Number(18) == roman_calculator.Roman_Number("XVIII")

def test_compara_mayor():
    pass

def test_compara_menor():
    pass

def test_suma_romanos():
    assert roman_calculator.Roman_Number(5) + roman_calculator.Roman_Number(10) == roman_calculator.Roman_Number(15)
    assert roman_calculator.Roman_Number(9) + 10 == roman_calculator.Roman_Number(19)
    assert 9 + roman_calculator.Roman_Number(10) == roman_calculator.Roman_Number(19)

def test():
    pass



# def test_valid_option():
#     assert roman_calculator.select(5) == input("Opción incorrecta, vuelve a ingresar opción válida")
#     #tengo duda si esto es así

# def test_sum():
#     assert roman_calculator.sum_roman(3, 4) == "VII"
#     assert roman_calculator.sum_roman("III", "IV") == "VII"
    
# def test_multiply():
#     assert roman_calculator.mult_roman(2, 5) == "X"
#     assert roman_calculator.mult_roman("II", "V") == "X"

# def test_rest():
#     assert roman_calculator.rest_roman(3, 1) == "II"
#     assert roman_calculator.rest_roman("III", "I") == "II"

# def test_divide():
#     assert roman_calculator.divide_roman(10, 2) == "V"
#     assert roman_calculator.divide_roman("X", "II") == "V"

# def test_division_0():
#     assert roman_calculator.divide_roman(10, 0) == None

# def test_negative_result():
#     with pytest.raises(ValueError) as contexto:
#         roman_calculator.rest_roman(2, 6)
#         assert str(contexto.value).endswith("operación no permitida")