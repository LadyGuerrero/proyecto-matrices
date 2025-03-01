def bubble_sort(fila):
    n = len(fila)
    for i in range(n):
        for j in range(0, n - i - 1):
            if fila[j] > fila[j + 1]:
                fila[j], fila[j + 1] = fila[j + 1], fila[j]

def mostrar_matriz(matriz):
    for fila in matriz:
        print(fila)

# Definimos una matriz de ejemplo
matriz = [
    [34, 21, 56],
    [12, 78, 45],
    [89, 65, 23]
]

# Mostramos la matriz original
print("Matriz original:")
mostrar_matriz(matriz)

# Pedimos al usuario la fila a ordenar
fila_ordenar = int(input("Ingresa el índice de la fila a ordenar (0-2): "))

# Ordenamos la fila seleccionada
bubble_sort(matriz[fila_ordenar])

# Mostramos la matriz después de la ordenación
print("\nMatriz después de ordenar la fila:")
mostrar_matriz(matriz)