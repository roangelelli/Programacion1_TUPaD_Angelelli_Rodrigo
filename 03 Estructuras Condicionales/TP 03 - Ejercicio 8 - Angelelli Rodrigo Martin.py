#Ejercicio 8: 8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee: 
# 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO. 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro. 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
# El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el usuario e imprimir el resultado por pantalla.

nombreUsuario = input("Por favor ingrese su nombre: ")
eleccion = input ("""Por favor ingrese su elección:
                  1 Si desea su nombre en mayúsculas.
                  2 Si desea su nombre en minúsculas.
                  3 Si desea si nombre con la primer letra mayúscula. 
                  """)
if eleccion == "1":
    print (nombreUsuario.upper())
elif eleccion == "2":
    print (nombreUsuario.lower())
elif eleccion == "3":
    print (nombreUsuario.title())
else:
    print ("La opción ingresada no es valida.")