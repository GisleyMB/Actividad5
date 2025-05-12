def mcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Uso del algoritmo
x = int(input("Ingresa el primer número: "))
y = int(input("Ingresa el segundo número: "))
resultado = mcd(x, y)
print(f"El máximo común divisor de {x} y {y} es: {resultado}")

