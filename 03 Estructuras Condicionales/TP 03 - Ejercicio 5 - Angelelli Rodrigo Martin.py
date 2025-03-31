#Ejercicio 5: ) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada,
#  imprimir por en pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres".
contraseña = input ("Por favor ingrese una contraseña entre 8 y 14 caracteres: ")

if len(contraseña) > 14:
    print ("Por favor ingrese una contraseña de entre 8 y 14 caracteres.")
elif len(contraseña) < 8:
    print ("Por favor ingrese una contraseña de entre 8 y 14 caracteres.")
else:
    print ("Ha ingresado una contraseña correcta.")

