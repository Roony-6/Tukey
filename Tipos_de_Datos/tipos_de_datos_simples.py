# Tipos de datos PRIMITIVOS en Python (simples/básicos)
# ----------------------------------------------------

# 1. ENTEROS (int) - Números sin decimales
edad = 25
temperatura = -10

# 2. FLOTANTES (float) - Números con decimales
pi = 3.1416
precio = 99.50

# 3. CADENAS DE TEXTO (str) - Entre comillas
nombre = "Ana"
mensaje = 'Hola, mundo'

# 4. BOOLEANOS (bool) - True o False
es_estudiante = True
tiene_descuento = False

# Mostrar los datos y sus tipos
print("=== TIPOS PRIMITIVOS ===")
print(f"Entero (int): {edad} -> {type(edad)}")
print(f"Flotante (float): {pi} -> {type(pi)}")
print(f"Texto (str): '{nombre}' -> {type(nombre)}")
print(f"Booleano (bool): {es_estudiante} -> {type(es_estudiante)}")

# Conversión entre tipos (casting)
print("\n=== CONVERSIÓN ===")
numero_texto = "123"
numero_convertido = int(numero_texto)  # str a int
print(f"'123' como entero: {numero_convertido} -> {type(numero_convertido)}")

# Ejercicio: Completa estos datos
print("\n=== EJERCICIO ===")
mi_edad = 20                   # Cambia este valor (int)
mi_peso = 65.5                 # Cambia este valor (float)
mi_nombre = "Juan"             # Cambia este valor (str)
me_gusta_python = True         # Cambia este valor (bool)

print(f"Nombre: {mi_nombre} ({type(mi_nombre)})")
print(f"Edad: {mi_edad} ({type(mi_edad)})")
print(f"Peso: {mi_peso} ({type(mi_peso)})")
print(f"¿Te gusta Python?: {me_gusta_python} ({type(me_gusta_python)})")