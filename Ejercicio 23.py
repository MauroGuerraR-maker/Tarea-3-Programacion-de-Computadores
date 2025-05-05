a = int(input("Introduce el primer número: "))
b = int(input("Introduce el segundo número: "))

while b != 0:
    a, b = b, a % b

print("El máximo común divisor entre ambos numeros es:", a)
