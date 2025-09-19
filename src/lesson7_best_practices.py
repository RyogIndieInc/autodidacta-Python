# src/lesson7_best_practices.py

"""
Estaremos aplicando las mejores prácticas en está lección:
- Nombres descriptvos
- Snake_case
- Comentarios útiles, explicando el por qué, no el qué
- Mensajes claros en consola
- evitar repetir cálculos innecesarios
"""

# El jugador comienza con un valor fijo de energía (120) y cada ataque cuesta 30.
initial_energy = 120
attack_cost = 30

# El jugador gasta energía
remaining_energy = initial_energy - attack_cost

# Simulando batalla del jugador contra un slime
print(f"Jugador empieza con {initial_energy} energía, ataca a un slime y gasta {attack_cost} energía")
print(f"energía restante: {remaining_energy}")