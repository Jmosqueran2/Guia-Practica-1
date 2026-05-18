"""Bloque 7 — Funciones"""
from utils import mostrar_menu, mostrar_resultado, pedir_con_marco, pedir_opcion, pausar


def doble(x): return x * 2

def ejercicio_1():
    vals = pedir_con_marco("Función doble(x)", ["Número"])
    try:
        x = float(vals[0])
    except ValueError:
        mostrar_resultado("Error", ["Número inválido."]); pausar(); return
    mostrar_resultado("Resultado", [f"doble({x}) = {doble(x)}"])
    pausar()


def sumar_varios(*nums): return sum(nums)

def ejercicio_2():
    nums = [1,2,3,4,5]
    mostrar_resultado("Suma con *args", [
        f"Lista          : {nums}",
        f"sumar_varios() : {sumar_varios(*nums)}",
    ])
    pausar()


def factorial(n):
    if n < 0: raise ValueError("No existe factorial negativo.")
    if n == 0: return 1
    return n * factorial(n - 1)

def ejercicio_3():
    vals = pedir_con_marco("Factorial recursivo", ["n (entero ≥ 0)"])
    try:
        n = int(vals[0])
        if n < 0: raise ValueError
    except ValueError:
        mostrar_resultado("Error", ["Ingresa entero no negativo."]); pausar(); return
    mostrar_resultado("Resultado", [f"factorial({n}) = {factorial(n)}"])
    pausar()


# ── Ejercicio extra ───────────────────────────────────────
def es_primo(n: int) -> bool:
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True

def primos_hasta(limite: int) -> list:
    return [n for n in range(2, limite + 1) if es_primo(n)]

def ejercicio_extra():
    vals = pedir_con_marco("Extra — Números primos", ["Límite (1-200)"])
    try:
        limite = int(vals[0])
        if not (1 <= limite <= 200): raise ValueError
    except ValueError:
        mostrar_resultado("Error", ["Ingresa un número entre 1 y 200."]); pausar(); return
    primos = primos_hasta(limite)
    mostrar_resultado(f"Primos hasta {limite}", [
        f"Cantidad : {len(primos)}",
        f"Lista    : {primos}",
    ])
    pausar()


def menu():
    opciones = ["Función doble(x)",
                "Suma con *args",
                "Factorial recursivo",
                "Extra — Números primos (inventado)"]
    while True:
        mostrar_menu("BLOQUE 7 — Funciones", opciones)
        op = pedir_opcion(0, len(opciones))
        if op == 0: break
        [ejercicio_1, ejercicio_2, ejercicio_3, ejercicio_extra][op - 1]()
