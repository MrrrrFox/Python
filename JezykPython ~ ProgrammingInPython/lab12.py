########################################################################################################################
# 1. Proszę napisać abstrakcyjną klasę Calka z metodą inicjalizacyjną określającą granice całkowania, liczbę kroków oraz
# funkcję podcałkową (proszę skontrolować poprawność przekazanych parametrów) oraz metodą abstrakcyjną
# obliczającą wartość całki.
# Następnie proszę utworzyć klasy dziedziczące po klasie Calka z metodami obliczającymi wartość całki odpowiednio
# metodą trapezów lub Simpsona, w metodzie proszę umieścić komentarz dokumentacyjny.
# Potrzebne wzory są w pliku: calki1.pdf (3.(3)p)
print('############################## ZAD_1 ##############################')

from abc import ABC
from abc import abstactmethod

f = lambda x: x**2

class Calka(ABC):
    def __init__(self,Min,Max,N,Func):
        self.min = Min
        self.max = Max
        self.n = N
        self.fun = Func
    @abstractmethod # metoda abstrakcyjna tak jak w podr
    def calkowanie(self):
        '''Metoda abstrakcyjna'''

class CalkaTrapezy(Calka):
    def calkowanie(self):   # calkowanie metoda trapezow
        '''Definicja metody abstrakcyjnej'''
        self.krok = (self.max-self.min)/self.n
        self.suma = 0
        #metoda
        print("calka metoda trapezow: ", self.suma)

class CalkaSimpson(Calka):
    def calkowanie(self):   # calkowanie metoda Simpsona
        '''Definicja metody abstrakcyjnej'''
        self.krok = (self.max-self.min)/(2*self.n)
        self.suma = 0
        #metoda
        print("calka metoda trapezow: ", self.suma)

########################################################################################################################
# 2.Proszę napisać klasę implementującą stos, klasa ma obsługiwać możliwość tworzenia pustego stosu bądź inicjalizacji
# istniejącym stosem (obiektem klasy), dodawania i usuwania elementu, dodawania elementów innego stosu,
# zwracania rozmiaru i wypisywania stosu.
# Następnie proszę napisać klasę dziedziczącą po klasie stosu i implementującą stos posortowany (rosnąco lub malejąco).
# W tym przypadku element/elementy innego stosu można do stosu dodać pod warunkiem zachowania porządku sortowania.
# Proszę sprawdzić jaki jest średni rozmiar posortowanego stosu, który wypełniamy całkowitymi liczbami losowymi
# z przedziału [0,100] losując 100 wartości (średnia po 100 powtórzeniach) (3.(3)p)
print('############################## ZAD_2 ##############################')

from random import randint

class stos:
    def __init__(self, stos2=None):
        if type(stos2) is stos:
            self.data = [elem for elem in stos2.data]
        else:
            self.data = []
    def push(self,elem):
        self.data.append(elem)
    def pop(self):
        return self.data.pop(len(self.data)-1)
    def push_stos(self, stos2):
        if type(stos2) is stos:
            for elem in stos2.data:
                self.push(elem)
        else:
            print("argument nie jest typu stos!")
    def __len__(self):
        return len(self.data)
    def __str__(self):
        print(self.data, end="")
        return ""

# stos rosnacy - podejscie intuicyjne
class sorted_stos(stos):
    def __init__(self, stos2=None):
        if type(stos2) is sorted_stos:
            self.data = [elem for elem in stos2.data]
        else:
            self.data = []
    def push(self,elem):
        if len(self.data)==0 or elem>=self.data[-1]:
            self.data.append(elem)
    def push_stos(self, stos2):
        if type(stos2) is sorted_stos:
            for elem in stos2.data:
                self.push(elem)
        else:
            print("argument nie jest typu sorted_stos!")
# testy
"""
# TEST1 - tylko stos
S = stos()
S.push(10)
S.push(3)
S.push(15)
print("S = ", S)
tmp=S.pop()
print("after pop S = ", S)
print("pop value = ", tmp)

# TEST2 stos + stos
S2 = stos(S)
print("S = ", S)
print("S2 = ", S2)
S2.push(44)
print("S = ", S)
print("S2 = ", S2)
S2.push_stos(S)
print("S = ", S)
print("S2 = ", S2)
print("S2 len = ", len(S2))

# TEST3 sorted stos
S3 = sorted_stos()
S3.push(2)
S3.push(10)
S3.push(7)
print("sorted stos S3 = ", S3)
S3.push_stos(S)
print("sorted stos S3 = ", S3)
S4 = sorted_stos(S2)
S5 = sorted_stos(S3)
S5.push(72)
print("sorted stos S3 = ", S3)
print("sorted stos S4 = ", S4)
print("sorted stos S5 = ", S5)
"""
# average len
sum_len = 0
for _ in range(100):
    aver = sorted_stos()
    for _ in range(100):
        aver.push(randint(0,100))
    #print(aver)
    sum_len = sum_len+len(aver)
print("srednia dlugosc posortowanego stosu to: ", sum_len/100)

########################################################################################################################
# 3.Proszę zaimplementować klasę pozwalającą na zliczanie linii, słów i znaków w pliku
# (metody inicjalizująca i zliczająca). W klasie proszę także zaimplementować bezparametrową metodę statyczną zwracają
# komunikat analogiczny do komunikatu zwracanego przez polecenie systemowe linuxa wc w przypadku jednoczesnego
# zliczania dla kilku plików (3.(3)p)
#Przykład:
#$wc AA.py BB.py
#   50    91   944 AA.py
#   80  117 1281 BB.py
# 130  208 2225 razem
print('############################## ZAD_3 ##############################')

class fileDataCounter:
    l = 0
    w = 0
    m = 0
    def __init__(self, *filesToExplore):
        self.files = []
        for file in filesToExplore:
            self.files.append(file)
        self.lines = self.words = self.marks = 0
    def count(self):
        print("lines\twords\tmarks\t\tname")
        for file in self.files:
            with open(file,"r") as currentFile:
                self.lines = self.words = self.marks = 0
                for line in currentFile:
                    self.lines += 1
                    words_tab = line.split()
                    self.words += len(words_tab)
                    self.marks += len(line)
                    fileDataCounter.l += self.lines
                    fileDataCounter.w += self.words
                    fileDataCounter.m += self.marks
                print(self.lines,'\t\t',self.words,'\t\t',self.marks,'\t\t',file)
        if len(self.files) >1:
            fileDataCounter.exploreAll()

    @staticmethod
    def exploreAll():
        print(fileDataCounter.l,'\t\t',fileDataCounter.w,'\t\t',fileDataCounter.m,'\t\t',"RAZEM")

A = fileDataCounter("test3.txt","test3_2.txt")
A.count()