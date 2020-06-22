import sys
sys.path.append('build/lib.linux-x86_64-3.7')

import mod
from random import randint
import time

def Sortowanie_babelkowe(tab, n):
	for i in range(n):
		for j in range(n-1):
			if tab[j] > tab[j + 1]:
				tab[j],tab[j + 1] = tab[j + 1],tab[j]

rozmiary = [10, 10**2, 10**3, 10**4]
tab1_czasy = []
tab2_czasy = []
for rozm in rozmiary:
	tab1 = [randint(0,rozm) for _ in range(rozm)]
	tab2 = [elem for elem in tab1]
	t1_start = time.time()
	Sortowanie_babelkowe(tab1,rozm)
	t1_finish = time.time()
	tab1_czasy.append(t1_finish-t1_start)
	t2_start = time.time()
	mod.met(tab1)
	t2_finish = time.time()
	tab2_czasy.append(t2_finish-t2_start)
	
print("czasy PY: ", tab1_czasy)
print("czasy C: ", tab2_czasy)