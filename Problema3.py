from cmath import pi

class CIRCULO:
    def area(self,radio):
        area = radio*radio*pi
        print("El area del circulo es: "+str(area))

circ = CIRCULO ()
circ.area(4)