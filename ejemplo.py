# --- EJEMPLOS DE FUNCIONES (Retornan un valor) ---

def sumar(a, b):
    return a + b

def es_par(numero):
    return numero % 2 == 0

def calcular_area_circulo(radio):
    pi = 3.14159
    return pi * (radio ** 2)

def obtener_saludo(nombre):
    return f"¡Hola, {nombre}! Bienvenido al curso."

def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32


# --- EJEMPLOS DE PROCEDIMIENTOS (No retornan valor, realizan una acción) ---

def mostrar_bienvenida():
    print("==================================")
    print("  SISTEMA DE EJEMPLOS PYTHON      ")
    print("==================================")

def mostrar_datos_usuario(nombre, edad):
    print(f"Usuario: {nombre}")
    print(f"Edad: {edad} años")

def dibujar_linea(longitud):
    print("-" * longitud)

def listar_frutas():
    frutas = ["Manzana", "Banana", "Cereza"]
    print("Lista de frutas:")
    for fruta in frutas:
        print(f"- {fruta}")

def despedida():
    print("¡Gracias por usar el programa! Hasta pronto.")

# Funciones:

print("=== EJECUCIÓN DE LAS 5 FUNCIONES ===")

print(f"1. Suma (10 + 5): {sumar(10, 5)}")

print(f"2. ¿Es 10 par?: {es_par(10)}")

print(f"3. Area de un circulo con radio 5: {calcular_area_circulo(5)}")

print(f"4. Saludo: {obtener_saludo('Nyls')}")

print(f"5. 25°C en Fahrenheit es: {celsius_a_fahrenheit(25)}°F")

print("\n" + "="*40 + "\n")

# Procedimientos:

print("=== EJECUCIÓN DE LOS 5 PROCEDIMIENTOS ===")

mostrar_bienvenida()

mostrar_datos_usuario("Nyls", 19)

dibujar_linea(34)

listar_frutas()

despedida()