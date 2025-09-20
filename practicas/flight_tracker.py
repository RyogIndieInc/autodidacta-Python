# practicas/flight_tracker.py

"""
🎯 Objetivo

Reforzar el uso de variables para almacenar información.

Empezar a combinar texto con datos dinámicos.

Practicar cómo un programa puede mostrar un reporte simple.

📝 Contexto narrativo (RPG vibes + toque realista)

Imagina que eres el encargado de anunciar los vuelos de un puerto aéreo mágico 🧙‍♂️✈️.
Tu programa mostrará información de un vuelo: aerolínea, número, ciudad de salida, ciudad de llegada y estado.
"""

airline = input("nombre de tu aerolínea: ")
flight_number = int(input("¿Cuál es el número de vuelo?: "))
departure_city = input("¿Cuál es la ciudad de salida?: ")
arrival_city = input("¿Cuál es la ciudad de llegada?: ")
status = input("Estado del vuelo (En horario / cancelado o retrasado): ")

print("\n ✈️ Rastreador de vuelos ✈️")
print(f"\n\t✈️ Vuelo N° {flight_number} | {airline}")
print(f"\tDe: {departure_city} → A: {arrival_city}")
print(f"\tEstado: {status}")

# Si el usuario elige retrasado, tomar en consideración este print()
print(f"\n ⚠️ Atención pasajeros: el vuelo sufrirá una demora.")