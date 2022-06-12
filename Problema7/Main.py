import Funciones

BIENVENIDA = "Bienvenido al menú interactivo"
MSG = """¿Qué quieres hacer? Escribe una opción
    1) Crear lista
    2) Mostrar lista
    3) Ordenar valores y mostrar
    4) Salir
    Opcion: """

def Main():
    print(BIENVENIDA)
    while True:
        opcion = input(MSG)
        if opcion == '1':
            Funciones.crear_lista()
            
        elif opcion == '2':
            Funciones.mostrar_lista()

        elif opcion == '3':
            Funciones.ordenar()

        elif opcion == '4':
            print("¡Hasta luego! Ha sido un placer ayudarte")
            break

        else:
            print("Comando desconocido, vuelve a intentarlo")

Main()