# src/payday.py

"""
🎯 Objetivo

Reforzar el uso de variables numéricas.

Realizar operaciones matemáticas simples (suma y resta).

Mostrar un resultado claro con mensajes dinámicos.

📝 Contexto narrativo (RPG vibes 🪙)

Tu héroe acaba de terminar una misión y es momento de cobrar la recompensa.
Pero, como todo aventurero, también tiene que pagar impuestos 🧾 y dejar una parte en la taberna 🍻.
Tu misión es calcular cuánto oro le queda después de todo.
"""

# Declarar variables iniciales
reward_gold = int(input("¿Cuánto oro recibiste por la misión?: "))
taxes = 100
tavern_cost = 50
player_name = input("¿Cuál se su nombre querido héroe?: ")

# Calcular el oro restante después de restar impuestos y taberna.
print(f"{player_name} ha completado la misión y ha obtenido: {reward_gold} de oro.")
print(f"Tras pagar {taxes} de impuesto y {tavern_cost} en la taverna")

final_gold = reward_gold - (taxes + tavern_cost)
print(f"Oro final de {player_name}: {final_gold}")