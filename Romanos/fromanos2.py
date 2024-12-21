"""
Conversor que recibe un número y lo convierte a número romano
"""

roman_numbers = {
    "M": 1000,
    "CM": 900,
    "D": 500,
    "CD": 400,
    "C": 100,
    "XC": 90,
    "LX": 60,
    "L": 50,
    "XL": 40,
    "X": 10,
    "IX": 9,
    "V": 5,
    "IV": 4,
    "I": 1
}

def to_roman(num: int)-> str:
    roman = ""
    if num == 0 or num > 3000:
        roman = None
    else:
        for key, value in roman_numbers.items():
            while value <= num:
                num = num - value
                roman = roman + key
    return roman

def may_rest(list_of_rests: list, rest: int)->bool:
    try:
        last_rest = str(list_of_rests[-1])
    except IndexError:
        return True
    
    current_rest = str(rest)
    result = True
    
    #aqui estamos comprobando la longitud del número de restas (ahora string)
    # #si la longitud de la última resta (por ej 900) es igual a la resta actual (300)
    # #entonces ya no puede seguir restando porque esta queriendo restar centenas con centenas
    if len(last_rest) == len(current_rest):
        result = False
    
    return result

def may_sum(value:int, the_rest:int)->bool:
    result = False
    if len(str(value)) < len(str(the_rest)):
      result = True
    return result
   

def to_arabigo(roman_num: str)-> int:
    """
    Recibe un número romano y lo convierte a entero
    """
    if check_repetition(roman_num):
       raise ValueError(f"{roman_num} es un número inválido")
    result = 0
    previous_value = 1001
    substract = lambda x: x-(2 * previous_value)
    rests_allowed = [(1, 5), (1, 10), (10, 100), (100, 500), (100, 1000)]
    #rests_made = []
    rested = False
    the_rest = 0

    for char in roman_num:
        #recorre el diccionario y pide que traiga el valor del caracter o, si no está, por defecto que de 0
        value = roman_numbers.get(char, 0)
        if value == 0:
            raise ValueError (f"{char} no es un símbolo romano")
        
        if value > previous_value:
            if rested:
               raise ValueError(f"Restas anidadas")
            if (previous_value, value) in rests_allowed:
                the_rest = value - previous_value
                # if not may_rest(rests_made, the_rest):
                #    raise ValueError (f"esta resta no se puede realizar")
                #rests_made.append(the_rest)
                result = result + substract(value)
                rested = True
                #if rested and len(pv_str) >= len(tr_str):
                #    raise ValueError (f"esta suma no se puede realizar")
            else:
               raise ValueError(f"{previous_value}, {value} no es una expresión correcta")
        else:
            if rested:
                if may_sum(value, the_rest):
                  result = result + value
                  rested = False
                else:
                  raise ValueError(f"suma no se puede realizar")
            else:
              result = result + value
        previous_value = value

    return result

def find_streak(haystack, needle, streak):
  """
  Predicado que devuelve True si needle aparece streak veces seguido dentro de haystack
  """
  occs = 0
  is_streak = False
  for item in haystack:
    if item == needle:
      occs = occs + 1
      is_streak = True
      if occs == streak:
        break
    else:
      occs = 0
      is_streak = False
  return is_streak and occs >= streak

def check_repetition(num_roman:str)->bool:
   no_repeat = [("I", 4), ("X", 4), ("C", 4), ("M", 4), ("V", 2), ("L", 2), ("D", 2)]
   is_streak = False
   for char, limit in no_repeat:
      if find_streak(num_roman, char, limit):
        is_streak = True
        break
   return is_streak
    # def check_repetition(num_roman: str)->bool:
    #     return find_streak((num_roman, "I", 4) or \
    #             find_streak(num_roman, "X", 4) or \
    #             find_streak(num_roman, "C", 4) or \
    #             find_streak(num_roman, "M", 4))


