#EJERCICIO 4:Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia. 
# El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.

sumatoria = 0
numeroUsuario = 1

while numeroUsuario !=0 :
    numeroUsuario = int(input("Por favor ingrese un número entero, para detener el proceso ingrese 0:"))
    sumatoria=sumatoria+numeroUsuario

print ("La sumatoria de todos los números ingresados es:",sumatoria,)
