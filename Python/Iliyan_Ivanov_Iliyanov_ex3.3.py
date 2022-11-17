edadpe = int(input("Ingresa la edad de el perro: "))

if edadpe <= 2:
    equivalente = edadpe * 10.5
    print("En años humanos es: ", equivalente)
else:
    equivalente = (edadpe * 10.5) + ((edadpe-2) * 4)
    print(" En años humanos es: ", equivalente)