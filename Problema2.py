while True:
    try:
        data = input("Ingrese la lista de calificaciones separadas por ',': ")
        data = data.strip()
        data = data.split(',')
        lista = []
        for m in data:
            m = int(m)
            lista.append(m)
        print(lista)
        break
    except:
        print("Existe un error de tipeo")