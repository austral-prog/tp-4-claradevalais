def line():
    print("TO DO")
    coefa = float(input("Ingrese el coeficiente A: "))
    coefb = float(input("Ingrese el coeficiente B: "))
    coefx1 = float(input("Ingrese el coeficiente X1: "))
    coefx2 = float(input("Ingrese el coeficiente X2: "))
    print(f"El coeficiente A de su ecuación de la recta es: {coefa}")
    print(f"El coeficiente B de su ecuación de la recta es: {coefb}")
    print(f"El coeficiente X1 de su ecuación de la recta es: {coefx1}")
    print(f"El coeficiente X2 de su ecuación de la recta es: {coefx2}")
    print("")
    print("Para la siguiente ecuación:")
    print(f"\tY = {coefa}X + {coefb}")
    print("")
    print("Dados los siguientes puntos:")
    
    y1 = (coefa * coefx1) + coefb
    y2 = (coefa * coefx2) + coefb
    dist = ((coefx2 - coefx1)**2 + (y2 - y1)**2)**0.5

    print(f"\tP1 ({coefx1}, {(coefa * coefx1) + coefb})")
    print(f"\tP2 ({coefx2}, {(coefa * coefx2) + coefb})")
    print(f"La distancia entre ellos es: {dist}")

line()
