#!/usr/bin/env python3.7

import numpy as np 
import glob

###################################################################################
# 1.Proszę napisać funkcję, która pozwoli na wypisanie: 
# n początkowych wierszy pliku, 
# n końcowych wierszy pliku, 
# co n-tego wiersza pliku, 
# n-tego słowa ze wszystkich wierszy 
# n-tego znaku ze wszystkich wierszy. 
# Nazwę pliku oraz n przekazujemy jako parametr do funkcji. Każdy podpunkt==jedna linia kodu (1.5p)
print('##############################ZAD_1##############################')

def func1(nazwa,n):
	with open(nazwa) as zad1:
		linie = zad1.readlines()
		print('1')
		for i in range(n): print(linie[i])
		print('2')
		for i in range(len(linie)-n,len(linie)): print(linie[i])
		print('3')
		for i in range(0,len(linie),n): print(linie[i])		
		print('4')
		for i in range(len(linie)): print(linie[i].split()[n-1])
		print('5')
		for i in range(len(linie)): print(linie[i][n-1])

# uzyłem na szybko wypelnionego pliku do testow - dodalem go do archiwum
func1('zad7_1.txt',4)

###################################################################################
# 2. Wszystkie pliki z rozszerzeniem in w katalogu bieżącym traktujemy jako wyniki kolejnych serii pomiarów tych samych wielkości. 
# Zakładamy, że w każdym z plików mamy dwie kolumny liczb (x, y). Na wyjściu chcemy otrzymać jeden plik z trzema kolumnami:
# x pierwsza kolumna z dowolnego z plików wejściowych,
# średnia y z danego wiersza ze wszystkich plików (numpy.average),
# odchylenie standardowe y z danego wiersza ze wszystkich plików (numpy.std)
# (2p)
# PLIKI TESTOWE: pliki.zip
print('##############################ZAD_2##############################')

list = [[] for _ in range(7)] # tu bede dawal y-ki i jedne x-sy
counter = -1

for f in glob.glob("pliki/*.in"):
	counter = counter + 1
	file = open(f)
	
	data = file.read()
	data = data.split()
	# dodanie x-ow
	if counter == 0:
		for i in range(0,len(data),2):
			list[6].append(data[i])
	# dodanie y-ow
	for i in range(1,len(data), 2):
		list[counter].append(data[i])
	file.close()		

# pomysl moim zdaniem jest dobry, ale listy okazuja sie byc puste (sposob niepoprawny)
print(list)

###################################################################################
# 3. Proszę napisać funkcję, tworzącą plik z instrukcjami pozwalającymi na wygenerowanie wykresu plików j.w. + wynikowego 
# (łącznie z odchyleniem standardowym)*patrz niżej, proszę skorzystać z potrójnego cudzysłowu (1.5p)
print('##############################ZAD_3##############################')


###################################################################################
# 4. Proszę sporządzić histogram słów rozpoczynających się na daną literę alfabetu ze wszystkich plików pasujących do określonego wzorca 
# w katalogu bieżącym, opcje wyświetlenia: sortowanie alfabetyczne bądź po liczbie słów (2.5p)
# PLIKI TESTOWE: zad4A.in, zad4B.in
print('##############################ZAD_4##############################')


###################################################################################
# 5. Proszę napisać funkcję, która odczytuje plik i 
# dla wszystkich znajdujących się w nim wartości liczbowych znajduje sumę ich cyfr i wynik zapisuje w innym pliku w postaci: 123->1+2+3=6, 
# a dla wartości tekstowych znajduje liczbę samogłosek i liczbę spółgłosek i wynik zapisuje jako: ala=2+1 (2.5p)
# PLIK TESTOWY: zad5.in
print('##############################ZAD_5##############################')

def func2(plik):
	with open('output.txt', 'w') as out:
		text = plik.read()
		for element in text.split():
			if element.isnumeric():
				eq = ''
				suma = 0
				for a in element:
					eq = eq + a
					eq = eq + '+'
					suma = suma + int(a)
				eq = element+'->'+eq[:-1]+'='+str(suma)
				out.write(eq+'\n')
			if element.isalpha():
				samo = 0
				spol = 0
				samostr = 'AEIOUYaeiouy'
				for a in element:
					if a in samostr:
						samo = samo + 1
					else:
						spol = spol + 1
				eq = element+'='+str(samo)+'+'+str(spol)
				out.write(eq+'\n')

with open('zad5.in') as zad5:
	func2(zad5)
print('ZAPISANO DO PLIKU')