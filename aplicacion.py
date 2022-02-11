def Show_Menu():
    print()
    print()
    optionDict = {
        " 0": "crear una nueva person card",
        " 1": "buscar una person card por id",
        " 2": "mostrar todas las person cards",
        " 3": "actualizar una person card",
        " 4": "eliminar una person card",
        "-1": "salir de la app",
    }
    for option, value in optionDict.items():
        print(f"{option}::{value}")
    print()


while True:
    Show_Menu()
    option = int(input("opción: "))
    if option == -1:
        break
    elif option == 0:
        pass
    elif option == 1:
        pass
    elif option == 2:
        pass
    elif option == 3:
        pass
    elif option == 4:
        pass
    else:
        print("la app continua...")
