x= float(input("Ingresa el coeficiente x:"))
y= float(input("Ingresa el coeficiente y:"))

if x != 0:
    print("Hay una solución, la solución es=", (-y/x))
elif (x == 0) and (y != 0 ):
    print("La ecuación no tiene ninguna solución")
elif (x == 0) and (y == 0):
    print("Hay infinitas soluciones")