# src/lesson10_player_card.py

# Actividad práctica: Ficha del héroe

name = input("¿Cuál es tu nombre?: ")
level = int(input("¿Cuál es tu nivel?: "))
height = float(input("¿Cuál es tu estatura?: "))
initial_object = None

print(" " * 30)
print("🧾 Ficha del héroe")
print(f"El nombre del héroe es: {name}")
print(f"¡Oh!, excelente, eres nivel: {level}")
print(f"Tienes la estatura perfecta de un héroe: {height}")
print(f"¿Tienes armas? {initial_object}")

print(" " * 30)
initial_object = "Espada"

print(" " * 30)
print(f"¡El héroe ha encontrado un arma!")

to_equip = input("¿Quieres equipar el arma?: ")
print(f"Te has equipado: {initial_object}")