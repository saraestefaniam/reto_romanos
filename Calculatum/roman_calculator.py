from Romanos.fromanos2 import to_roman, to_arabigo

def sum_roman(n1: str, n2:str)->str:
    result = ""

    try:
        #esto es pa comprobar si es que el valor que entregaron podría pasar a ser un entero
        num_for_sum_1 = int(n1)
        num_for_sum_2 = int(n2) 
    except:
        #transformar de romano a arabigo
        num_for_sum_1 = to_arabigo(n1)
        num_for_sum_2 = to_arabigo(n2)
    
    result = num_for_sum_1 + num_for_sum_2
    result = to_roman(result)
    
    return result
    

    #if isinstance(n1) == int and isinstance(n2) == int:
        #aqui le digo que lo transforme a int
    #else:
        #aqui que entonces transforme los num a arabigo para hacer la operación
    
    #luego los vuelvo a transforma a roman para devovler 
    
    
    #isinstance #esto devuelve el tipo de variable del argumento

#def rest_roman(n1: str, n2: str)->str:
