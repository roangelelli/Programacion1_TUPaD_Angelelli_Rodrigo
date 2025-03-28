# Ejercicio 1: Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.
print ("Hola Mundo!")


# Ejercicio 2: Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando el nombre ingresado.
#Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir por pantalla “Hola Marcos!”
nombre = input ("Por favor ingrese su nombre: ")
print (f"Hola {nombre}!")


# Ejercicio 3: Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e imprima por pantalla una oración con los datos ingresados. 
#Por ejemplo: si el usuario ingresa “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30 años y vivo en Argentina”
nombre = input ("Por favor ingrese su nombre: ")
apellido = input ("Por favor ingrese su apellido: ")
edad = input ("Por favor ingrese su edad: ")
residencia = input ("Por favor ingrese su localidad de residencia: ")
print (f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}." ) 


#Ejercicio 4: Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro.
import math
pi= math.pi
radio = float (input ("Por favor ingrese el radio de su circuferencia: "))
areaCirc =  pi*(radio**2)
perCirc =  2*pi*radio
print (f"El área de su círculo es {areaCirc:.2f} y el perímetro es {perCirc:.2f} ")


#Ejercicio 5: Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale.
segundos = int (input ("Por favor ingrese una cantidad de segundos: "))
minutos = segundos // 60
horas = minutos / 60
print (f"Los segundos ingresados equivalen {horas:.2f} horas. ")


#Ejercicio 6: Crear un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número.
numeroUsuario = int (input ("Por favor ingrese un número entero: "))
print(f"{numeroUsuario} x 1 = {numeroUsuario * 1}")
print(f"{numeroUsuario} x 2 = {numeroUsuario * 2}")
print(f"{numeroUsuario} x 3 = {numeroUsuario * 3}")
print(f"{numeroUsuario} x 4 = {numeroUsuario * 4}")
print(f"{numeroUsuario} x 5 = {numeroUsuario * 5}")
print(f"{numeroUsuario} x 6 = {numeroUsuario * 6}")
print(f"{numeroUsuario} x 7 = {numeroUsuario * 7}")
print(f"{numeroUsuario} x 8 = {numeroUsuario * 8}")
print(f"{numeroUsuario} x 9 = {numeroUsuario * 9}")
print(f"{numeroUsuario} x 10 = {numeroUsuario * 10}")


#Ejercicio 7:Crear un programa que pida al usuario dos números enteros distintos del 0 
# y muestre por pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.
num1 = int (input("Por favor ingrese un número entero distinto a cero: "))
num2 = int (input("Por favor ingrese otro número entero distinto a cero: "))
suma = num1 + num2
div = num1 / num2
mult = num1 * num2
resta = num1 - num2
print (f"La suma de {num1} + {num2} es {suma}")
print (f"La división de {num1} / {num2} es {div}")
print (f"La multiplicación de {num1} * {num2} es {mult}")
print (f"La resta de {num1} - {num2} es {resta}")


#Ejercicio8: Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice de masa corporal.
altura = float (input ("Por favor ingrese su altura: "))
peso = float (input ("Por favor ingrese su peso: "))
IMC = peso / (altura**2)
print (f"Su índice de masa corporal (IMC) es: {IMC:.2f}" )


#Ejercicio9: Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por pantalla su equivalente en grados Fahrenheit.
celsius = float (input ("Por favor ingrese la temperatura en grados Celsius: "))
fht = (celsius*9/5)+32
print (f"El equivalente en grados Fahrenheit es: {fht}")


#Ejercicio10: Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de dichos números.
numUsu1 = float (input ("Por favor ingrese un número: "))
numUsu2 = float (input ("Por favor ingrese un número: "))
numUsu3 = float (input ("Por favor ingrese un número: "))
promedio = (numUsu1+numUsu2+numUsu3)/3
print (f"El promedio de sus números ingresados es: {promedio:.2f}.")