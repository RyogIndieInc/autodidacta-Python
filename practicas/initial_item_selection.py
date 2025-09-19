# practicas/initial_item_selection.py

# Imagina que tu jugador llega al inicio de la aventura y debe elegir un objeto inicial.

print("\n🌟 ¡Bienvenido, valiente aventurero! 🌟")
username = input("🗣️ ¿Cuál es tu nombre, héroe?: ")

# Convertimos a entero porque el nivel siempre será un número
initial_level = int(input("📈 ¿Cuál es tu nivel inicial?: "))

print("\n🎒 Elige tu objeto inicial:")
print("\t1️⃣ Espada 🗡️")
print("\t2️⃣ Escudo 🛡️")
print("\t3️⃣ Poción 🧪")

item_choice = int(input("👉 Escribe el número de tu elección: "))

print("\n⚔️ Preparando tu equipo...")
print(f"🧍 El jugador {username} comienza con nivel {initial_level}.")
print(f"🔢 Has elegido el objeto número {item_choice} - Espada 🗡️")
print(f"🔢 Has elegido el objeto número {item_choice} - Escudo 🛡️")
print(f"🔢 Has elegido el objeto número {item_choice} - Poción 🧪")
print("🚀 ¡Que comience la aventura, héroe!")