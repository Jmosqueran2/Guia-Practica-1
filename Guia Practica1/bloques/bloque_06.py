"""Bloque 6 — Bucles"""
from utils import mostrar_menu, mostrar_resultado, pedir_con_marco, pedir_opcion, pausar


def ejercicio_1():
    nums = []; c = 1
    while c <= 10: nums.append(str(c)); c += 1
    mostrar_resultado("Números 1-10 con while", ["  ".join(nums)])
    pausar()


def ejercicio_2():
    frutas = ["Manzana","Pera","Uva","Mango","Fresa"]
    mostrar_resultado("Frutas con enumerate()",
                      [f"[{i}]  {f}" for i,f in enumerate(frutas)])
    pausar()


def ejercicio_3():
    pares     = [x for x in range(1,11) if x % 2 == 0]
    cuadrados = [x**2 for x in range(1,11) if x % 2 == 0]
    mostrar_resultado("Cuadrados de pares del 1 al 10", [
        f"Pares     : {pares}",
        f"Cuadrados : {cuadrados}",
    ])
    pausar()


# ── Ejercicio extra ───────────────────────────────────────
def ejercicio_extra():
    vals = pedir_con_marco("Extra — Tabla de multiplicar", ["Número (1-12)"])
    if not vals[0].strip():
        mostrar_resultado("Error", ["El campo no puede estar vacío."]); pausar(); return
    try:
        n = int(vals[0])
        if not (1 <= n <= 12): raise ValueError("Debe estar entre 1 y 12.")
    except ValueError as e:
        mostrar_resultado("Error", [f"Número inválido: {e}"]); pausar(); return
    lineas = [f"{n} x {i:>2} = {n*i:>3}" for i in range(1, 13)]
    mostrar_resultado(f"Tabla del {n}", lineas)
    pausar()


def menu():
    opciones = ["Números 1-10 con while",
                "Frutas con enumerate()",
                "Cuadrados de pares (list comprehension)",
                "Extra — Tabla de multiplicar (inventado)"]
    while True:
        mostrar_menu("BLOQUE 6 — Bucles", opciones)
        op = pedir_opcion(0, len(opciones))
        if op == 0: break
        [ejercicio_1, ejercicio_2, ejercicio_3, ejercicio_extra][op - 1]()
