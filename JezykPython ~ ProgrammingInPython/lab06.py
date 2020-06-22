#!/usr/bin/env python3.7

from math import sin
from math import factorial
from random import randint

###################################################################################
# 1.Proszę napisać trzy funkcje generatorowe:
# -> zwracającą kolejne elementy ciągu Fibonacciego (generator nieskończony),
# -> zwracającą te wartości z przekazanej jako parametr sekwencji, które są parzyste/nieparzyste
# -> zwracającą wartości z przekazanej jako pierwszy parametr sekwencji 
# 	i przerywającą działanie po napotkaniu wartości większej niż drugi parametr przekazany do funkcji
#Korzystając ze zdefiniowanych funkcji proszę obliczyć sumę parzystych/nieparzystych elementów ciągu Fibonacciego mniejszych od 100 (2p)
print('##############################ZAD_1##############################')

def gen_11():
	a = 0
	yield a
	b = 1
	yield b
	while True:
		yield a+b
		a,b = b,a+b

def gen_12(seq, tryb='np'):	# np - nieparzyste, p - parzyste
	for i in seq:
		if tryb=='np':
			if i%2==1:
				yield i
		else:
			if i%2==0:
				yield i

def gen_13(seq,max):
	for i in seq:
		if i>max:
			break
		yield i

print( 'suma parzystych: ', sum(gen_13(gen_12(gen_11(),'p'), 100)) )
print( 'suma nieparzystych: ', sum(gen_13(gen_12(gen_11(),'np'), 100)) )

###################################################################################
# 2.Proszę napisać generator działający dokładnie tak samo jak wbudowany range (proszę się upewnić, że wiecie Państwo jak on działa!), 
# ale pozwalający na generowanie liczb rzeczywistych (2p)
#Do testów: range(10), range(-10), range(1,10), range(10,1), range(1,10,2), range(1,10,-2), range(10,1,2), range(10,1,-2)
print('##############################ZAD_2##############################')

def gen_2(start, koniec=None, krok=None):
	if koniec==None and krok==None:
		koniec = float(start)
		start = 0.
	if krok==None:
		krok = 1.
	if krok>0 and start>=koniec:
		return
	elif krok<0 and start<=koniec:
		return
	if start<koniec:
		while(start<koniec):
			yield float(start)
			start = start + krok
	else:
		while(start>koniec):
			yield float(start)
			start = start + krok

# TESTY I POROWNANIE
for i in range(10,1,-2):
	print(i)
for i in gen_2(10,1,-2):
	print(i)

###################################################################################
# 3. Proszę napisać generator zwracający kolejne wiersze trójkąta Pascala wraz z sumą ich wartości (2p)
print('##############################ZAD_3##############################')

def gen_3():
	num = 0
	yield [num,1, [1]]	# numer wiersza, suma wiersza, elementy wiersza
	dlugosc = 2
	while True:
		num = num+1
		now = []
		for i in range(dlugosc):
			if i == 0 or i == dlugosc-1:
				now.append(1)
			else:
				now.append(prev[i-1]+prev[i])
		prev = now
		dlugosc=dlugosc+1
		yield [num,sum(now), now]		# numer wiersza, suma wiersza, elementy wiersza

wynik = gen_3()
for i in range(10):
	print(next(wynik))

###################################################################################
# 4. Proszę napisać generator zwracający przybliżenie funkcji sinus, gdzie kolejny wyraz wynosi: ((-1)k/(1+2k)!)x(1+2k) (math.factorial)
# Proszę sprawdzić ile wyrazów ciągu jest koniecznych do uzyskania zadanej dokładności, np. 10-8 (2p)
print('##############################ZAD_4##############################')

def gen_4(x):
	k=0
	eps = 10**(-8)
	wynik = (-1)**k * x**(1+2*k) / factorial(1+2*k)
	while sin(x)+eps < wynik or wynik < sin(x)-eps:
		yield wynik, sin(x)
		k=k+1
		wynik = wynik + (-1)**k * x**(1+2*k) / factorial(1+2*k)

iterator = 1
for a,b in gen_4(1):
	print(iterator, f'przyblizenie ~ {a:.8}','\t',f'sin(x) = {b:.8}')
	iterator = iterator + 1

###################################################################################
# 5.Proszę wygenerować losowy ciąg zer i jedynek o długości N. 
# Proszę napisać generator zwracający liczbę zer oddzielających kolejne jedynki w sekwencji przekazanej jako parametr. 
# Korzystając z utworzonego generatora proszę obliczyć średnią odległość między kolejnymi jedynkami w wygenerowanym wcześniej ciągu (2p)
print('##############################ZAD_5##############################')

N = 10**6
list = [randint(0,1) for _ in range(N)]
#print(list)

def gen_5(seq):
	ilosc = 0
	pierwsze_1 = 0
	for i in seq:
		if i == 1 and pierwsze_1 == 0:
			pierwsze_1 = 1
			ilosc = 0
		elif i==1:
			yield ilosc
			ilosc = 0
		else:
			ilosc = ilosc + 1

licznik = 0
mianownik = 0
for i in gen_5(list):
	#print(i)
	licznik = licznik + i
	mianownik = mianownik + 1
print('srednia odleglosc miedzy kolejnymi jedynkami: ', f'{licznik/mianownik:.2}')
