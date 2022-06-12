class Rectangulo:
    def calcular_area(self,base,altura):
        area = base*altura
        print("El area del rectangulo es: "+str(area))

rect = Rectangulo ()
rect.calcular_area(4,50)