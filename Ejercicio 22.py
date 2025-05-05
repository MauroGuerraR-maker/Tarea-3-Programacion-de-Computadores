#Numeros impares menores que

numero = int(input("Introduce un número entero: "))

print(f"Números impares menores que {numero}:")

for i in range(1, numero):
    if i % 2 != 0:
        print(i)

