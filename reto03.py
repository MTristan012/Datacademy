def conversor():
    print("Conversor")
    menu = """
    1 - Millas a Kilometros
    2 - Kilometros a Millas
    Selecciona una opcion: """
    mk = int(input(menu))
    if mk == 1:
        millas = float(input("Inserte las Millas: "))
        cv_kilometros = millas*1.609344 
        print(str(cv_kilometros) + " Kilometros") 
    elif mk == 2:
        kilometros = float(input("Inserte los Kilometros: "))
        cv_millas = kilometros/1.609344
        print(str(cv_millas) + " millas")
    else:
        print("Ninguna opcion es valida")


if __name__ == '__main__':
    conversor()