# Id de estudiante: 160642
# Nombre y apellidos de estudiante: Gabriel Colmenares
# Nombre de la Universidad: Dewey University
# Código y título del curso: COMP315-C4-2025SP
# Nombre del programa: Programa 2 - Manipulación de Listas
# Fecha de entrega: 21 de mayo del 2025
# Descripción general: Programa en Python que realiza múltiples operaciones sobre una lista de números.
# Utiliza métodos de listas, comprensión de listas, conjuntos (sets) y funciones incorporadas.

# Programa 2: Manipulación de Listas

# Solicitar números al usuario
entrada = input("Ingresa una serie de números separados por espacios: ")

# Convertir la entrada en una lista de enteros
numeros = list(map(int, entrada.split()))

print("\nLista original:", numeros)

# Operaciones sobre la lista
suma_total = sum(numeros)
maximo = max(numeros)
minimo = min(numeros)
promedio = round(suma_total / len(numeros), 2)

# Eliminar duplicados usando set y volver a convertir a lista
sin_duplicados = list(set(numeros))

# Ordenar lista
ordenada = sorted(sin_duplicados)

# Obtener solo los números pares con comprensión de listas
pares = [n for n in numeros if n % 2 == 0]

# Mostrar resultados
print(f"\nSuma de todos los números: {suma_total}")
print(f"Valor máximo: {maximo}")
print(f"Valor mínimo: {minimo}")
print(f"Promedio: {promedio}")
print(f"Lista sin duplicados: {sorted(sin_duplicados)}")
print(f"Lista ordenada: {ordenada}")
print(f"Números pares: {pares}")
