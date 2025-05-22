# Id de estudiante: 160642
# Nombre y apellidos de estudiante: Gabriel Colmenares
# Nombre de la Universidad: Dewey University
# Código y título del curso: COMP315-C4-2025SP
# Nombre del programa: Programa 1 - Conversor de Temperaturas
# Fecha de entrega: 21 de mayo del 2025
# Descripción general: Programa en Python que convierte temperaturas entre Fahrenheit y Celsius
# para múltiples entradas usando listas, bucles, comprensión de listas y salida tabular.

# Programa 1: Conversor de Temperaturas (Fahrenheit ↔ Celsius)

# Solicitar al usuario cuántas temperaturas desea convertir
cantidad = int(input("¿Cuántas temperaturas quieres convertir? "))

# Listas para almacenar datos
temperaturas_entrada = []
unidades_entrada = []

# Recolectar datos usando bucle
for i in range(cantidad):
    temp = float(input(f"\nTemperatura {i+1}: "))
    unidad = input("¿Esta temperatura está en (F)ahrenheit o (C)elsius? ").strip().upper()
    
    # Validar unidad
    while unidad not in ['F', 'C']:
        print("Unidad inválida. Por favor escribe F o C.")
        unidad = input("¿Esta temperatura está en (F)ahrenheit o (C)elsius? ").strip().upper()
    
    temperaturas_entrada.append(temp)
    unidades_entrada.append(unidad)

# Realizar conversiones usando comprensión de listas
temperaturas_convertidas = [
    round((t - 32) * 5/9, 2) if u == 'F' else round((t * 9/5) + 32, 2)
    for t, u in zip(temperaturas_entrada, unidades_entrada)
]

# Mostrar tabla de resultados como en la imagen
print("\nOriginal       Convertida")
for t, u, conv in zip(temperaturas_entrada, unidades_entrada, temperaturas_convertidas):
    unidad_original = "°F" if u == 'F' else "°C"
    unidad_convertida = "°C" if u == 'F' else "°F"
    print(f"{t:6.2f}{unidad_original:<2}   -> {conv:6.2f}{unidad_convertida}")