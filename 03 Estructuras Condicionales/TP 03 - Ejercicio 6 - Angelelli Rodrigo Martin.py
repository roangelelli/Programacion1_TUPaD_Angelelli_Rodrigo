#Ejercicio 6: Escribir un programa que tome la lista numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar 
# si hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.

from statistics import mode, median, mean
import random

numeros_aleatorios = [random.randint(1,100) for i in range(50)]
print (numeros_aleatorios)

moda = mode(numeros_aleatorios)
media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)

print(f"La moda de la lista de números es {moda}.")
print(f"La media de la lista de números es {media}.")
print(f"La mediana de la lista de números es {mediana}.")

if media > mediana and mediana > moda:
    print ("La lista de números tiene un sesgo positivo.")
elif media < mediana and mediana < moda:
    print ("La lista de números tiene un sesgo negativo.")
elif media == mediana == moda:
    print ("La lista de números no tiene sesgo.")
else:
    pass

