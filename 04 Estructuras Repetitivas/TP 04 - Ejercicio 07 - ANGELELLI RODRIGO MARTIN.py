#EJERCICIO 7: Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario.

sumatoria=0
numeroUsuario = int(input ("Por favor ingrese un número entero positivo: "))

while numeroUsuario < 0:
    numeroUsuario = int(input ("El número ingresado no es positivo, ingrese otro: "))

for i in range (0,numeroUsuario+1):
    sumatoria=sumatoria+i
print ("La suma de los números comprendidos entre el cero y su número es:",sumatoria,)
