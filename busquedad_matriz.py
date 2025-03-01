def buscar_valor(matriz, valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return f"Valor {valor} encontrado en la posición ({i}, {j})"
    return f"Valor {valor} no encontrado"

# Definimos una matriz de ejemplo
matriz = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

# Pedimos al usuario un número a buscar
valor_buscar = int(input("Ingresa el número a buscar: "))
resultado = buscar_valor(matriz, valor_buscar)
print(resultado)