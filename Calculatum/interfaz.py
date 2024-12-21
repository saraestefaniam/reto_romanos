
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Calculatum.roman_calculator import Roman_Number

def muestra_menu():
    print("Calculatum")
    print("=========")
    print("1. Suma")
    print ("2. Resta")
    print("3. Multiplicación")
    print("4. División")

def input_options(msg:str, options: tuple):
    options = tuple(map(str, options))
    while True: 
        opt = input(f"{msg}: ")
        if opt in options:
            break
        print(f"Introduce un valor de los siguientes {options}")
    return opt


def input_numero(msg: str):
    while True:
        candidato = input(f"{msg}: ")
        try:
            res = Roman_Number(int(candidato) if candidato.isdigit() else candidato)
            break
        except ValueError:
            print("Introduce un entero o romano válido")
    return res

def muestra_resultado(opt: int, n1: Roman_Number, n2:Roman_Number):
    if opt == "1":
        ops = "+"
        res = n1 + n2
    elif opt == "2":
        ops = "-"
        res = n1 - n2
    elif opt == "3":
        ops = "x"
        res = n1 * n2
    else:
        ops = "÷"
        res = n1 / n2

    print(f"Resultado: {n1} {ops} {n2} = {res}")
