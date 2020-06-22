########################################################################################################################
# 1. Proszę utworzyć klasę definiującą współrzędne punktu na płaszczyźnie.
# Obie współrzędne proszę zdefiniować jako własności (metoda inicjalizacyjna bezparametrowa) (1p)
print('############################## ZAD_1 ##############################')

class Coords:
    def __init__(self):
        self.__x = 0
        self.__y = 0

    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self,value):
        self.__x = value
    @x.getter
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y
    @y.setter
    def y(self,value):
        self.__y = value
    @y.getter
    def y(self):
        return self.__y

ob = Coords()
print(ob.x)
ob.x = 13
print(ob.x)
########################################################################################################################
# 2. Proszę zdefiniować funkcje dodawania i odejmowania współrzędnych (z wykorzystaniem wcześniej zdefiniowanej klasy)
# oraz opatrzyć je dekoratorem (implementowanym jako funkcja) sprawdzającym czy współrzędne leżą w określonym zakresie,
# jeżeli nie - proszę zgłosić wyjątek (3p)
print('############################## ZAD_2 ##############################')

def zakres(min,max):
    def fz(fun):
        def fw(coord1,coord2):
            if min<=coord1.x<=max and min<=coord1.y<=max and min<=coord2.x<=max and min<=coord2.y<=max:
                return fun(coord1,coord2)
            else:
                raise
        return fw
    return fz


@zakres(-10,10)
def Plus(coords1,coords2):
    if type(coords1) is Coords and type(coords2) is Coords:
        newCoords = Coords()
        newCoords.x=coords1.x+coords2.x
        newCoords.y=coords1.y+coords2.y
        return newCoords

@zakres(-10,10)
def Minus(coords1,coords2):
    if type(coords1) is Coords and type(coords2) is Coords:
        newCoords = Coords()
        newCoords.x=coords1.x-coords2.x
        newCoords.y=coords1.y-coords2.y
        return newCoords

A = Coords()
A.x = 3
A.y = 8
B = Coords()
B.x = 2
B.y = -3
print("A =", A.x,",",A.y)
print("B =", B.x,",",B.y)
C = Plus(A,B)
print("C = A+B = ", C.x,",",C.y)
D = Minus(A,B)
print("D = A-B = ", D.x,",",D.y)
########################################################################################################################
# 3. Proszę utworzyć klasę z metodami statycznymi obliczającymi obwód i pole trójkąta lub czworokąta
# (dających się wpisać w okrąg, odpowiednio wzory Herona i Brahmagupty),
# zdefiniowanych poprzez współrzędne wierzchołków (klasa z zadania 1) (3p)

# Wzór Herona: P=[p(p-a)(p-b)(p-c)]1/2, gdzie: a,b,c - długości boków, p - połowa obwodu
# Wzór Brahmagupty: P=[(p-a)(p-b)(p-c)(p-d)]1/2, oznaczenia j.w.
print('############################## ZAD_3 ##############################')

import math

class Figury:
    def __init__(self):
        pass

    @staticmethod
    def ObwodTrojkata(a, b, c):
        if type(a) is Coords and type(b) is Coords and type(c) is Coords:
            ab = math.sqrt((b.x-a.x)**2 + (b.y-a.y)**2)
            bc = math.sqrt((c.x-b.x)**2 + (c.y-b.y)**2)
            ca = math.sqrt((a.x-c.x)**2 + (a.y-c.y)**2)
            return ab+bc+ca
        else:
            raise

    @staticmethod
    def PoleTrojkata(a, b, c):
        if type(a) is Coords and type(b) is Coords and type(c) is Coords:
            # i tak wymagana jest dl bokow, wiec bez sensu liczyc potem obwod korzystajac z powyzszej funkcji
            ab = math.sqrt((b.x-a.x)**2 + (b.y-a.y)**2)
            bc = math.sqrt((c.x-b.x)**2 + (c.y-b.y)**2)
            ca = math.sqrt((a.x-c.x)**2 + (a.y-c.y)**2)
            p = (ab+bc+ca)/2
            return math.sqrt(p*(p-ab)*(p-bc)*(p-ca))
        else:
            raise

    @staticmethod
    def ObwodCzworokata(a, b, c, d):
        if type(a) is Coords and type(b) is Coords and type(c) is Coords and type(d) is Coords:
            ab = math.sqrt((b.x-a.x)**2 + (b.y-a.y)**2)
            bc = math.sqrt((c.x-b.x)**2 + (c.y-b.y)**2)
            cd = math.sqrt((d.x-c.x)**2 + (d.y-c.y)**2)
            da = math.sqrt((a.x-d.x)**2 + (a.y-d.y)**2)
            return ab+bc+cd+da
        else:
            raise

    @staticmethod
    def PoleCzworokata(a, b, c, d):
        if type(a) is Coords and type(b) is Coords and type(c) is Coords and type(d) is Coords:
            # i tak wymagana jest dl bokow, wiec bez sensu liczyc potem obwod korzystajac z powyzszej funkcji
            ab = math.sqrt((b.x-a.x)**2 + (b.y-a.y)**2)
            bc = math.sqrt((c.x-b.x)**2 + (c.y-b.y)**2)
            cd = math.sqrt((d.x-c.x)**2 + (d.y-c.y)**2)
            da = math.sqrt((a.x-d.x)**2 + (a.y-d.y)**2)
            p = (ab+bc+cd+da)/2
            return math.sqrt((p-ab)*(p-bc)*(p-cd)*(p-da))
        else:
            raise TypNiezgodny("Niewlasciwy typ")

# do testow egipski trojkat + prostokat z tego trojkata i wierzch D
A = Coords()
A.x = 0
A.y = 0
B = Coords()
B.x = 0
B.y = 3
C = Coords()
C.x = 4
C.y = 0
D = Coords()
D.x = 4
D.y = 3
print("Obwod trojkata = ",Figury.ObwodTrojkata(A,B,C))
print("Pole trojkata = ",Figury.PoleTrojkata(A,B,C))
print("Obwod czworokata = ",Figury.ObwodCzworokata(A,B,D,C))
print("Pole czworokata = ",Figury.PoleCzworokata(A,B,D,C))

########################################################################################################################
# 4. Proszę utworzyć dekorator (implementowany jako klasa) umożliwiający zliczenie liczby wywołań poszczególnych
# funkcji nim obłożonych, z metodą statyczną zwracającą wynik (3p)
print('############################## ZAD_4 ##############################')