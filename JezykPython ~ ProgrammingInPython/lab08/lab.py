import module1

###################################################################################
# 1.funkcję dokonującą przekształcenia punktu na płaszczyźnie wg wzorów (ifs):
#  x(t+1)=a*x(t)+b*y(t)+c
#  y(t+1)=d*x(t)+e*y(t)+f
# Przykładowy zestaw współczynników (a,b,c,d,e,f):
# ((0,0,0,0,0.16,0), (0.2,-0.26,0,0.23,0.22,1.6), (-0.15,0.28,0,0.26,0.24,0.44), (0.85,0.04,0,-0.04,0.85,1.6))
#Przy kolejnych przekształceniach określoną szóstkę współczynników wybieramy odpowiednio z prawdopodobieństwem: (1%, 7%, 7%, 85%),
# proszę użyć random.choices. Wynik proszę narysować, powinna wyjść paprotka (4p)
print('##############################ZAD_1##############################')

module1.fun1(10000)

###################################################################################
# 2.funkcję obliczającą wartość całki z zadaną dokładnością, np.  10−6 metodą Monte Carlo. Proszę sprawdzić ile trafień
#jest koniecznych do uzyskania wyniku (jako wartości dokładnej proszę użyć wartości zwracanej przez funkcję scipy.integrate.quad) (4p)

#Losujemy n punktów znajdujących się w obrębie prostokąta ograniczającego funkcję w granicach całkowania.
#Wprowadzamy zmienną pomocniczą t, którą modyfikować będziemy następująco:
# -> jeżeli wylosowany punkt (xi, yi) leży nad osią OY i jednocześnie pod wykresem funkcji całkowanej,
#czyli spełnia nierówność: 0 < yi ≤ f(xi), wówczas zwiększamy zmienną t o jeden,
# -> jeżeli wylosowany punkt (xi, yi) leży pod osią OY i jednocześnie nad wykresem funkcji całkowanej,
#czyli spełnia nierówność: 0 > yi ≥ f(xi), wówczas zmniejszamy zmienną t o jeden,
# -> jeżeli wylosowany punkt (xi, yi) nie spełnia żadnego z powyższych warunków, wówczas pozostawiamy zmienną t bez zmian.
#Całkę obliczamy jako Pprostokąta t/n
print('##############################ZAD_2##############################')

funkcja = lambda x : -x**2 + 2

module1.fun2(funkcja, -2, 2)

###################################################################################
# 3.funkcję obliczającą wartość całki z zadaną dokładnością, np.  10−6 metodą Monte Carlo.
#Proszę sprawdzić ile trafień jest koniecznych do uzyskania wyniku.
#Całkę obliczamy jako iloczyn średniej wartości funkcji w punktach losowych wewnątrz przedziału całkowania oraz szerokości przedziału (2p)
print('##############################ZAD_3##############################')

funkcja2 = lambda x : x**3 - 1

module1.fun3(funkcja2, -3,4)