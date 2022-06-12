while True:
    try:
        X = int(input("Introduzca el numerador:"))
        Y = int(input("Intruduzca el denominador: "))
        porcentaje = round((X/Y)*100)
        if porcentaje < 1:
            print("'E'")
        elif porcentaje > 99:
            print("'F'")
        else:
            print(str(porcentaje)+"%")
        break
    except ValueError:
        print("'X' e 'Y' deben ser números enteros")
    except ZeroDivisionError:
        print("'Y' debe ser diferente de cero")