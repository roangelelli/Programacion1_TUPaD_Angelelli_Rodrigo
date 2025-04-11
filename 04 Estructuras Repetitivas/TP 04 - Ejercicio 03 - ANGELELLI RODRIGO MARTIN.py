#EJERCICIO 3:Escribe un programa que sume todos los números enteros comprendidos entre dos valores dados por el usuario, excluyendo esos dos valores.
numero1 = int(input ("Por favor ingrese un número entero: "))
numero2 = int(input ("Por favor ingrese otro número entero: "))
sumatoria = 0

for i in range (numero1+1, numero2,1):
    sumatoria = sumatoria + i

print ("La sumatoria de los números comprendidos es:",sumatoria,)