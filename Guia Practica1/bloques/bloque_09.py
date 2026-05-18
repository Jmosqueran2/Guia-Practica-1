"""Bloque 9 — Tuplas"""
from utils import mostrar_menu, mostrar_resultado, pedir_con_marco, pedir_opcion, pausar


def ejercicio_1():
    tupla = (10,20,30,40)
    try:    tupla[0] = 99; err = "Sin error"
    except TypeError as e: err = str(e)
    mostrar_resultado("Inmutabilidad de la tupla", [
        f"Tupla: {tupla}",
        f"tupla[0] = 99  →  Error: {err}",
    ])
    pausar()


def ejercicio_2():
    a, b, *resto = (100,200,300,400)
    mostrar_resultado("Unpacking con *", [
        "Tupla : (100, 200, 300, 400)",
        f"a     = {a}", f"b     = {b}", f"resto = {resto}",
    ])
    pausar()


def ejercicio_3():
    coords = [(1,2),(3,4),(5,6),(7,8)]
    mostrar_resultado("Lista de coordenadas",
                      [f"x={x}, y={y}" for x,y in coords])
    pausar()


# ── Ejercicio extra ───────────────────────────────────────
def ejercicio_extra():
    vals = pedir_con_marco("Extra — Registro de punto GPS",
                           ["Latitud", "Longitud", "Altitud (m)"])
    try:
        lat  = float(vals[0])
        lon  = float(vals[1])
        alt  = float(vals[2]) if vals[2] else 0.0
        if not (-90 <= lat <= 90):   raise ValueError("Latitud fuera de rango (-90 a 90).")
        if not (-180 <= lon <= 180): raise ValueError("Longitud fuera de rango (-180 a 180).")
    except ValueError as e:
        mostrar_resultado("Error", [str(e)]); pausar(); return
    # Guardar como tupla inmutable
    punto = (lat, lon, alt)
    mostrar_resultado("Punto GPS (tupla inmutable)", [
        f"Coordenada : {punto}",
        f"Latitud    : {punto[0]}°",
        f"Longitud   : {punto[1]}°",
        f"Altitud    : {punto[2]} m",
        "",
        "Almacenado como tupla: no puede modificarse.",
    ])
    pausar()


def menu():
    opciones = ["Inmutabilidad de la tupla",
                "Unpacking con *",
                "Recorrer lista de coordenadas",
                "Extra — Registro de punto GPS (inventado)"]
    while True:
        mostrar_menu("BLOQUE 9 — Tuplas", opciones)
        op = pedir_opcion(0, len(opciones))
        if op == 0: break
        [ejercicio_1, ejercicio_2, ejercicio_3, ejercicio_extra][op - 1]()
