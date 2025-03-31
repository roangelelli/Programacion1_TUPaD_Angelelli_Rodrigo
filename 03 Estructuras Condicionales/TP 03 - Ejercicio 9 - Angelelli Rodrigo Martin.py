#Ejercicio 9: Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la magnitud en una de las siguientes categorías según la escala de Richter
# e imprima el resultado por pantalla.

magnitudTerremoto = float(input("Por favor ingrese la magnitud del terremoto: "))
if magnitudTerremoto < 3:
    print ("Muy leve (imperceptible).")
elif magnitudTerremoto >= 3 and magnitudTerremoto < 4:
    print ("Leve (ligeramente perceptible).")
elif magnitudTerremoto >= 4 and magnitudTerremoto < 5:
    print ("Moderado (sentido por personas, pero generalmente no causa daños).")
elif magnitudTerremoto >= 5 and magnitudTerremoto < 6:
    print ("Fuerte (puede causar daños en estructuras débiles).")
elif magnitudTerremoto >= 6 and magnitudTerremoto < 7:
    print ("Muy fuerte (puede causar daños significativos).")
elif magnitudTerremoto >= 7:
    print ("Extremo (puede causar graves daños a gran escala).")
else: 
    pass