#!/usr/bin/env python3.7
from sys import argv

#print(dir(""))

# X.join(seq) - laczy sekwencje za pomoca pocznika X

# f'a = {a:.3}' - wypisanie wartosci a do 3 miejsc po przecinku
# f'{a=}'

# sortowanie listy
#l.sort() - sortowanie w miejscu w porzadku naturalnym, l=l.sort() zadziala, ale bez sensu bo l nie jest juz lista

# key = lambda x:x[3] - sortujemy liste w oparciu o 4 element listy krotek

# sum(seq) - przyjmuje sekwencje, zwraca ich sume


# ponizsze zadania z http://home.agh.edu.pl/~gos

    #Proszę utworzyć string składający się z elementów listy argv z wyłączeniem nazwy programu. Jeżeli program został uruchomiony bez podania parametrów proszę wypisać na ekran komunikat informujący o właściwym sposobie uruchomienia programu (1p)

string1 = ''
if len(argv) == 1:
	print("Program sklada string z elementow listy argv z wylaczeniem nazwy programu")
else:
	string1 = ''.join(argv[1:])
	print(string1)

    #Na podstawie wcześniej utworzonego stringa proszę utworzyć cztery listy: zawierającą małe litery, zawierającą duże litery, zawierającą cyfry oraz zawierającą wszystko co nie jest literą (2p)

lists = [ [] for _ in range(4)]
lists[0].extend([i for i in string1 if i.islower()])
lists[1].extend([i for i in string1 if i.isupper()])
lists[2].extend([i for i in string1 if i.isdigit()])
lists[3].extend([i for i in string1 if i.isascii() and not i.isalnum()])
print(lists)

    #Na podstawie utworzonej listy zawierającej małe litery proszę utworzyć listę małych liter bez powtórzeń. Następnie proszę utworzyć nową listę, w której każdy element jest dwuelementową krotką (litera, krotność jej wystąpienia w liście oryginalnej) (2p)

smallList = []
for i in lists[0]:
	if i not in smallList:
		smallList.append(i)
print(smallList)

krotki = [(i, lists[0].count(i)) for i in smallList]
print(krotki)

    #Otrzymaną w powyższym punkcie listę proszę posortować względem krotności (1p)

krotki.sort(key = lambda x:x[1])
print(krotki)

    #Proszę utworzyć listę dwuelementowych krotek, w których pierwszy element jest liczbą pobraną z listy cyfr, drugi natomiast wartością funkcji liniowej ax+b dla danej liczby; wartości współczynników proszę ustalić w następujący sposób: a równa się liczbie samogłosek w stringu z punktu pierwszego, a b - liczbie spółgłosek tamże (2p)

samo = string1.count('a') + string1.count('e') + string1.count('i') + string1.count('o') + string1.count('u') + string1.count('y') + string1.count('A') + string1.count('E') + string1.count('I') + string1.count('O') + string1.count('U') + string1.count('Y')
spol = len(lists[0]) + len(lists[1]) - samo

#samogloski = 'aeiouyAEIOUY'
#samo = sum[string1.count(i) for i in samogloski]

print('ilosc samoglosek:', samo)
print('ilosc spolglosek:', spol)

nowekrotki = [(int(i), samo * int(i) + spol) for i in lists[2]]
print(nowekrotki)

    #Proszę obliczyć wartości parametrów prostej korzystając z metody najmniejszych kwadratów (2p):
    #a=(1/D)Σyi(xi-x);
    #D=Σ(xi-x)2;
    #b=y-ax

x_sr = sum( i for i,_ in nowekrotki) / len(nowekrotki)
print('x sredni =',x_sr)
y_sr = sum( i for _,i in nowekrotki) / len(nowekrotki)
print('y sredni =',y_sr)

D = sum( (i-x_sr)**2 for i,_ in nowekrotki)
print('D =',D)

a = 1/D * sum(j*(i-x_sr) for i,j in nowekrotki)
print('a =',a)

b = y_sr - a*x_sr
print('b =',b)
