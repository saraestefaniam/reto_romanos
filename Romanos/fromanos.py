"""
Conversor que recibe un número y lo convierte a número romano
"""

# numeros_romanos = {
#     "M": 1000,
#     "CM": 900,
#     "D": 500,
#     "CD": 400,
#     "C": 100,
#     "XC": 90,
#     "LX": 60,
#     "L": 50,
#     "XL": 40,
#     "X": 10,
#     "IX": 9,
#     "V": 5,
#     "IV": 4,
#     "I": 1

# }


def break_down(index: int, digit: str)-> int:
    """
    1. Pasar cifra a entero
    2. Devolver cifra * 10 ** posicion
    """
    digit_int = int(digit)
    broken_digit = digit_int * 10 ** index
    return broken_digit

    #esta función tambíen podría ser una sola línea, así:
    #return int(digit) * 10 ** index
    #también lo podríamos haber resulto con un lambda en la función to_roman
    #value = lambda p, c: int(c) * 10 ** p

def translate(num: int)-> str:
    symbols = {
        1:"I", 2:"II", 3:"III", 4:"IV", 5:"V", 6:"VI", 7:"VII", 8:"VIII", 9:"IX",
        10:"X", 20:"XX", 30:"XXX", 40:"XL", 50:"L", 60: "LX", 70: "LXX", 80:"LXXX", 90:"XC",
        100:"C", 200:"CC", 300:"CCC", 400:"CD", 500:"D", 600:"DC", 700:"DCC", 800:"DCCC", 900:"CM",
        1000:"M", 2000:"MM", 3000:"MMM"
    }
    return symbols[num]


def to_roman(n: int)->str:
    list_translations = []
    number_string = str(n)
    backward = number_string[::-1]
    for index, digit in enumerate(backward):
        value = break_down(index, digit)
        translated_value = translate(value)
        list_translations.append(translated_value)
    
    list_translations_backwards = list_translations[::-1]
    roman_number = ""
    for element in list_translations_backwards:
        roman_number = roman_number + element
    return roman_number






# def a_romanos(num_entrada: int)-> str:
#     romano = ""
#     if num_entrada == 0:
#         romano = None
#     for clave, value in numeros_romanos.items():
#         if value == num_entrada:
#             romano = clave
#     return romano




