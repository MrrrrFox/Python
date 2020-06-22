#!/usr/bin/env python3.7
from random import randint
from random import random

# 1. Proszę utworzyć funkcję przyjmującą jeden parametr i zwracającą słownik. Liczba elementów w słowniku jest wartością losową z przedziału [0,20). Kluczami są wartości rzeczywiste z przedziału [0, 1), a wartościami są wartości wyrażenia matematycznego z jedną zmienną przekazanego jako parametr wywołania funkcji obliczone dla danego klucza. Wartości w słowniku mają być zaokrąglone do trzeciego miejsca po przecinku i zapisane z taką dokładnością jako ciągi znaków (1p)
print('ZAD 1 ------------------------------------------------------')
def fun1(todo):
	slownik = {}
	ile = randint(0,19)
	while len(slownik) < ile:
		x = random()
		if x not in slownik:
			slownik.setdefault(x, "{0:.3f}".format(eval(todo.format(x))))
	return slownik

print(fun1('2*x+4'))
print(fun1('8*{}+1'))

# 2. Proszę napisać funkcję, do której można przekazać dowolną liczbę list i krotek a zwracającą listę zawierającą elementy wspólne dla wszystkich parametrów. Proszę użyć konstrukcji for-else (1p)
print('ZAD 2 ------------------------------------------------------')
def fun2(*param):
	list = []
	for i in param[0]:
		for j in range(1,len(param)):
			if i not in param[j]:
				break;
		else:
			list.append(i)
	return list

print(fun2([1,2,3], (1,4,2,5), [11,2,1]))
	
# 3. Proszę napisać funkcję przyjmującą dwie sekwencje i parametr z wartością domyślną True. Funkcja zwraca listę zawierającą dwuelementowe krotki zawierające elementy o jednakowych indeksach z obu sekwencji. Jeżeli wartość trzeciego parametru wynosi True, długość zwracanej listy równa jest długości krótszej z przekazanych sekwencji, w przeciwnym wypadku brakujące wartości uzupełniamy wartością None. Budowanie każdej z wynikowych list jedna linijka! (2p)
print('ZAD 3 ------------------------------------------------------')
def mergeSeq(seq1, seq2, krotsza = True):
	sizem = min(len(seq1),len(seq2))
	sizeM = max(len(seq1),len(seq2))
	if krotsza == True:
		return [(seq1[i],seq2[i]) for i in range(sizem)] 
	else:
		return [(seq1[i],seq2[i]) if i<sizem else (None,seq2[i]) for i in range(sizeM)] if len(seq1)<len(seq2) else [(seq1[i],seq2[i]) if i<sizem else (seq1[i],None) for i in range(sizeM)]

seq1 = [1,2,3,4,7,8,9,0]
seq2 = [19,3,14,2, 5]
print(mergeSeq(seq1,seq2))
print(mergeSeq(seq1,seq2, False))

# 4. Proszę napisać funkcję przyjmującą zmienną liczbę argumentów, która będzie zwracała najmniejszą/największą wartość. Następnie proszę napisać funkcję, przyjmującą jako parametry funkcję oraz zmienną liczba parametrów pozycyjnych. W wywołaniu proszę przekazać funkcję szukającą min/max oraz listę. (2p)
print('ZAD 4 ------------------------------------------------------')
def max(*a):
	if len(a)>0:
		najw = a[0]
		for i in range(len(a)):
			if najw<a[i]:
				najw = a[i]
		return najw
	print('brak argumentow!')
	return False

print(max(1,2,3))
print(max(87,12))
print(max())

def fun4(anotherFun, *arguments):
	return anotherFun(*arguments)

arg1 = [1,2,3]
arg2 = [87,12]
arg3 = []

print(fun4(max, *arg1))
print(fun4(max, *arg2))
print(fun4(max, *arg3))

# 5. Proszę napisać funkcję umożliwiającą rozmienienie kwoty pieniędzy przekazanej jako jej pierwszy parametr nominałami określonymi poprzez drugi parametr - wartość domyślna krotka (10,5,2) (algorytm zachłanny). Proszę sprawdzić działanie funkcji przekazując inny zestaw monet. (2p)
print('ZAD 5 ------------------------------------------------------')
def zachl_rozm(kwota, nomin=(10,5,2)):
	tab = [0]*len(nomin)
	i = 0
	while i<len(nomin):
		if(nomin[i] <= kwota):
			kwota = kwota - nomin[i]
			tab[i] = tab[i] + 1
		else:
			i = i + 1
	slownik = {}
	for i in range(len(nomin)):
		slownik.setdefault(nomin[i],tab[i])
	if kwota == 0:
		slownik.setdefault('r',0)
		return slownik
	else:
		slownik.setdefault('r',kwota)
		print('kwoty nie da sie rozmienic podanym zestawem nominalow')
		return slownik

print(zachl_rozm(12))
print(zachl_rozm(17))
print(zachl_rozm(22))
print(zachl_rozm(11))
print(zachl_rozm(11, (10,5,2,1)))
print(zachl_rozm(104, (17,8,3)))
print(zachl_rozm(109, (17,5,2)))

# 6. Proszę napisać funkcję przyjmującą cztery parametry: liczba, której wartość zgadujemy, granice przedziału, w którym szukana liczba się mieści i ostatni określający sposób poszukiwania wartości z wartością domyślną 'r'. Przy wartości domyślnej ostatniego parametru, liczby poszukujemy losując kolejną wartość, w innym przypadku poszukujemy wartości poprzez podział przedziału poszukiwania wartości na pół. W obu przypadkach w każdym kroku odpowiednio zawężamy przedział poszukiwania (proszę wykorzystać operator trójargumentowy). Proszę sprawdzić ile kroków jest potrzebnych do znalezienia szukanej wartości w zależności od metody. (2p)
print('ZAD 6 ------------------------------------------------------')
def fun6(liczba, poczatek, koniec, tryb = 'r'):
	ileProb = 0
	while True:
		ileProb = ileProb+1
		i = randint(poczatek,koniec) if tryb == 'r' else (poczatek+koniec)//2
		print('proba nr', ileProb, '- wylosowano liczbe ', i)
		if i == liczba:
			print('znaleziona za',ileProb,'razem w trybie', tryb)
			return ileProb
		else:
			poczatek = poczatek if i>liczba else i
			koniec = koniec if i<liczba else i
	

print(fun6(20,0,100))
print(fun6(20,0,100,'d'))