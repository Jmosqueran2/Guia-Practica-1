"""Bloque 4 — Entrada y salida"""
from utils import mostrar_menu, mostrar_resultado, pedir_con_marco, pedir_opcion, pausar


def ejercicio_1():
    vals = pedir_con_marco("Nombre y edad con f-string", ["Nombre", "Edad"])
    nombre = vals[0] if vals[0] else "Desconocido"
    try:
        edad = int(vals[1])
        if edad < 0: raise ValueError
    except ValueError:
        edad = 0
    mostrar_resultado("Resultado", [f"Hola, {nombre}! Tienes {edad} años."])
    pausar()


def ejercicio_2():
    vals = pedir_con_marco("Suma y promedio", ["Número 1", "Número 2"])
    try:
        n1 = float(vals[0]); n2 = float(vals[1])
    except ValueError:
        mostrar_resultado("Error", ["Debes ingresar números válidos."]); pausar(); return
    mostrar_resultado("Resultado", [
        f"Suma     →  {n1 + n2}",
        f"Promedio →  {(n1 + n2) / 2:.2f}",
    ])
    pausar()


def ejercicio_3():
    vals = pedir_con_marco("Concatenación sin casting", ["Ingresa un número"])
    valor = vals[0]
    mostrar_resultado("Resultado", [
        f"'{valor}' + '5'  =  '{valor + '5'}'",
        "",
        "Se concatenan como texto, no se suman.",
    ])
    pausar()


# ── Ejercicio extra ───────────────────────────────────────
def ejercicio_extra():
    vals = pedir_con_marco("Extra — Ficha personal completa",
                           ["Nombre", "Apellido", "Ciudad", "Profesión"])
    nombre, apellido, ciudad, prof = vals
    if not nombre: nombre = "N/A"
    if not apellido: apellido = "N/A"
    mostrar_resultado("Ficha Personal", [
        f"Nombre completo : {nombre} {apellido}",
        f"Ciudad          : {ciudad if ciudad else 'N/A'}",
        f"Profesión       : {prof if prof else 'N/A'}",
        "",
        f"Iniciales       : {nombre[0].upper()}.{apellido[0].upper()}." if nombre != 'N/A' and apellido != 'N/A' else "Iniciales: N/A",
    ])
    pausar()


def menu():
    opciones = ["Nombre y edad con f-string",
                "Suma y promedio de dos números",
                "Concatenación sin casting",
                "Extra — Ficha personal completa (inventado)"]
    while True:
        mostrar_menu("BLOQUE 4 — Entrada y salida", opciones)
        op = pedir_opcion(0, len(opciones))
        if op == 0: break
        [ejercicio_1, ejercicio_2, ejercicio_3, ejercicio_extra][op - 1]()
