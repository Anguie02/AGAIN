# importamos el módulo random 
import random
# Definimos una función
#dejamos dos lineas al princio y al final de una funcion 


def adivina_el_número(x):
    print("°°°°°°°°°°°°°°°°°°°°°°°°°")
    print("Bienvendio(a) al juego!!!")
    print("Tu meta es adivinar el número generado por la computadora")
    print("°°°°°°°°°°°°°°°°°°°°°°°°°")
    # creamos una variable para almacenar el número aleatorio
    num_aleatorio = random.randint(1,x)
    # creamos un bucle
    prediccion = 0
    while prediccion != num_aleatorio:
        prediccion = int(input(f"Adivina un número entre 1 y {x}: "))

        if prediccion < num_aleatorio:
            print("Intenta otra vez. Este número es muy pequeño.")
        elif prediccion > num_aleatorio:
            print("Intenta otra vez. Este número es muy grande.")

    print(f"Felicidades adivinaste el número {num_aleatorio} correctamente")   

adivina_el_número(10)          

