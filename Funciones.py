import random

def crear_lista():
    global lista
    lista = []
    for i in range(0,20):
        lista.append(random.randint(1,100))
    return print("---La lista ha sido creada---")

def mostrar_lista():
    return print(lista)

def ordenar():
    lista.sort()
    return print(lista)