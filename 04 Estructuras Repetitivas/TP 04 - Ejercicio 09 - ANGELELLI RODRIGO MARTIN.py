#EJERCICIO 9: Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la media de esos valores.
suma=0
contador=0

while contador != 10: #CAMBIANDO EL NUMERO 100 SE PUEDE TESTEAR CON MENOS VALORES.
    numeroUsuario = int(input ("Por favor ingrese un número entero:"))
    contador = contador + 1
    suma= suma + numeroUsuario

print (f"La media de sus números ingresados es: {suma/contador}")
