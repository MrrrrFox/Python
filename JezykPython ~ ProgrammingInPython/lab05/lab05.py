#!/usr/bin/env python3.7
from random import randint
from random import random
from math import sqrt
from functools import reduce


###################################################################################
# 1. Proszę napisać program testujący alternatywne sposoby budowania zestawu wartości: pętla for, lista składana, funkcja map i wyrażenie generatorowe (składnia taka jak listy składanej tylko w miejsce nawiasów kwadratowych należy wstawić okrągłe; o generatorach będziemy mówić na kolejnych zajęciach). Dla każdego ze sposobów proszę utworzyć osobną funkcję tak, aby uzupełnić poniższy kod:
print('##############################ZAD_1##############################')
from time import time_ns
from sys import version 

powt=1000 
N=10000

def tester(_func):
	time = time_ns()
	for _ in range(powt):
		_func()		# przy tescie sumy tutaj ma byc petla for sumujaca lub sum(_func())
	time = time - time_ns()
	return abs(time)
	
def forStatement():
	forList = []
	for i in range(N):
		forList.append(i)		# przy kwadracie i**2
	return forList
	
def listComprehension():
	return [ i for i in range(N) ]		# przy kwadracie i**2

def mapFunction():
	return list(map(lambda x:x,range(N)))	# przy kwadracie x**2, a przed testem5 bez rzutowania

def generatorExpression():
	return list((i for i in range(N)))	# przy kwadracie i**2, a przed testem5 bez rzutowania

print(version)
test=(forStatement, listComprehension, mapFunction, generatorExpression)
for testFunction in test:
	print(testFunction.__name__.ljust(20), '=>', tester(testFunction))

"""
gdzie: tester - funkcja wywołująca powt razy daną funkcję, w której tworzonych jest N wartości.

Proszę wykonać testy:
dodawanie elementu
dodawanie elementu podniesionego do kwadratu
sumowanie elementów z wykorzystaniem pętli for
sumowanie z wykorzystaniem funkcji sum
konwersja obiektu map i generatora do listy

Do pomiaru czasu proszę użyć funkcji time_ns z modułu time. Otrzymane wyniki proszę dołączyć do wysyłanego programu (2p)

"""

###################################################################################
# 2. Proszę napisać funkcję obliczającą wartość całki metodą prostokątów korzystając z funkcji map (funkcja podcałkowa, granice całkowania oraz liczba kroków jako parametry wywołania funkcji) (2p)
print('##############################ZAD_2##############################')
underFun = lambda x: x**2

def fun2(todo, a, b, N):
	dx = (b-a)/(N-1)
	#print(dx)
	xi = [a+i*dx for i in range(N)]
	#print(xi)
	yi = list(map(todo, xi))
	#print(yi)
	S = dx*sum(yi)
	#print(S)
	return S

wynik = fun2(underFun,-1,3,1000)
print(wynik)


###################################################################################
# 3. Proszę wyznaczyć wartość liczby pi metodą Monte-Carlo korzystając z funkcji filter (2p)
# Koło o promieniu 1 wpisujemy w kwadrat o boku 2 i umieszczamy ich środki w początku układu współrzędnych. Stosunek pól tych figur jest równy stosunkowi liczby trafień w ich obszar, przy losowaniu dużej liczby punktów wewnątrz kwadratu (przyda się funkcja random.uniform).
print('##############################ZAD_3##############################')
list2 = []
N = 100000
for _ in range(N):
	x = 2*random()
	y = 2*random()
	list2.append(sqrt((1-x)**2 + (1-y)**2))

Pi = 4 * len(list(filter(lambda x:x<1, list2))) / N
print(Pi)


###################################################################################
# 4. Proszę znaleźć:
# -> największą wartość w każdym wierszu macierzy (map),
# -> największą wartość w każdej kolumnie macierzy (map+zip),
# -> sumę dwóch macierzy (map+zip+lista składana).
#Każde polecenie jedna linijka (2p)
print('##############################ZAD_4##############################')
# tworzenie dwoch macierzy MxN
M=5
N=4 
matrix1 = [ [] for _ in range(M) ]
matrix2 = [ [] for _ in range(M) ]

for i in range(M):
	for j in range(N):
		matrix1[i].append(randint(0,20))
		matrix2[i].append(randint(0,20))
print(matrix1, '\n\n', matrix2, '\n')

# max z wierszy 
ad1 = list(map(lambda x: max(x), matrix1))
print('ad1	', ad1)

# max z kolumn
ad2 =list(map(lambda x: max(x), zip(*matrix1)))
print('ad2	', ad2)

# suma macierzy
ad3 = [list(map(sum, zip(*a))) for a in zip(matrix1,matrix2)]
print('ad3	', ad3)


###################################################################################
# 5. Proszę napisać funkcję przyjmującą dwa parametry - lista x-ów i y-ów. Korzystając z funkcji reduce i map proszę obliczyć (i zwrócić z funkcji) wartości dofitowanych współczynników prostej oraz ich niepewności (potrzebne wzory w pliku) (2p)
print('##############################ZAD_5##############################')
N = 3
randRange = 5
x = [randint(0,randRange) for _ in range(N)]
y = [randint(0,randRange) for _ in range(N)]
print(x)
print(y)

def fun5(xList, yList):
	x_sr = reduce((lambda x,y:x+y), xList)/N
	y_sr = reduce((lambda x,y:x+y), yList)/N
	print('x_sr = ',x_sr, ';		y_sr=', y_sr)
	D = reduce(lambda x,y:x+y,list(map(lambda x: (x-x_sr)**2,xList)))
	print('D = ',D)
	a = reduce(lambda x,y:x+y,list(map(lambda x,y:y*(x-x_sr), xList, yList)))/D
	print('a = ',a)
	b = y_sr - a * x_sr
	print('b = ',b)
	d_y = sqrt( reduce((lambda x,y: x+y), list(map(lambda x,y: (y-(a*x+b))**2, xList, yList ))) / (N-2) )
	print('d_y = ',d_y)
	d_a = d_y / sqrt(D)
	print('d_a = ',d_a)
	d_b = d_y * sqrt(1/N + (x_sr**2)/D)
	print('d_b = ',d_b)
	return a,b,d_a,d_b

a,b,d_a,d_b = fun5(x,y)
