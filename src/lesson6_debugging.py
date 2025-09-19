# src/lesson6_debugging.py

# debugging example syntax error
#A — SyntaxError (error de sintaxis)
def say_hello()
    print("Hola, mundo")

"""
Qué verás: SyntaxError: invalid syntax apuntando a la línea de def.
Solución: falta : después del paréntesis — añade :.
"""


# B — NameError (nombre no definido)
player = "Ryo"
print("Player:", player_name)

"""
Qué verás: NameError: name 'player_name' is not defined.
Solución: usar la variable correcta player o definir player_name.
"""


# C — TypeError (operación no válida entre tipos)
gold = "100"
gold += 50

"""
Qué verás: TypeError: can only concatenate str (not "int") to str.
Solución: convertir gold a int (gold = int(gold)) o formatear la salida.
"""


# D — IndexError (índice fuera de rango)
items = ["espada", "escudo"]
print(items[2])

"""
Qué verás: IndexError: list index out of range.
Solución: revisar índices (máximo válido es 1 aquí) o validar len().
"""

# E — ValueError (conversión inválida)
n = int("tres")

"""
Qué verás: ValueError: invalid literal for int() with base 10: 'tres'.
Solución: validar antes de convertir, o manejar con try/except más adelante.
"""