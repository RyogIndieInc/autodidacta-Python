# src/lesson9_intro_player.py

# ACTIVIDAD PRÁCTICA: MENSAJE DE BIENVENIDA USANDO FUNCIONES DE ENTRADA Y SALIDA CON CONVERSIÓN DE TIPOS.

username = input("¿Cuál es tu nombre?: ")
# Convertimos a entero porque el nivel siempre será un número
initial_level = int(input("¿Cuál es tu nivel inicial?: "))

print(f"Bienvenido {username}, tu nivel actual es: {initial_level}")
print(f"¡Disfruta de esta gran aventura!")