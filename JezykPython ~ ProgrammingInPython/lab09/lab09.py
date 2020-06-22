
from random import randint

###################################################################################
# 1.Proszę napisać funkcję przyjmującą trzy parametry. Na początku należy sprawdzić czy wszystkie parametry są
# liczbami większymi od zera oraz czy pierwszy jest mniejszy od drugiego, jeżeli coś nie jest prawdą zgłaszamy wyjątek.
# Jeżeli wszystko jest OK losujemy tyle liczb całkowitych (z przedziału domkniętego określonego przez dwa
# pierwsze parametry) jaka jest wartość trzeciego parametru przekazanego do funkcji i zliczamy liczbę wylosowanych
# wartości parzystych i nieparzystych. Z funkcji zwracamy wartość ilorazu parzyste/nieparzyste o ile jest to możliwe,
# jeśli nie zgłaszamy wyjątek (2p).
print('##############################ZAD_1##############################')

def fun1(first, second, third):
    try:
        if not (0<first<second and 0<third):
            raise
    except:
        print("Argumenty", first, second, third,"nie spelniaja zalozen.")
    else:
            list = [randint(first,second) for _ in range(third)]
            print(list)
            parz = 0
            nparz = 0
            for elem in list:
                if elem%2==0:
                    parz = parz + 1
            nparz = len(list)-parz
            print("liczba parzystych: ", parz, "\tliczba nieparzystych: ", nparz)
            try:
                iloraz = parz/nparz
            except:
                print("Nie ma liczb nieparzystych. (dzielenie przez 0)")
            else:
               return iloraz


result = fun1(2,3,3)
print(result)

###################################################################################
# 2.Proszę napisać funkcję obliczającą średnią arytmetyczną wartości z dwóch pierwszych kolumn w pliku.
# Jeżeli liczba linii w pliku wynosi zero, jeśli któryś wiersz nie zawiera co najmniej dwóch kolumn lub
# gdy plik nie zawiera danych liczbowych funkcja zgłasza wyjątek. Jeżeli udało się obliczyć średnią wynik
# należy zapisać w pliku (wspólny plik dla wszystkich wywołań funkcji) w postaci:
# nazwa pliku: średnia
# Funkcję należy wywołać dla wszystkich plików z rozszerzeniem dat z katalogu bieżącego
# (przed otwarciem proszę sprawdzać czy plik ma odpowiedni atrybut -> os.access).
# Proszę zapewnić zamknięcie pliku niezależnie od pojawienia się wyjątku! (2.5p)
# Pliki testowe: pliki_dat.zip
print('##############################ZAD_2##############################')

###################################################################################
# 3.Proszę napisać funkcję sprawdzającą czy elementy listy tworzą trójkę (a^2+b^2=c^2)/czwórkę(a^2+b^2+c^2=d^2)
# pitagorejską (funkcja ma działać dla dowolnej długości "podciągu"!). Proszę zgłosić wyjątek w przypadku
# niepoprawnej długości listy oraz w przypadku, gdy lista nie zawiera żadnych trójek/czwórek pitagorejskich.
# Dla każdej trójki/czwórki proszę sprawdzić ile jest w niej wartości parzystych i nieparzystych (3p).
# Listy testowe:
# l=(1,2,2,3,2,3,6,7,1,4,8,9,4,4,7,9,2,6,9,13,6,6,7,11,3,4,12,13,2,5,14,15,2,10,11,15,1,12,12,17,8,9,12,17,1,6,18,19,6,6,17,19,6,10,15,21,4,5,20,21,4,8,19,21,4,13,16,21,8,11,16,21,3,6,22,23,3,13,18,23,6,13,18,23,9,14,20,25,12,15,16,25,2,7,26,27,2,10,25,27,2,14,23,27,7,14,22,27,10,10,23,27,3,16,24,29,11,12,24,29,12,16,21,29,2)
# l=(1,2,2,3,2,3,6,7,1,4,8,9,4,4,7,9,2,6,9,13,6,6,7,11,3,4,12,13,2,5,14,15,2,10,11,15,1,12,12,17,8,9,12,17,1,6,18,19,6,6,17,19,6,10,15,21,4,5,20,21,4,8,19,21,4,13,16,21,8,11,16,21,3,6,22,23,3,13,18,23,6,13,18,23,9,14,20,25,12,15,16,25,2,7,26,27,2,10,25,27,2,14,23,27,7,14,22,27,10,10,23,27,3,16,24,29,11,12,24,29,12,16,21,29)
# l=(3,4,5,5,12,13,7,24,25,9,40,41,6,8,10,60,80,100,18,24,30,15,8,17)
# l=(1,2,3,4,5,6,7,8,9)
print('##############################ZAD_3##############################')

l1=(1,2,2,3,2,3,6,7,1,4,8,9,4,4,7,9,2,6,9,13,6,6,7,11,3,4,12,13,2,5,14,15,2,10,11,15,1,12,12,17,8,9,12,17,1,6,18,19,6,6,17,19,6,10,15,21,4,5,20,21,4,8,19,21,4,13,16,21,8,11,16,21,3,6,22,23,3,13,18,23,6,13,18,23,9,14,20,25,12,15,16,25,2,7,26,27,2,10,25,27,2,14,23,27,7,14,22,27,10,10,23,27,3,16,24,29,11,12,24,29,12,16,21,29,2)
l2=(1,2,2,3,2,3,6,7,1,4,8,9,4,4,7,9,2,6,9,13,6,6,7,11,3,4,12,13,2,5,14,15,2,10,11,15,1,12,12,17,8,9,12,17,1,6,18,19,6,6,17,19,6,10,15,21,4,5,20,21,4,8,19,21,4,13,16,21,8,11,16,21,3,6,22,23,3,13,18,23,6,13,18,23,9,14,20,25,12,15,16,25,2,7,26,27,2,10,25,27,2,14,23,27,7,14,22,27,10,10,23,27,3,16,24,29,11,12,24,29,12,16,21,29)
l3=(3,4,5,5,12,13,7,24,25,9,40,41,6,8,10,60,80,100,18,24,30,15,8,17)
l4=(1,2,3,4,5,6,7,8,9)

###################################################################################
# 4.Proszę napisać funkcję znajdującą miejsce zerowe funkcji w określonym przedziale z zadaną dokładnością (np. 10-7)
# metodą bisekcji. Jeżeli funkcja nie ma miejsca zerowego w zadanym przedziale lub jest nieokreślona
# w jakimś punkcie proszę zgłosić wyjątek (2.5p).
# Przykładowe funkcje:
# x+1 [-2, 0]
# x+1 [1, 2]
# (x-2)*(x-2)/(x-1)-2 [0, 2]
# (x-2)*(x-2)/(x-1)-2 [4, 6]
print('##############################ZAD_4##############################')

f1 = lambda x: x+1
f2 = lambda x: (x-2)*(x-2)/(x-1)-2

def fun4(fun, x_min, x_max, eps=10e-7):
    mid = (x_min+x_max)/2
    try:
        wart = fun(x_min)
        wart = fun(mid)
        wart = fun(x_max)
    except:
        print("funkcja jest nieokreslona w pewnym punkcie")
    else:
        if fun(x_min)*fun(x_max)<0:
            if -eps <= fun(mid) <= eps:
                print("miejsce zerowe funkcji to: ", mid)
            else:
                if fun(x_min)*fun(mid)<0:
                    fun4(fun, x_min, mid)
                elif fun(mid)*fun(x_max)<0:
                    fun4(fun, mid, x_max)
        else:
            try:
                if x_max-x_min < 2*eps:
                    raise
            except:
                print("brak miejsca zerowego")



print(fun4(f1, -2,0))
#print(fun4(f1, 1, 2))
print(fun4(f2, 0, 2))
print(fun4(f2, 4, 6))