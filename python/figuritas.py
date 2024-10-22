import math
#funcion para calcular area y perimetro de un rectangulo
def rectangulo(base,altura):
    area= base * altura
    perimetro = 2 * (base + altura)
    return area , perimetro
#funcion para calcular area y perimetro de un triangulo 
def triangulo(base, altura, lado1, lado2, lado3):
    area= base * altura 
    perimetro= lado1 + lado2 + lado3 
    return area, perimetro
#funcion para calcular el volumen de una esfera 
def esfera(radio):
    volumen=(4/3) * math.pi * radio** 3
    return volumen

#funcion del menu 
def menu():
    print("hola, bienvenido a python con funciones")
    print("elije una opcion:")
    print("A_ area y perimetro de un rectangulo")
    print("B_ area y perimetro de un triangulo")
    print("C_ volumen de una esfera")

    opcion = input("introduce la opcion deseada:").upper()
    if opcion == "A":
        base = float(input("introduce la base:"))
        altura = float(input("introduce la altura:"))
        area,perimetro = rectangulo(base,altura)
        print("el area es:", area)
        print("el perimetro es:", perimetro)

    elif opcion == "B":
        base = float(input("introduce la base:"))
        altura = float(input("introduce la altura:"))
        lado1 = float(input("introduce el lado1:"))
        lado2 = float(input("introduce el lado2:"))
        lado3 = float(input("introduce el lado3:"))
        area, perimetro = triangulo(base, altura, lado1, lado2, lado3)
        print("el area es:", area)
        print("el perimetro es:", perimetro)
    elif opcion == "c" :
        radio = float(input("introduce el radio:")) 
        volumen = esfera(radio)  
        print("el volumen es de:", volumen)

    else:
        print("opcion no valida, intentelo de nuevo")  

    #ejecutar el menu
menu()     