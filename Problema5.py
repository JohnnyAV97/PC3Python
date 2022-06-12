import random
class Alumno:
    def Display(self,nombre,numero_registro):
        print("Nombre: "+str(nombre))
        print("Numero de registro: "+str(numero_registro))

    def setAge(self):
        print("Edad del estudiante: "+str(random.randint(5,50)))

    def setNota(self):
        print("Nota del estudiante: "+str(random.randint(0,20)))

alumno1 = Alumno()

alumno1.Display("Juan",10)
alumno1.setAge()
alumno1.setNota()