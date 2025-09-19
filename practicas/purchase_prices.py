# practice purchase_prices.py

# Purchase prices: simula una compra en la que el jugador compra 2 pociones y el oro se descuenta.

potion_price = 50 # Precio de una poción
initial_gold = 200 # Oro inicial del jugador
potion_quantity = 2 # Cantidad de pociones a comprar
username = "RyogDev" # Nombre del jugador

# Cálculo del costo total de las pociones

total_cost = potion_price * potion_quantity # Costo total de las pociones
remaining_gold = initial_gold - total_cost # Oro restante después de la compra

# Mensaje de resultado
print(f"{username} ha comprado {potion_quantity} pociones por {total_cost} de oro.")

print(f"Oro restante: {remaining_gold}")