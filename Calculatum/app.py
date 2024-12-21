
from Calculatum.interfaz import muestra_menu, input_options, input_numero, muestra_resultado

def run():
    muestra_menu()
    o = input_options("Selecciona una", (1, 2, 3, 4))
    nr = input_numero("Introduce primer valor")
    nr1 = input_numero("Introduce segundo valor")
    muestra_resultado(o, nr, nr1)