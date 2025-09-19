# src/lesson5_working_with_variables.py

# Variables iniciales
oro = 100
pociones = 3
jugador = "RyogDev"

print(f"{jugador} tiene {oro} monedas de oro y {pociones} pociones.")

# Actualizando valores
oro += 50     # oro = oro + 50
pociones -= 1 # pociones = pociones - 1

print(f"Después de la misión, {jugador} tiene {oro} monedas y {pociones} pociones.")

# Operadores compuestos adicionales
oro *= 2   # duplica el oro
pociones //= 2  # divide pociones y redondea hacia abajo

print(f"Tras encontrar un tesoro, {jugador} tiene {oro} monedas y {pociones} pociones.")

# Combinar texto + número (ojo!)
nivel = 5
print("Nivel actual: " + str(nivel))  # conversión explícita
print(f"Nivel actual: {nivel}")       # mejor con f-string
