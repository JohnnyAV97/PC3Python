import math

def sumar(x:float, y: float)->float :
    """Retorna la suma de x + y"""
    return x + y

def restar(x:float, y: float)->float :
    """Retorna la resta de x - y"""
    return x - y

def multiplicar(x:float, y: float)->float :
    """Retorna la multiplicacion de x * y"""
    return x * y

def dividir()->float :
    """Retorna la division de x / y"""
    x = get_numero('Ingrese el primer numero: ')
    y = get_numero('Ingrese el segundo numero: ')
    try:
        division = x / y
        print(f'la division de los numeros es  : {division}')
    except ZeroDivisionError:
        print("No es posible dividir entre cero")
        return dividir()

def get_numero(msg: str='Ingrese un número entero: ')->int:
    """Solicita un número"""
    try:
        x = int(input(msg))
        return x
    except ValueError:
        print("Tipo de dato no valido")
        return get_numero(msg)