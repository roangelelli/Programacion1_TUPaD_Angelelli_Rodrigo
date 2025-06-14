# 1 - Crear una función llamada imprimir_hola_mundo que imprima por pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el programa principal.

def imprimir_hola_mundo():
    print("Hola Mundo!")

imprimir_hola_mundo()

# 2 - Crear una función llamada saludar_usuario(nombre) que reciba como parámetro un nombre y devuelva un saludo personalizado.

def saludar_usuario(nombre):
    return f"Hola {nombre}!"

nombre = input("Ingrese su nombre: ")
print(saludar_usuario(nombre))

# 3 - Crear una función llamada informacion_personal(nombre, apellido, edad, residencia) que reciba cuatro parámetros e imprima una presentación personal.

def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

nombre = input("Nombre: ")
apellido = input("Apellido: ")
edad = input("Edad: ")
residencia = input("Residencia: ")
informacion_personal(nombre, apellido, edad, residencia)

# 4 - Crear dos funciones para calcular área y perímetro de un círculo dado el radio.
import math

def calcular_area_circulo(radio):
    return math.pi * radio ** 2

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

radio = float(input("Ingrese el radio del circulo: "))
print("area:", calcular_area_circulo(radio))
print("Perimetro:", calcular_perimetro_circulo(radio))

# 5 - Crear una función que convierta una cantidad de segundos a horas.

def segundos_a_horas(segundos):
    return segundos / 3600

segundos = int(input("Ingrese la cantidad de segundos: "))
print("Horas equivalentes:", segundos_a_horas(segundos))

# 6 - Crear una función que imprima la tabla de multiplicar del 1 al 10 de un número dado.

def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

numero = int(input("Ingrese un numero para ver su tabla de multiplicar: "))
tabla_multiplicar(numero)

# 7 - Crear una función que reciba dos números y devuelva una tabla con suma, resta, multiplicación y división.

def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "Indefinido"
    return (suma, resta, multiplicacion, division)

a = float(input("Primer numero: "))
b = float(input("Segundo numero: "))
resultados = operaciones_basicas(a, b)
print("Suma:", resultados[0])
print("Resta:", resultados[1])
print("Multiplicacion:", resultados[2])
print("Division:", resultados[3])

# 8 - Crear una función que calcule el índice de masa corporal (IMC) dados el peso y la altura.

def calcular_imc(peso, altura):
    return peso / (altura ** 2)

peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))
print("IMC:", round(calcular_imc(peso, altura), 2))

# 9 - Crear una función que convierta grados Celsius a Fahrenheit.

def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

celsius = float(input("Temperatura en Celsius: "))
print("Equivalente en Fahrenheit:", celsius_a_fahrenheit(celsius))

# 10 - Crear una función que calcule el promedio de tres números.

def calcular_promedio(a, b, c):
    return (a + b + c) / 3

a = float(input("Primer numero: "))
b = float(input("Segundo numero: "))
c = float(input("Tercer numero: "))
print("Promedio:", calcular_promedio(a, b, c))
