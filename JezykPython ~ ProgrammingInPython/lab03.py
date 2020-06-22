#!/usr/bin/env python3.7

from sys import argv
from random import randint

# slowniki - nawiasy klamrowe
# s= {} - pusty slownik, pary klucz+wartosc

# klucz = identyfikator, nie moze sie zmienic wiec jest unikalny
# zatem string, krotka itp sa dobrymi kluczami

# s[k] = w - dodaje do slownika / nadpisuje to co jest w slowniku pdo tym indeksem
# del() [instrukcja] / pop() [metoda] - usuwa ze slownika del usuwa i jak nie ma to wyjatek, pop usuwa i zwraca wartosc usuwanego klucza 

# z jednego slownika do drugiego -> update()
# rozmiar slownika -> len()
# czy klucz wystepuje w slowniku? -> if k in s
# iteracja po kluczach -> for k in s
# usuwanie wszystkich elementow -> clear
# s.keys -> klucze
# s.values -> wartosci
# s.items -> pary klucz+wartosc
# s.default(k,w), slownik s, klucz k, wartosc w, nie ma klucza -> dodaje do slownika i zwraca klucz, jezeli istnieje to zwraca wartosc np. s.default(k, []) - za pierwszym razem nic, za drugim mozna wywolywac dalej, np s.default(k, []).append()

# k,w - zbior, k:w - slownik
# {k:w for ...}

#modul random - losowanie liczb z roznych rozkladow, np random() -> od 0 do 1
# randint() - z obustronnie domknietego, randrange() - dziala jak range
# ustawianie ziarna -> seed

# losowe ustawienie zbioru wartosci -> shuffle
# losowanie pojedynczej wartosci z sekwencji -> choice
# choices -> moga sie powtarzac
# sample -> bez powtorzen

# funkcje: def fun():
				#cialo
				# return...


# enumerate(seq) - na wyjsciu krotki, indeks, wartosc














    #Proszę napisać funkcję sprawdzającą czy liczba przekazana jako parametr jej wywołania jest liczbą palindromową (2p)

def pal(liczba):
	return str(liczba) == str(liczba)[::-1]

print(pal(223))
print(pal(4114))

    #Proszę utworzyć słownik zawierający 100 elementów, w którym klucze są wartościami losowymi z przedziału [100,10000]; jeżeli w słowniku istnieje już klucz równy wylosowanej wartości nic nie robimy w przeciwnym wypadku dodajemy do słownika element (klucz: palindrom), gdzie palindrom=True/False (1p)

slownik = {}
i = 0
while len(slownik) < 100:
	val = randint(100,10000)
	if val not in slownik:
		slownik.setdefault(val,pal(val))
	else:
		i = i+1
print(slownik)
print(len(slownik))
print(i)

    #Proszę utworzyć listę stu wartości losowych z przedziału [0,20). Następnie na podstawie tej listy proszę utworzyć dwa słowniki: pierwszy - klucze wartości parzyste z listy, drugi - nieparzyste; w obu wartości - lista indeksów (określonych iteracyjnie z wykorzystaniem metody setdefault i funkcji enumerate) danego klucza w liście. Następnie na podstawie jednego z otrzymanych słowników proszę utworzyć nowy słownik, w którym klucze zostają takie same jak w słowniku wejściowym, wartości tworzymy natomiast w sposób następujący: jeżeli lista będąca wartością związaną z danym kluczem zawiera jakieś wartości podzielne bez reszty przez 3 ich lista stanowi wartość związaną z kluczem w nowym słowniku, jeżeli takich liczb nie ma wartość jest krotką(maksymalny indeks[, minimalny indeks]) (1.5p)

slownikp = {}
slowniknp = {}
randlist = [randint(0,19) for _ in range(100)]
for i,j in enumerate(randlist):
	if j%2 == 0:
		slownikp.setdefault(j,[]).append(i)
	else:
		slowniknp.setdefault(j,[]).append(i)
print(slownikp)
print(slowniknp)

slownik3 = {k:slownikp[k] if [i for i in slownikp[k] if i%3 ==0] else (max(slownikp[k]), min(slownikp[k])) for k in slownikp}
print('slownik3 ',slownik3)

    #Proszę utworzyć słownik o rozmiarze równym wartości pierwszego parametru przekazanego do programu. Kluczami w tym słowniku mają być kolejne wartości naturalne, a wartościami liczby losowe z przedziału [2,15). Następnie proszę na jego podstawie utworzyć listę, której elementami są krotki (wartość, klucz) oraz słownik, w którym zostaną zamienione miejscami wartości z kluczami (1.5p)

slownik4 = {i:randint(2,14) for i in range(0,int(argv[1]))}
print(slownik4)
list = [(i,slownik4[i]) for i in slownik4]
print(list)
slownik4_rev = {v:k for k,v in slownik4.items()}
print(slownik4)
print(slownik4_rev)

    #Proszę utworzyć listę 100 wartości losowych z przedziału [0,11). Następnie proszę na jej podstawie utworzyć słownik, w którym kluczami będą wartości z przedziału, z którego liczby były losowane, wartościami będą natomiast listy z indeksami (określonymi z wykorzystaniem metod setdefault i index) ich wystąpień w liście (2p)

randlist = [randint(0,10) for _ in range(100)]
slownik = {}
for i in randlist:
	slownik.setdefault(i,[]).append(randlist.index(i,0 if len(slownik[i])==0 else slownik[i][-1]+1 ))
print(randlist)
print(slownik)

    #Proszę utworzyć dwa słowniki o rozmiarze 10, w których kluczami są kolejne wartości naturalne, a wartościami liczby losowe z przedziału [1,100). Następnie w obu słownikach proszę zamienić miejscami klucze z wartościami. Na podstawie tak otrzymanych słowników proszę utworzyć nowy słownik, w którym klucze są kluczami występującymi w obu wcześniej utworzonych słownikach, wartościami natomiast są dwuelementowe krotki wartości związanych z danym kluczem w słownikach oryginalnych (2p)

slow1 = {i:randint(1,99) for i in range(0,10)}
print(slow1)
slow1 = {v:k for k,v in slow1.items()} 
print(slow1)

slow2 = {i:randint(1,99) for i in range(0,10)}
print(slow2)
slow2 = {v:k for k,v in slow2.items()} 
print(slow2)





