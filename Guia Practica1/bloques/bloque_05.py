"""Bloque 5 — Condicionales"""
from utils import mostrar_menu, mostrar_resultado, pedir_con_marco, pedir_opcion, pausar


def ejercicio_1():
    vals = pedir_con_marco("Par o impar", ["Número entero"])
    try:
        n = int(vals[0])
    except ValueError:
        mostrar_resultado("Error", ["No es un entero válido."]); pausar(); return
    mostrar_resultado("Resultado", [f"{n} es {'Par' if n % 2 == 0 else 'Impar'}."])
    pausar()


def ejercicio_2():
    vals = pedir_con_marco("Calificación por nota", ["Nota (0-100)"])
    try:
        nota = float(vals[0])
        if not (0 <= nota <= 100): raise ValueError
    except ValueError:
        mostrar_resultado("Error", ["Nota inválida (0-100)."]); pausar(); return
    letra = "A" if nota >= 90 else "B" if nota >= 80 else "C" if nota >= 70 else "D"
    mostrar_resultado("Resultado", [f"Nota: {nota}  →  Calificación: {letra}"])
    pausar()


def ejercicio_3():
    vals = pedir_con_marco("Sistema de Login", ["Usuario", "Contraseña"])
    if vals[0] == "admin" and vals[1] == "123":
        mostrar_resultado("Acceso", ["✅ Bienvenido, admin!"])
    else:
        mostrar_resultado("Acceso", ["❌ Acceso denegado."])
    pausar()


# ── Ejercicio extra ───────────────────────────────────────
def ejercicio_extra():
    vals = pedir_con_marco("Extra — Clasificador de temperatura",
                           ["Temperatura (°C)"])
    try:
        t = float(vals[0])
    except ValueError:
        mostrar_resultado("Error", ["Temperatura inválida."]); pausar(); return
    if   t <= 0:   cat, emoji = "Congelante", "🥶"
    elif t <= 10:  cat, emoji = "Muy frío",   "🧥"
    elif t <= 20:  cat, emoji = "Fresco",     "😊"
    elif t <= 30:  cat, emoji = "Agradable",  "☀️"
    elif t <= 40:  cat, emoji = "Caluroso",   "🌡️"
    else:          cat, emoji = "Extremo",    "🔥"
    mostrar_resultado("Clasificación de temperatura", [
        f"Temperatura : {t}°C",
        f"Categoría   : {emoji} {cat}",
    ])
    pausar()


def menu():
    opciones = ["Par o impar",
                "Calificación por nota",
                "Sistema de login",
                "Extra — Clasificador de temperatura (inventado)"]
    while True:
        mostrar_menu("BLOQUE 5 — Condicionales", opciones)
        op = pedir_opcion(0, len(opciones))
        if op == 0: break
        [ejercicio_1, ejercicio_2, ejercicio_3, ejercicio_extra][op - 1]()
