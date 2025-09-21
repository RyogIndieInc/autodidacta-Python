# src/chatbot_v1.py

"""
🎯 Objetivo

Reforzar el uso de entradas (input()) y salidas (print()).

Crear un flujo conversacional básico.

Practicar con texto dinámico en base a las respuestas del usuario.

📝 Contexto narrativo (RPG vibes 🤖✨)

Tu héroe llega a la taberna y se encuentra con un extraño ser mecánico llamado ChatBot 🤖.
Este bot hace preguntas simples al héroe y responde de manera básica según lo que el jugador conteste.
"""

# Simular una conversación simple
print("🤖¡Bienvenido!, soy ChatBot 1.0. ¡Encantado de conocerte!")

username = input("Podrías decirme tu nombre: ")
print(f"🤖Hola, {username}, ¿Cómo te sientes hoy?")

mood = input("¿Cuál es tu estado de animo?: ")
print(f"🤖 ¡Guau!, te sientes {mood} {username}")

print(f"🤖 {username}, ¿Te gustaría que te dé un consejo?")

advice = input("Si / No: ")
print(f"{username}, Si Luffy puede ser serio cuando entrena, pero divertido cuando habla, tú también puedes serlo, ¡Ánimo!.")

print(f"¡Que tengas una gran aventura, {username}!")