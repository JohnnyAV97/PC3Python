import Funciones

BIENVENIDA = "Bienvenido al menú interactivo"
MSG = """¿Qué quieres hacer? Escribe una opción
    1) Sumar
    2) Restar
    3) Multiplicar
    4) Dividir
    5) Salir
    Opcion: """

def Main():
    print(BIENVENIDA)
    while True:
        opcion = input(MSG)
        if opcion == '1':
            n1 = Funciones.get_numero('Ingrese el primer numero: ')
            n2 = Funciones.get_numero('Ingrese el segundo numero: ')
            
            s = Funciones.sumar(n1, n2)
            print(f'la suma de los numeros es  : {s}')
            
        elif opcion == '2':
            n1 = Funciones.get_numero('Ingrese el primer numero: ')
            n2 = Funciones.get_numero('Ingrese el segundo numero: ')
            
            s = Funciones.restar(n1, n2)
            print(f'la resta de los numeros es  : {s}')

        elif opcion == '3':
            n1 = Funciones.get_numero('Ingrese el primer numero: ')
            n2 = Funciones.get_numero('Ingrese el segundo numero: ')
            
            s = Funciones.multiplicar(n1, n2)
            print(f'la multiplicacion de los numeros es  : {s}')

        elif opcion == '4':
            Funciones.dividir()

        elif opcion == '5':
            print("¡Hasta luego! Ha sido un placer ayudarte")
            break

        else:
            print("Comando desconocido, vuelve a intentarlo")

Main()