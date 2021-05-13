import math

def calculadora():
    print("Calcuadora de Volumenes")
    menu = """
    1 - Calcular Volumen de un Cubo
    2 - Calcular Volumen de un Prisma Rectangular
    3 - Calcular Volumen de un Cilindro
    4 - Calcular Volumen de una Esfera
    5 - Calcular Volumen de un Cono 
    
    Seleccione una opcion """

    opcion = int(input(menu))
    if opcion == 1:
        print("Se Calculara el volumen de un Cubo")
        lado = int(input("Inserta cuanto mide uno de los lados: "))
        vol_cubo = lado*3
        print("El Volumen de tu Cubo es de " + str(vol_cubo) + " unidades cubicas")
    elif opcion == 2:
        print("Se Calculara el volumen de un Prisma Rectangular")
        base_prisma = int(input("Inserta cuanto mide la base del prisma: "))
        altura_prisma = int(input("Inserta cuanto mide la altura del prisma: "))
        ancho_prisma = int(input("Inserta cuanto mide el ancho del prisma: "))
        vol_prisma = base_prisma*ancho_prisma*altura_prisma
        print("El Volumen de tu Prisma Rectangular es de " + str(vol_prisma) + " unidades cubicas")
    elif opcion == 3:
        print("Se Calculara el volumen de un Cilindro")
        radio_cilindro = int(input("Inserta cuanto mide el radio del Cilindro: "))
        altura_cilindro = int(input("Inserta cuanto mide la altura del Cilindro: "))
        vol_cilindro = altura_cilindro*math.pi*pow(radio_cilindro,2)
        print("El Volumen del Cilindro es de " + str(vol_cilindro) + " unidades cubicas")
    elif opcion == 4:
        print("Se Calculara el volumen de una Esfera")
        radio_esfera = int(input("Inserta cuanto mide el radio del Cono: "))
        radio_cubico = pow(radio_esfera,3)
        vol_esfera = (4/3)*math.pi*radio_cubico
        print("El Volumen de la Esfera es de " + str(vol_esfera) + " unidades cubicas")
    elif opcion == 5:
        print("Se Calculara el volumen de un Cono")
        radio_cono = int(input("Inserta cuanto mide el radio del Cono: "))
        altura_cono = int(input("Inserta cuanto mide la altura del Cono: "))
        vol_cono = altura_cono*math.pi*pow(radio_cono,2)*(2/3)
        print("El Volumen del Cono es de " + str(vol_cono) + " unidades cubicas")
    else:
        print("Inserte una Opcion Valida")



if  __name__ == '__main__':
    calculadora()