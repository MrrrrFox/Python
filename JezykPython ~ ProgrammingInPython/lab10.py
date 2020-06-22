########################################################################################################################
# 1.Celem programu jest implementacja tzw. automatu komórkowego. Składa się on z N komórek, każda w stanie 0 lub 1.
# W kolejnych iteracjach stan danej komórki zmienia się zgodnie z określoną regułą, na podstawie stanu danej komórki oraz
# jej dwóch najbliższych sąsiadów (prawego i lewego) w poprzedniej iteracji.
# Regułę zapisuje się jako binarną reprezentację liczby zapisanej w systemie dziesiętnym, np. dla reguły nr 30 jej reprezentacja binarna to 00011110.
# Jeżeli każda komórka może być w dwóch stanach (0 lub 1), to możliwych jest osiem kombinacji stanu komórki i jej dwóch najbliższych sąsiadów.

#Możemy utworzyć tabelę, w górnym wierszu której przedstawiony jest stan danej komórki i jej dwóch najbliższych sąsiadów
# (lewy sąsiad, komórka, prawy sąsiad) w danej chwili czasowej, a w wierszu dolnym wpisujemy regułę automatu,
# która określa stan komórki centralnej w chwili kolejnej (przyjmujemy periodyczne warunki brzegowe -
# lewym sąsiadem komórki o indeksie 0 jest komórka o indeksie N-1, prawym sąsiadem komórki o indeksie N-1 jest komórka o indeksie 0):

#   111	110	101	100	011	010	001	000
#   0	0	0	1	1	1	1	0

# Przykład:
# t=0: 0000000001000000000
# t=1: 0000000011100000000
# t=2: 0000000110010000000
# t=3: 0000001101111000000

# Proszę utworzyć klasę Automat, a w niej:

# -> metodę inicjalizującą przyjmującą dwa parametry całkowite i jeden logiczny, pierwszy parametr określa liczbę komórek,
# drugi regułę automatu, a trzeci sposób inicjalizacji stanu początkowego: losowy bądź zera z wyjątkiem komórki w środku, równej 1
# -> metodę ewolucji automatu z parametrem określającym liczbę iteracji
# -> metodę wypisującą na ekran przebieg ewolucji (zamiast jedynek proszę wyświetlać *, a zamiast zer - spacje)

# Proszę uruchomić program dla automatu o długości 31, dla reguł 90, 94 i 182 oraz 16 iteracji (6p)
print('##############################ZAD_1##############################')

from random import randint

class Automat:
    def __init__(self, n, regula, tryb = False):    # tryb -> False => 00..00100..00, True => losowy
        self.tab = []
        self.iter = 0
        for _ in range(n):
            if tryb == False:
                self.tab.append(0)
            else:
                self.tab.append(randint(0,1))
        if tryb == False:
            self.tab[n//2]=1

    def __str__(self):
        string_to_show = "t=" + str(self.iter) + ": "
        for i in range(len(self.tab)):
            string_to_show = string_to_show + str(self.tab[i])
        return string_to_show

a1 = Automat(11,2)
a2 = Automat(19,1,True)
print(a1)
print(a2)



########################################################################################################################
# 2.Proszę utworzyć klasę Wektor dla dowolnej liczby współrzędnych, którego stan początkowy jest określony prezz metodę inicjalizacyjna.
# W klasie proszę zdefiniować metody przeciążające operatory: +, +=, -, -=, * (mnożenie wektora przez liczbę),
# *= (mnożenie wektora przez liczbę), ==, [ ] oraz funkcję len (liczba współrzędnych) i str;
# proszę także zdefiniować metodę len zwracającą długość wektora (4p)
print('##############################ZAD_2##############################')


from math import sqrt

class Wektor:

    def __init__(self, *coords):
        self.tab = []
        for item in coords:
            self.tab.append(item)

    def __len__(self):
        return len(self.tab)

    def __add__(self, vec):
        if type(vec) is Wektor:
            if len(self) == len(vec):
                newWektor = Wektor()
                for i in range(len(self.tab)):
                    newWektor.addCoord(self.tab[i] + vec.tab[i])
                return newWektor

    def __iadd__(self, vec):
        if type(vec) is Wektor:
            if len(self) == len(vec):
                for i in range(len(self.tab)):
                   self.tab[i] += vec.tab[i]
                return self

    def __sub__(self, vec):
        if type(vec) is Wektor:
            if len(self) == len(vec):
                newWektor = Wektor()
                for i in range(len(self.tab)):
                    newWektor.addCoord(self.tab[i] - vec.tab[i])
                return newWektor

    def __isub__(self, vec):
        if type(vec) is Wektor:
            if len(self) == len(vec):
                for i in range(len(self.tab)):
                    self.tab[i] -= vec.tab[i]
                return self

    def __mul__(self, liczba):
        newWektor = Wektor()
        for i in range(len(self.tab)):
            newWektor.addCoord(self.tab[i] * liczba)
        return newWektor

    __rmul__ = __mul__

    def __imul__(self, liczba):
        for i in range(len(self.tab)):
            self.tab[i] *= liczba
        return self

    def __eq__(self, vec):
        if type(vec) is Wektor:
            if len(self) == len(vec):
                for i in range(len(self.tab)):
                    if self.tab[i] != vec.tab[i]:
                        return False
                return True
        return False

    def __getitem__(self, indeks):
        if indeks<=len(self.tab)-1:
            return self.tab[indeks]

    def __str__(self):
        string_to_show = "("
        for i in range(len(self.tab)):
            string_to_show = string_to_show + str(self.tab[i])
            if i!=len(self.tab)-1:
                string_to_show = string_to_show + ","
        string_to_show = string_to_show + ")"
        return string_to_show

    def len(self):
        return sqrt(sum(x**2 for x in self.tab))

    def addCoord(self, newCoord):
        self.tab.append(newCoord)

# init
v1 = Wektor(3,2,3)
print("v1 = ", v1)
v2 = Wektor(1,4,5)
print("v2 = ", v2)
v3 = Wektor(15,10,15)
print("v3 = ", v3)
# +
print("v1+v2 = ", v1+v2)
# +=
print("v1 = ", v1, "v2 = ", v2)
v1 += v2
print("v1+=v2 -> v1 = ", v1)
# -
print("v1-v2 = ",v1-v2)
# -=
print("v1 = ", v1, "v2 = ", v2)
v1 -= v2
print("v1-=v2 -> v1 = ", v1)
# *
print("v1*5 = ", v1*5)
print("5*v1 = ", 5*v1)
# *=
v1 *= 5
print("v1*=5 -> v1 = ", v1)
# ==
print("v1 = ", v1, "v2 = ", v2, "v1==v2 = ", v1==v2)
print("v1 = ", v1, "v3 = ", v3, "v1==v3 = ", v1==v3)
# []
print("v1 = ", v1, "v1[0] = ", v1[0], "v1[-1] = ", v1[-1])
# __len__
print("v1 = ", v1, "__len__() = ", len(v1))
# len
print("v1 = ", v1, "len() = ", v1.len())