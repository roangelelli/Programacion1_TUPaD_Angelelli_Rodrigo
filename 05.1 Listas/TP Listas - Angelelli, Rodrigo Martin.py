#Ejercicio 1: Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función range.

lista_ejercicio_1 = list(range(4,101,4))
print(lista_ejercicio_1)

#Ejercicio 2: Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el penúltimo. 

lista_ejercicio_2 = ["Iphone","AppleWatch","Mac","AirPods","VisionPro"]
print(lista_ejercicio_2[-2])

#Ejercicio 3: Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por pantalla.
lista_ejercicio_3=[]
lista_ejercicio_3.append("Gatos")
lista_ejercicio_3.append("Perros")
lista_ejercicio_3.append("Pajaros")
print(lista_ejercicio_3)

#Ejercico 4: Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”, respectivamente. 
#Imprimir la lista resultante por pantalla.

animales=["perro","gato","conejo","pez"]
animales[1]="loro"
animales[3]="oso"
print(animales)

#Ejercicio 5: Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.
#numeros = [8,15,3,22,7]
#numeros.remove (max(numeros))
#print(numeros)
#Respuesta: Lo que realiza el siguiente problema, es crear una lista denominada numeros, con 5 numeros enteros como elementos,
#luego utiliza la funcion .remove para eliminar elementos en conjunto con la funcion 'max' para eliminar unicamente el mayor valor de la lista,
#al ejecutarse, como consecuencia en este caso se elimina el valor '22' ya que es el maximo.

#Ejercicio 6: Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por pantalla los dos primeros.

lista_ejercicio_6 = list(range(10,31,5))
print(lista_ejercicio_6[0])
print(lista_ejercicio_6[1])

#Ejercicio 7: Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores cualquiera.

autos=["sedan","polo","suran","gol"]
autos[1]="hatchback"
autos[2]="4x4"
print(autos)

#Ejercicio 8: Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append directamente. 
#Imprimir la lista resultante por pantalla.

dobles=[]
dobles.append(5*2)
dobles.append(10*2)
dobles.append(15*2)
print(dobles)

#Ejercicio 9: Dada la lista “compras”, cuyos elementos representan los productos comprados por diferentes clientes:
#a) Agregar "jugo" a la lista del tercer cliente usando append.
#b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
#c) Eliminar "pan" de la lista del primer cliente.
#d) Imprimir la lista resultante por pantalla.

compras=[["pan","leche"],["arroz","fideos","salsa"],["agua"]]
compras[2].append("jugo")
compras[1][1]="tallarines"
compras[0].remove("pan")
print(compras)

#Ejercicio 10: Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:
# ● Posición lista_anidada[0]: 15
# ● Posición lista_anidada[1]: True
# ● Posición lista_anidada[2][0]: 25.5
# ● Posición lista_anidada[2][1]: 57.9
# ● Posición lista_anidada[2][2]: 30.6
# ● Posición lista_anidada[3]: False
# Imprimir la lista resultante por pantalla.

lista_anidada=[[0],[True],[25.5,57.9,30.6],[False]]
print(lista_anidada)
