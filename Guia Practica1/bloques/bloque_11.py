"""Bloque 11 — Conjuntos"""
from utils import mostrar_menu, mostrar_resultado, pedir_con_marco, pedir_opcion, pausar


def ejercicio_1():
    A,B = {1,2,3,4},{3,4,5,6}
    mostrar_resultado("Operaciones entre conjuntos", [
        f"A = {A}", f"B = {B}", "",
        f"Unión        A | B  = {A|B}",
        f"Intersección A & B  = {A&B}",
        f"Diferencia   A - B  = {A-B}",
        f"Dif.simétrica A ^ B = {A^B}",
    ])
    pausar()


def ejercicio_2():
    lista = [1,2,2,3,3,3,4]
    sin_dup = sorted(set(lista))
    mostrar_resultado("Eliminar duplicados con set", [
        f"Original      : {lista}",
        f"Sin duplicados: {sin_dup}",
    ])
    pausar()


def ejercicio_3():
    A,B = {1,2,3,4},{3,4,5,6}
    resultado = (A|B)-(A&B)
    mostrar_resultado("(A|B) - (A&B)", [
        f"A = {A}   B = {B}",
        f"A | B = {A|B}",
        f"A & B = {A&B}",
        f"(A|B)-(A&B) = {resultado}",
        "", f"Equivale a A ^ B = {A^B}",
    ])
    pausar()


# ── Ejercicio extra ───────────────────────────────────────
def ejercicio_extra():
    vals = pedir_con_marco("Extra — Materias en común",
                           ["Materias alumno A (separadas por coma)",
                            "Materias alumno B (separadas por coma)"])
    try:
        a_set = {m.strip() for m in vals[0].split(",") if m.strip()}
        b_set = {m.strip() for m in vals[1].split(",") if m.strip()}
        if not a_set or not b_set: raise ValueError("Ingresa al menos una materia por alumno.")
    except ValueError as e:
        mostrar_resultado("Error", [str(e)]); pausar(); return
    mostrar_resultado("Análisis de materias", [
        f"Alumno A         : {sorted(a_set)}",
        f"Alumno B         : {sorted(b_set)}",
        "",
        f"En común         : {sorted(a_set & b_set) or 'Ninguna'}",
        f"Solo alumno A    : {sorted(a_set - b_set) or 'Ninguna'}",
        f"Solo alumno B    : {sorted(b_set - a_set) or 'Ninguna'}",
        f"Total distintas  : {len(a_set | b_set)}",
    ])
    pausar()


def menu():
    opciones = ["Unión, intersección y diferencia",
                "Eliminar duplicados con set",
                "(A|B) - (A&B) — diferencia simétrica",
                "Extra — Materias en común (inventado)"]
    while True:
        mostrar_menu("BLOQUE 11 — Conjuntos (set)", opciones)
        op = pedir_opcion(0, len(opciones))
        if op == 0: break
        [ejercicio_1, ejercicio_2, ejercicio_3, ejercicio_extra][op - 1]()
