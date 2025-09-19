# src/lesson8_backpack.py

# El jugador comienza con 3 pociones con un valor de 50 de oro y 2 espadas con un valor de 120 de oro, y tiene 500 oro inicial
potions = 3
potion_price = 50
swords = 2
swords_price = 120
initial_gold = 500

# El jugador decide comprar 2 espadas

shopping_swords = initial_gold - (swords_price * 2)
swords = 4
# Transcción éxitosa
print(f"Compra éxitosa, oro restante: {shopping_swords}")

# Tus espadas se han guardado en tu mochila
print(f"El jugador acaba de comprar 2 espadas, ahora tienes {swords} espadas y {potions} pociones en tu mochila")
