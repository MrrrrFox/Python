########################################################################################################################
# 1.Proszę napisać iterator zwracający kolejne liczby pierwsze z zadanego zakresu dwoma sposobami
# (jedna lub dwie klasy) i porównać ich wykorzystanie (2p).
print('############################## ZAD_1 ##############################')
class PierwszeSolo:
    def __init__(self, mi, ma):
        self.min = mi-1
        self.max = ma

    def __iter__(self):
        return self

    def __next__(self):
        self.min += 1
        while True:
            for i in range(2,self.min//2+1):
                if self.min % i == 0:
                    break
            else:
                return self.min
            self.min += 1
            if self.min > self.max:
                raise StopIteration

class PierwszeDuo:
    def __init__(self, mi, ma):
        self.min = mi
        self.max = ma

    def __iter__(self):
        return PierwszeDuoNext(self.min, self.max)

class PierwszeDuoNext:
    def __init__(self, mi, ma):
        self.min = mi-1
        self.max = ma
    def __next__(self):
        self.min += 1
        while True:
            for i in range(2,self.min//2+1):
                if self.min % i == 0:
                    break
            else:
                return self.min
            self.min += 1
            if self.min > self.max:
                raise StopIteration


print('----- 1 klasa -----')
test1_1 = PierwszeSolo(5,20)
print('pierwsze wywolanie')
for elem in test1_1:
    print(elem, end=' ')
print('\ndrugie wywolanie')
for elem in test1_1:
    print(elem, end=' ')

print('----- 2 klasy -----')
test1_2 = PierwszeDuo(5,20)
print('pierwsze wywolanie')
for elem in test1_2:
    print(elem, end=' ')
print('\ndrugie wywolanie')
for elem in test1_2:
    print(elem, end=' ')
print()
# czyli iterując 1 klasą możemy tylko raz przejsc przez iterator bo zapamietuje on swoj stan
# a iterując 2 klasami możemy przechodzić danym iteratorem przez obiekt ile razy chcemy


########################################################################################################################
# 2. Proszę napisać iterator zwracający kolejne przybliżenie miejsca zerowego metodą Newtona-Raphsona:
#xn+1=xn-f(xn)/f'(xn) z zadaną dokładnością startując od określonej wartości początkowej,
# np. f(x)=sin(x)-(0.5x)2, x=1.5 i eps=10-5 (pochodna - scipy.misc) (3p).
print('############################## ZAD_2 ##############################')
import scipy.misc
from math import sin
f = lambda x : sin(x)-(0.5*x)**2
myX = 1.5
myEps = 10**-5
class NewtonRaphsonMin:
    def __init__(self, function ,x_start, epsilon):
        self.fun = function
        self.x = x_start
        self.eps = epsilon
        self.iter = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.iter += 1
        x_prev = self.x
        self.x = x_prev - self.fun(x_prev)/scipy.misc.derivative(self.fun, x_prev)
        if abs(self.x-x_prev) < self.eps:
            raise StopIteration
        return (self.iter,self.x)

test2 = NewtonRaphsonMin(f,myX,myEps)
for elem in test2:
    print(elem)
print()

########################################################################################################################
# 3. Proszę napisać iterator liczb pseudolosowych. Ciąg taki otrzymujemy ze wzoru:
# Xn+1 = (aXn + c) mod m, dla m = 2^31-1, a = 7^5, c = 0, x0 = 1.
# Korzystając z zaimplementowanego iteratora proszę wylosować 10^5 par liczb z przedziału [0,1).
# Proszę sprawdzić jaki procent wylosowanych par mieści się w kwadracie o boku 0.1*n, gdzie n∈(1,10].
# Otrzymany wynik proszę porównać z wynikiem uzyskiwanym z wykorzystaniem generatora liczb pseudolosowych z języka Python (5p).
print('############################## ZAD_3 ##############################')

import random

myM = 2**31-1
myA = 7**5
myC = 0
my_x_0 = 1

width = 0.1

n = 10**5

class Pseudolosowe:
    def __init__(self, m, a, c, x_0):
        self.m = m
        self.a = a
        self.c = c
        self.x = x_0
    def __iter__(self):
        return self
    def __next__(self):
        self.x = (self.a*self.x+self.c)%self.m
        return self.x/self.m

pseudoLos = Pseudolosowe(myM,myA,myC,my_x_0)
myAcc = [0 for _ in range(2,11)]
randAcc = [0 for _ in range(2,11)]
# funkcja pomocnicza czy punkt nalezy do kwadratu o boku a
def InSquare(point, sq_a):
    if point[0] < sq_a and point[1] < sq_a:
        return 1
    return 0
# losuje punkty, dla kazdego punktu sprawdzam czy nalezy do danego kwadratu
for i in range(n):
    myPara = (next(pseudoLos), next(pseudoLos))
    randomPara = (random.random(),random.random())
    for j in range(2,11):
        myAcc[j-2] += InSquare(myPara,width*j)
        randAcc[j-2] += InSquare(randomPara,width*j)
# powiedzmy, obsluga outputu - wymagane byly procenty
for i in range(9):
    myAcc[i] = myAcc[i]/n*100
    randAcc[i] = randAcc[i]/n*100

print(myAcc)
print(randAcc)