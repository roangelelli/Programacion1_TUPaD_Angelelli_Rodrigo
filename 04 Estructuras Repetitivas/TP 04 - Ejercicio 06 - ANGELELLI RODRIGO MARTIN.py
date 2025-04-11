#EJERCICIO 6: Desarrolla un programa que imprima en pantalla todos los números pares comprendidos entre 0 y 100, en orden decreciente.

num = 100
for num in range (100,-1,-1):
    if num % 2 == 0:
        print (num)
