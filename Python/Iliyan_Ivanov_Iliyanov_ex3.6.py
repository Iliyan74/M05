l1 = float(input("Ingresa la longitud de l1:"))
l2 = float(input("Ingresa la longitud de l2:"))
l3 = float(input("Ingresa la longitud de l3:"))

if (l1 == l2) and (l2 == l3):
    print("El triángulo es equilátero")
elif (l1 == l2) or (l1 == l3) or (l2 == l3):
    print("El triángulo es isóceles")
else:
    print("El triángulo es escaleno")