#Ejercicio 1: Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa
# función para calcular y mostrar en pantalla el factorial de todos los números enteros
# entre 1 y el número que indique el usuario

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Solicitar número al usuario
limite = int(input("Ingrese un número entero: "))

# Mostrar factoriales desde 1 hasta el número ingresado
for i in range(1, limite + 1):
    print(f"Factorial de {i} es {factorial(i):,}")

#Ejercicio 2: Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición indicada. 
#Posteriormente, muestra la serie completa hasta la posición que el usuario especifique.

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Solicitar al usuario hasta qué posición desea ver la serie
posicion = int(input("Ingrese la posición hasta la que desea ver la serie de Fibonacci: "))

# Mostrar la serie completa
print("Serie de Fibonacci:")
for i in range(posicion + 1):
    print(f"F({i}) = {fibonacci(i)}")

#Ejercicio 3: Crea una función recursiva que calcule la potencia de un número base elevado a un exponente, 
#utilizando la fórmula 𝑛𝑚 = 𝑛 ∗ 𝑛 (𝑚−1). Prueba esta función en un algoritmo general.

def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)

# Prueba general
base = int(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente: "))

resultado = potencia(base, exponente)
print(f"{base}^{exponente} = {resultado}")


#Ejercicio 4: Crear una función recursiva en Python que reciba un número entero positivo en base decimal 
# y devuelva su representación en binario como una cadena de texto.
def decimal_a_binario(n):
    if n == 0:
        return ""
    else:
        return decimal_a_binario(n // 2) + str(n % 2)

# Solicitar número al usuario
numero = int(input("Ingrese un número entero positivo: "))

if numero == 0:
    print("0")
else:
    binario = decimal_a_binario(numero)
    print(f"El número {numero} en binario es: {binario}")

#Ejercicio 5: Implementá una función recursiva llamada es_palindromo(palabra) que reciba una
# cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no lo es.
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    elif palabra[0] == palabra[-1]:
        return es_palindromo(palabra[1:-1])
    else:
        return False

palabra_ingresada = input("Ingresa una palabra (sin espacios ni tildes): ").lower()

if es_palindromo(palabra_ingresada):
    print(f"'{palabra_ingresada}' es un palíndromo.")
else:
    print(f"'{palabra_ingresada}' no es un palíndromo.")


#Ejercicio 6: Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un número
# entero positivo y devuelva la suma de todos sus dígitos.

def suma_digitos(n):
    if n < 10:
        return n
    else:
        return (n % 10) + suma_digitos(n // 10)

# Solicitar número al usuario
numero = int(input("Ingrese un número entero positivo: "))

if numero < 0:
    print("Debe ingresar un número positivo.")
else:
    resultado = suma_digitos(numero)
    print(f"La suma de los dígitos de {numero} es: {resultado}")

#Ejercicio 7: Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el
# nivel más bajo y devuelva el total de bloques que necesita para construir toda la pirámide.

def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)

# Solicitar número al usuario
nivel = int(input("Ingrese la cantidad de bloques en el nivel más bajo: "))

if nivel < 1:
    print("Debe ingresar un número entero positivo mayor o igual a 1.")
else:
    total = contar_bloques(nivel)
    print(f"Se necesitan {total} bloques para construir la pirámide.")

#Ejercicio 8: Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un
# número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces
# aparece ese dígito dentro del número.

def contar_digito(numero, digito):
    if numero == 0:
        return 0
    else:
        ultimo = numero % 10
        if ultimo == digito:
            return 1 + contar_digito(numero // 10, digito)
        else:
            return contar_digito(numero // 10, digito)

# Entrada del usuario
numero = int(input("Ingrese un número entero positivo: "))
digito = int(input("Ingrese el dígito a contar (0 a 9): "))

if numero < 0 or digito < 0 or digito > 9:
    print("Entrada inválida. Asegúrese de ingresar un número positivo y un dígito entre 0 y 9.")
else:
    cantidad = contar_digito(numero, digito)
    print(f"El dígito {digito} aparece {cantidad} veces en el número {numero}.")
