#EJERCICIO 8: Escribe un programa que permita al usuario ingresar 100 números enteros. 
# Luego, el programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son negativos y cuántos son positivos. 

contador = 0
numUsuario=0
numPositivos=0
numNegativos=0
numPar=0
numImpar=0

while contador != 100: #AL CAMBIAR EL VALOR 100 POR OTRO NÚMERO, PODREMOS TESTEARLO CON MENOS VALORES.
    numUsuario=int(input ("Por favor ingrese un número entero:"))
    contador = contador + 1

    if numUsuario % 2 == 0:
        numPar = numPar+1
    else:
        numImpar=numImpar+1

    if numUsuario > 0:
        numPositivos=numPositivos+1
    else:
        numNegativos=numNegativos+1

print (f"""El desglose de sus numeros es:
• Números positivos: {numPositivos}
• Números negativos: {numNegativos}
• Números pares: {numPar}
• Números impares: {numImpar}
""")    
            