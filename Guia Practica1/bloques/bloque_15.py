"""Bloque 15 — Funciones de orden superior"""
from functools import reduce
from utils import mostrar_menu, mostrar_resultado, pedir_con_marco, pedir_opcion, pausar


def ejercicio_1():
    nums = [2,4,6]
    mostrar_resultado("map() — incrementar en 1", [
        f"Original  : {nums}",
        f"map(+1)   : {list(map(lambda x: x+1, nums))}",
    ])
    pausar()


def ejercicio_2():
    nums = [1,2,3,4,5]
    mostrar_resultado("filter() — mayores a 3", [
        f"Original      : {nums}",
        f"filter(>3)    : {list(filter(lambda x: x>3, nums))}",
    ])
    pausar()


def ejercicio_3():
    nums = [1,2,3,4]
    mostrar_resultado("reduce() — producto total", [
        f"Lista        : {nums}",
        f"reduce(*)    : {reduce(lambda x,y: x*y, nums)}",
        f"Proceso: 1×2=2 → 2×3=6 → 6×4=24",
    ])
    pausar()


# ── Ejercicio extra ───────────────────────────────────────
def ejercicio_extra():
    vals = pedir_con_marco("Extra — Pipeline de transformaciones",
                           ["Números separados por coma"])
    try:
        nums = [float(x.strip()) for x in vals[0].split(",") if x.strip()]
        if not nums: raise ValueError("Sin números.")
    except ValueError as e:
        mostrar_resultado("Error", [str(e) if str(e) != "could not convert string to float: ''" else "Ingresa números separados por coma."])
        pausar(); return

    solo_pos   = list(filter(lambda x: x > 0, nums))
    duplicados = list(map(lambda x: x * 2, solo_pos))
    total      = reduce(lambda x,y: x+y, duplicados) if duplicados else 0

    mostrar_resultado("Pipeline: filter → map → reduce", [
        f"Entrada          : {nums}",
        f"1. filter(>0)    : {solo_pos}",
        f"2. map(x2)       : {duplicados}",
        f"3. reduce(suma)  : {total}",
    ])
    pausar()


def menu():
    opciones = ["map() — incrementar lista",
                "filter() — mayores a 3",
                "reduce() — producto total",
                "Extra — Pipeline de transformaciones (inventado)"]
    while True:
        mostrar_menu("BLOQUE 15 — Funciones de orden superior", opciones)
        op = pedir_opcion(0, len(opciones))
        if op == 0: break
        [ejercicio_1, ejercicio_2, ejercicio_3, ejercicio_extra][op - 1]()
