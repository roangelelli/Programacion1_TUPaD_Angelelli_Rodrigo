#EJERCICIO 10: Escribe un programa que invierta el orden de los dígitos de un número ingresado por el usuario. 
numero = input("Ingrese un número: ")

if numero.startswith('-'):
    invertido = '-' + numero[:0:-1] 
else:
    invertido = numero[::-1]

print("Número invertido:", invertido)
