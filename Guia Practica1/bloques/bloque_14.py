"""Bloque 14 — Unpacking"""
from utils import mostrar_menu, mostrar_resultado, pedir_con_marco, pedir_opcion, pausar


def ejercicio_1():
    primera, *mitad, ultima = (10,20,30,40)
    mostrar_resultado("Unpacking: primera, *mitad, ultima", [
        "Tupla    : (10, 20, 30, 40)",
        f"primera  = {primera}",
        f"mitad    = {mitad}",
        f"ultima   = {ultima}",
    ])
    pausar()


def multiplicar(a,b,c): return a*b*c

def ejercicio_2():
    lista = [2,3,4]
    mostrar_resultado("Pasar lista como args con *", [
        f"lista = {lista}",
        f"multiplicar(*lista) = {multiplicar(*lista)}",
    ])
    pausar()


def ejercicio_3():
    d1={"a":1,"b":2}; d2={"c":3,"d":4}
    combinado={**d1,**d2}
    mostrar_resultado("Combinar dicts con **", [
        f"d1        = {d1}",
        f"d2        = {d2}",
        f"combinado = {combinado}",
        f"d1 orig.  = {d1}  (sin cambios)",
    ])
    pausar()


# ── Ejercicio extra ───────────────────────────────────────
def ejercicio_extra():
    vals = pedir_con_marco("Extra — Desempaquetar resultado de función",
                           ["Número A", "Número B", "Número C"])
    try:
        nums = [float(v) for v in vals if v]
        if len(nums) < 2: raise ValueError("Ingresa al menos 2 números.")
    except ValueError as e:
        mostrar_resultado("Error", [str(e)]); pausar(); return

    def estadisticas(*valores):
        return min(valores), max(valores), sum(valores)/len(valores)

    minimo, maximo, promedio = estadisticas(*nums)
    primero, *resto = nums
    mostrar_resultado("Unpacking de estadísticas", [
        f"Números ingresados : {nums}",
        "",
        "── estadisticas(*nums) devuelve tupla ──",
        f"minimo, maximo, promedio = estadisticas(*nums)",
        f"minimo   = {minimo}",
        f"maximo   = {maximo}",
        f"promedio = {promedio:.2f}",
        "",
        f"primero, *resto = {primero}, {resto}",
    ])
    pausar()


def menu():
    opciones = ["Unpacking con * (primera, mitad, ultima)",
                "Pasar lista como args con *",
                "Combinar dicts con **",
                "Extra — Desempaquetar resultado de función (inventado)"]
    while True:
        mostrar_menu("BLOQUE 14 — Unpacking", opciones)
        op = pedir_opcion(0, len(opciones))
        if op == 0: break
        [ejercicio_1, ejercicio_2, ejercicio_3, ejercicio_extra][op - 1]()
