import random

def rangos():
    print("Tu numero esta dentro del limite?")
    numero = int(input("Inserta aqui tu numero: "))
    limite_inferior = random.randint(0,500)
    limite_superior = random.randint(501,1000)
    if numero >= limite_inferior and numero <= limite_superior:
        print("Tu numero esta en Rango")
    else:
        print("Tu numero esta fuera de rango")


if __name__== "__main__":
    rangos()