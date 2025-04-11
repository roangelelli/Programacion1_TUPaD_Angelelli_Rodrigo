#EJERCICIO 5: Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. 
# Al final, el programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

from random import randint

numeroAleatorio = randint(0,9)
numeroUsuario=int(input("Por favor ingrese un número para intentar adivinar: "))
contador=1

while numeroUsuario != numeroAleatorio:
    numeroUsuario=int(input("Por favor ingrese otro número para intentarlo nuevamente: "))
    contador=contador+1

print (f"Felicitaciones, el número aleatorio era {numeroAleatorio} y usted lo adivino en {contador} intentos.")