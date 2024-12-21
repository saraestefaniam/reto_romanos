from Romanos.fromanos2 import to_roman, to_arabigo

class Roman_Number:
    def __init__(self, num: int | str):
        if type(num) == int:
          self.valor = num
          self.representation = to_roman(num)
        elif type(num) == str:
           self.valor = to_arabigo(num)
           self.representation = num
        else:
           raise ValueError("Solo admitimos int or str")
    
    #metodo magico, transformar en cadena un objeto
    def __str__(self):
       return self.representation
    
    def __repr__(self):
        return self.__str__()

    def __add__(self, other:object):
        if isinstance(other, int):
            number_value = other
        elif isinstance(other, self.__class__):
            number_value = other.valor
        else:
            raise TypeError(f"'+' not supported between instances of 'Roman_Number' and '{other.__class__}'")
        
        sum = number_value + self.valor
        return Roman_Number(sum)
    
    def __radd__(self, other:object):
       return self + other
        #podria ser también return self.__add__(other)
    
    def __sub__(self, other:object):
        if isinstance(other, int):
            number_value = other
        elif isinstance(other, self.__class__):
            number_value = other.valor
        else: 
            raise ValueError(f"'-' not supported between instances of 'Roman_Number' and '{other.__class__}'")
        
        rest = self.valor - number_value
        return Roman_Number(rest)
    
    def __rsub__(self, other:object):
        if isinstance(other, int):
            number_value = other
        else:
            raise TypeError(f"'-' not supported between instances of 'Roman_Number' and '{other.__class__}'")
        
        rest = number_value - self.valor
        return Roman_Number(rest)
    

    def __mul__(self, other:object):
       pass

    def __truediv__(self, other:object):
       pass

    def __floordiv__(self, other:object):
       pass
    
    def __eq__(self, other:object):
       if not isinstance(other, self.__class__):
          return False
       return self.valor == other.valor
    
    def __lt__(self, other:object)-> bool: #less than
       pass

    def __le__(self, other:object)-> bool: #less or equal
       pass

    def __gt__(self, other:object)-> bool: #greater than
       pass

    def __ge__(self, other:object)-> bool: #greater or equal
       pass

    def __lt__(self, other:object)-> bool: #less than
       pass

    def __ne__(self, other:object)-> bool: #not equal
       pass
       
    def __hash__(self):
       return hash(self.valor)








# def sum_roman(n1: str, n2:str)->str:
#     result = ""

#     try:
#         #esto es pa comprobar si es que el valor que entregaron podría pasar a ser un entero
#         num_for_sum_1 = int(n1)
#         num_for_sum_2 = int(n2) 
#     except:
#         #transformar de romano a arabigo
#         num_for_sum_1 = to_arabigo(n1)
#         num_for_sum_2 = to_arabigo(n2)
    
#     result = num_for_sum_1 + num_for_sum_2
#     result = to_roman(result)
    
#     return result
    

    #if isinstance(n1) == int and isinstance(n2) == int:
        #aqui le digo que lo transforme a int
    #else:
        #aqui que entonces transforme los num a arabigo para hacer la operación
    
    #luego los vuelvo a transforma a roman para devovler 
    
    
    #isinstance #esto devuelve el tipo de variable del argumento

#def rest_roman(n1: str, n2: str)->str:
