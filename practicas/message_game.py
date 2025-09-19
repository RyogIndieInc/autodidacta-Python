# practiecs/message_game.py

# Mensaje del juego: escribe un programa que muestre un mensaje de bienvenida con el nombre del jugador y su nivel inicial.

# Usaré dos métodos de imprimir el mensaje del juego.

# Método 1: almacenando el mensaje en una variable

username = "RyogDev"
initial_level = 1
welcome_message = f"Welcome to game, {username}! You are starting at level {initial_level}."
print(welcome_message)

# Método 2: imprimiendo directamente el mensaje

print(f"Welcome to game, {username}! You are starting at level {initial_level}.")

"""
Ambos métodos producen el mismo resultado, pero el primero es útil si el mensaje necesita ser reutilizado o modificado más adelante. De igual manera, el segundo método es más directo y conciso para mensajes simples. La decisión final es tuya.
"""