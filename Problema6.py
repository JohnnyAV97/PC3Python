import math

class Punto:

    def __init__(self,X,Y):
        self.X = X
        self.Y = Y
        if self.X == None:
            self.X = 0
        elif self.Y == None:
            self.Y = 0
        print("The __init__ method was called")
    
    def String(self,X,Y):
        punto = "("+str(X)+","+str(Y)+")"
        print("Punto: "+punto)
    
    def Cuadrante(self,X,Y):
        if X>0 and Y>0:
            print("Pertenece al primer cuadrante")
        elif X<0 and Y>0:
            print("Pertenece al segundo cuadrante")
        elif X<0 and Y<0:
            print("Pertenece al tercer cuadrante")
        elif X>0 and Y<0:
            print("Pertenece al cuarto cuadrante")
        elif X==0 and Y!=0:
            print("Se situa sobre el eje Y")
        elif X!=0 and Y==0:
            print("Se situa sobre el eje X")
        elif X==0 and Y==0:
            print("Se situa sobre el origen")
    
    def Vector(self,X,Y):
        abscisa = self.X - X
        ordenada = self.Y - Y
        resultante = "("+str(abscisa)+","+str(ordenada)+")"
        print("Vector resultante: "+resultante)
    
    def Distancia(self,X,Y):
        distancia = math.sqrt((self.X-X)**2+(self.Y-Y)**2)
        print("La distancia entre los puntos es: "+str(distancia))

class Rectangulo:

    def __init__(self,X1,Y1,X2,Y2):
        self.X1 = X1
        self.Y1 = Y1
        self.X2 = X2
        self.Y2 = Y2
        print("The __init__ method was called")
    
    def Base(self):
        base = math.abs(self.X2 - self.X1)
        print("La distancia de la base es: "+str(base))
    
    def Altura(self):
        altura = math.abs(self.Y2 - self.Y1)
        print("La distancia de la altura es: "+str(altura))

    def Area(self):
        area = self.altura * self.base
        print("El area del rectangulo es: "+str(area))

point = Punto (-2,3)
point.Distancia(4,5)