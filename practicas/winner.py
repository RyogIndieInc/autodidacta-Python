# practicas/winner.py

"""
🎯 Objetivo de la práctica

Aprender a almacenar valores en variables.

Usar esos valores para mostrar resultados dinámicos.

Empezar a ver cómo un programa puede procesar texto y números para llegar a un desenlace.

📝 Contexto narrativo (RPG vibes)

Imagina que estás en un torneo de héroes. Dos jugadores se enfrentan y tú eres el juez del combate. Tu misión es anunciar al ganador según los puntos que tengan.
"""

# Le pediremos al usuario el nombre de los jugadores
player1 = input("¿Cómo se llama el jugador 1?: ")
player2 = input("¿Cómo se llama el jugador 2?: ")

# Le pediremos al usuario los puntos de cada jugaro
score1 = int(input(f"Puntuación de {player1}: "))
score2 = int(input(f"Puntuación de {player2}: "))

# Imprimiremos el nombre y puntuación de cada jugador dado por el usuario
print(f"El jugador {player1}, obtuvo {score1} puntos.")
print(f"El jugador {player2}, obtuvo {score2} puntos.")

# Mostramos ambos mensajes para que el usuario decida
print("🏆 El ganador es: ________")
print("🤝 Es un empate")