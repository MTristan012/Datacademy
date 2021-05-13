def area_triangulo():
    print("Area de un Triangulo")
    base = int(input("Cuanto mide la base?: "))
    altura = int(input("cuanto mide la altura?: "))
    area = (base * altura)/2
    print("El area de tu Triangulo es " + str(area) + " unidades cuadradas")
    print("Tipo de Triangulo")
    lado_a = int(input("Inserta cuanto vale el lado A de tu triangulo: "))
    lado_b = int(input("Inserta cuanto vale el lado B de tu triangulo: "))
    lado_c = int(input("Inserta cuanto vale el lado C de tu triangulo: "))
    if lado_a == lado_b == lado_c:
        print("Tu Triangulo es Equilatero")
    elif lado_a == lado_b != lado_c:
        print("Tu Triangulo es Isoseles")
    elif lado_a != lado_b == lado_c:
        print("Tu Triangulo es Isoseles")
    else:
        print("Tu Triangulo es Escaleno")
    

if __name__ == '__main__':
    area_triangulo()