# src/lesson3_text_data.py

# Variable de texto (string)
nombre = "RyogDev"
juego = "Diario del desarrollador"

# Concatenación clásica
saludo = "Hola " + nombre + ", bienvenido a " + juego + "!"
print(saludo)

# f-string (mejor práctica)
saludo_f = f"Hola {nombre}, bienvenido a {juego}!"
print(saludo_f)

# Texto multilínea
historia = """Érase una vez...
Un dev que aprendía Python
y quería dominar Git y VS Code.
"""
print(historia)

# Métodos comunes
print("Mayúsculas:", nombre.upper())
print("Minúsculas:", nombre.lower())
print("Longitud del nombre:", len(nombre))
print("Dividir una frase:", "aprender Python es genial".split())
