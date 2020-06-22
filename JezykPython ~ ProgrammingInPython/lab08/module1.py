import random

def fun1(iter_num):
    x0 = random.random()
    y0 = random.random()
    param = [(0,0,0,0,0.16,0), (0.2,-0.26,0,0.23,0.22,1.6), (-0.15,0.28,0,0.26,0.24,0.44), (0.85,0.04,0,-0.04,0.85,1.6)]
    with open('output.txt', 'w') as out:
        out.write(str(x0) + '\t' + str(y0) + '\n')
        for _ in range(iter_num):
            actual_param = random.choices(param, weights=[1, 7, 7, 85], k=1)
            actual_param = actual_param[0]
            #print(actual_param)
            x0 = actual_param[0]*x0 + actual_param[1]*y0 + actual_param[2]
            y0 = actual_param[3]*x0 + actual_param[4]*y0 + actual_param[5]
            out.write(str(x0) + '\t' + str(y0) + '\n')


import scipy.integrate

def fun2(funkcja, x_min, x_max):
    proper_result = scipy.integrate.quad(funkcja,x_min,x_max)
    print("Wynik wlasciwy: ", proper_result[0])
    t = 0
    min = 100000
    max = -100000
    eps = 0.000001
    start = x_min
    while start < x_max:
        if funkcja(start) > max:
            max = funkcja(start)
        if funkcja(start) < min:
            min = funkcja(start)
        start = start + eps
    #print(min, "    ", max)
    #n = 100000                     # dla konkretnej ilosci iteracji - do testow
    # for _ in range(n):
    #     x = random.uniform(x_min,x_max)
    #     y = random.uniform(min, max)
    #     if 0 < y <= funkcja(x):
    #         t = t+1
    #     if funkcja(x) <= y < 0:
    #         t = t-1
    # print("Wynik obliczony: ", abs(x_max-x_min)*abs(max-min)*t/n)
    iter = 0
    while True:
        x = random.uniform(x_min,x_max)
        y = random.uniform(min, max)
        if 0 < y <= funkcja(x):
            t = t+1
        if funkcja(x) <= y < 0:
            t = t-1
        iter = iter + 1
        if proper_result[0] - eps < abs(x_max-x_min)*abs(max-min)*t/iter < proper_result[0] + eps:
            print("Wynik obliczony: ", abs(x_max-x_min)*abs(max-min)*t/iter,"\nIlosc iteracji: ", iter)
            break

def fun3(funkcja, x_min, x_max):
    proper_result = scipy.integrate.quad(funkcja,x_min,x_max)
    print("Wynik wlasciwy: ", proper_result[0])
    eps = 0.000001
    suma = 0
    iter = 0
    while True:
        x = random.uniform(x_min,x_max)
        suma = suma + funkcja(x)
        iter = iter + 1
        if proper_result[0] - eps < abs(x_max-x_min)*suma/iter < proper_result[0] + eps:
            print("Wynik obliczony: ", abs(x_max-x_min)*suma/iter,"\nIlosc iteracji: ", iter)
            break