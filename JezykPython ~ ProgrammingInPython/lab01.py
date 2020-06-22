#!/usr/bin/env python3.7
import math
from math import sqrt
from cmath import sqrt as csqrt
from sys import argv

print('Hello!')

a=3
print(type(a))
a='7'
print(type(a))
a=2.5
print(type(a))
a=True
print(type(a))

a,*b=2,3,4,5.,'a'	# a=2, b - lista pozostalych argumentow
print(a, type(a))
print(type(b))

print(a,'		',b)
a,b = b,a			# swap
print(a,'		',b)

print(1//2,'		', 1/2)		# dzielenie calkowitoliczbowe (wymuszone) i normalne

k = (1,2,'a')	#krotka - niemodyfikowalne listy, indeksowane od 0
print('dlugosc krotki "k" to ',len(k))
# k[1] = 'x'		# blad, bo jest niemodyfikowalne

k = (1)			# nie krotka, tylko int
k = (1,)		# jednoelemtowa krotka
print(k);

k = [1,2,'a']	# lista o elementach roznych typow (nie tablica!)
print(k)
k[1] = 3		# jak najbardziej modyfikowalna
print(k)

k = ([1,2,'a'], 1, ('c',))
#k[0] = 3
print(k)
k[0][1] = 3
print(k)

k1 = k		# mamy plytka kopie
print(id(k), id(k1))	# identyfikator zmiennej
print('k1 ',k1)
#k1[0] = (3,)
print('k = ', k,', k1 = ', k1)

k = [1,2,3,4,5,6,7,8,9]
k1 = k[2:5]			# krobimy kopie niezalezna, k1 ma 3 elementy, zakres od 2 do 5 bez KONCA, czyli bez k[5]
print(k,'		',k1)
k1 = k[2:7:2]		# trzeci argument to krok, krok = 2
print(k,'		',k1)
k1 = k[:]		# kopia calej listy
print(k,'		',k1)
k1[0] = 3		# modyfikujemy konkretny element listy
print(k,'		',k1)

import copy

k1 = copy.deepcopy(k)	# gleboka kopia
print(k,'		',k1)	
k1 = k[::-1]			# kopia od typu
print(k,'		',k1)	

k = [0]*100		# lista 100-elementowa, gdzie kazdy element jest rowny 0
print(k)
k[5] = 1
print(k)
k = [[]]*100		# pusta lista list, ale modyfikacja jednej modyfikuje wszystkie
k[7].append(7)		# append() - dodanie czegos do listy
print(k)

k = [ [] for _ in range(100)] # lista skladana, najpierw co dodajemy ([]) potem petla z licznikiem dowolnym (np "_") i potem zakres od 0 do 99 z krokiem 1. czyli w kazdej iteracji dodajemy obiekt [] do listy list
k[7].append(7)
print(k)

k = []
k.append([1,2,3])	# dodajemy do listy na koniec 
print(k)
k.extend([1,2,3])	# rozszerzamy liste na koncu
print(k)

print(3 in k)		# czy 3 jest w k?
print(3 not in k)	# czy 3 nie jest w k?

# INSTRUKCJE STERUJACE - if, for, while
#-------------------------------------------------------------------- if
a = 1 if True else 0	# a rowna sie 1 jezeli cos i rowna sie 0 w przeciwnym wypadku
print(a)

print(-1<a<2)		# nie trzeba uzywac and
print(2<a<5)

print(argv, type(argv))

if len(argv) == 4:
	# rozwiazywanie rownanie kwadratowego
	#a = int(input('podaj a '))	# input uzytownika, rzutowanie na int, argumentem jest wyswietlany komunikat
	#b = int(input('podaj b '))
	#c = int(input('podaj c '))
	a = int(argv[1])
	b = int(argv[2])
	c = int(argv[3])
	eps = 0.0001
	delta = b**2 - 4*a*c
	if delta > 0:
		print('x_1 = ', (sqrt(delta) - b) / ( 2*a) , ', x_2 = ', -(sqrt(delta) - b) / 2*a )
	elif 0 - eps < delta < 0 + eps:
		print('x = ', (sqrt(delta) - b) / (2*a), ', krotnosc 2' )
	else:
		print('brak rozw w R')	# a.imag, a.re z biblioteki cmath

#-------------------------------------------------------------------- for
k = [1,2,3,4,5,6]
print(k)
for i in k:
	i+=1;
print(k)	#nic sie nie zmienia

for i in range(len(k)):	# range: 1 paramater=koniec przedzialu, domyslny poczatek=0 i krok=1, 2 parametry=poczatek i koniec z krokiem=1, 3 parametry=poczatek,koniec i skok
	k[i]+=1		# teraz juz modyfikujemy liste
print(k)

for i in range(len(k)):
	if k[i]>40:	# dla "4" nie wchodzimy do else ponizej
		break
else:		# else do for (lub while), wchodzimy do niego wtedy gdy przejdziemy cala petle
	print('...')

k=[(1,2), (3,4), (5,6)]
for i,j in k:	# k jest regularne, wiec rozpakowujemy krotki do konkretnych zmiennych
		
