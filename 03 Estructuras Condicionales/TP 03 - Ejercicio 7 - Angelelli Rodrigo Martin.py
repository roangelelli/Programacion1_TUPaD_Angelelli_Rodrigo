#Ejercicio 7: Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado termina con vocal, añadir un signo de exclamación al final 
# e imprimir el string resultante por pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.

fraseUsuario = input("Por favor ingrese una palabra o frase: ")
ultimaLetra = fraseUsuario[-1].lower()

if ultimaLetra == "a" or ultimaLetra == "e" or ultimaLetra == "i" or ultimaLetra == "o" or ultimaLetra == "u":
    print (fraseUsuario+"!")
else:
    print (fraseUsuario)