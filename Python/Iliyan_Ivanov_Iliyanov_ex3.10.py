tamaño= float(input("Ingresa el tamaño del tornillo en cm:"))


if (tamaño >= 1) and (tamaño <= 2.9):
    print("Tamaño pequeño")
elif (tamaño >= 3) and (tamaño <= 4.9):
    print("Tamaño mediano")
elif (tamaño >= 5) and (tamaño <= 6.4):
    print("Tamaño grande")
elif (tamaño >= 6.5) and (tamaño <= 8.4):
    print("Tamaño muy grande")
else:
    print("No hay tornillo de ese tamaño")