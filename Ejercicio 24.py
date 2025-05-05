import math

# Leer coeficientes
a = float(input("Introduce el coeficiente a: "))
b = float(input("Introduce el coeficiente b: "))
c = float(input("Introduce el coeficiente c: "))

# Verificar que no sea una ecuación de primer grado
if a == 0:
    print("No es una ecuación de segundo grado.")
else:
    discriminante = b**2 - 4*a*c

    if discriminante > 0:
        x1 = (-b + math.sqrt(discriminante)) / (2*a)
        x2 = (-b - math.sqrt(discriminante)) / (2*a)
        print("Tiene dos soluciones reales:")
        print("x1 =", x1)
        print("x2 =", x2)
    elif discriminante == 0:
        x = -b / (2*a)
        print("Tiene una solución real doble:")
        print("x =", x)
    else:
        print("No tiene soluciones reales.")
