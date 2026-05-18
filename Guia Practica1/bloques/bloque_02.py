"""Bloque 2 — Variables y tipos de datos"""
from utils import mostrar_menu, mostrar_resultado, pedir_con_marco, pedir_opcion, pausar


def ejercicio_1():
    mostrar_resultado("Un dato de cada tipo", [
        f"int      → {19}",
        f"float    → {3.14}",
        f"str      → {'Hola Python'}",
        f"bool     → {True}",
        f"None     → {None}",
        f"list     → {[1,2,3,'python']}",
        f"tuple    → {(1,'hello',3.14)}",
        f"dict     → {{'nombre':'Juan','edad':25}}",
        f"set      → {{1, 2, 3}}",
    ])
    pausar()


def ejercicio_2():
    lista = [10, 20, 30, 40, 50]
    mostrar_resultado("Lista de 5 elementos + slicing", [
        f"Lista completa : {lista}",
        f"Primero  [0]   : {lista[0]}",
        f"Último   [-1]  : {lista[-1]}",
        f"Slice  [1:4]   : {lista[1:4]}",
    ])
    pausar()


class DemoTipos:
    def datos(self):
        texto = "Python"
        lista = [1,2,3,4,5]
        dicc  = {"lenguaje":"Python","version":3}
        return [
            f"str  primer carácter : {texto[0]}",
            f"list último elemento : {lista[-1]}",
            f"dict valor 'version' : {dicc['version']}",
        ]

def ejercicio_3():
    mostrar_resultado("Clase con str, list y dict", DemoTipos().datos())
    pausar()


# ── Ejercicio extra ───────────────────────────────────────
def ejercicio_extra():
    vals = pedir_con_marco("Extra — Explorador de tipos", ["Ingresa cualquier valor"])
    v = vals[0]
    if not v.strip():
        mostrar_resultado("Error", ["No ingresaste ningún valor."]); pausar(); return
    for tipo, fn in [("int", int), ("float", float)]:
        try:
            fn(v); detected = tipo; break
        except ValueError:
            continue
    else:
        detected = "str"
    if v.lower() in ("true","false"): detected = "bool"
    mostrar_resultado("Explorador de tipos", [
        f"Valor ingresado : '{v}'",
        f"Tipo detectado  : {detected}",
        f"Longitud (str)  : {len(v)} caracteres",
        f"Mayúsculas      : {v.upper()}",
        f"Minúsculas      : {v.lower()}",
    ])
    pausar()


def menu():
    opciones = ["Un dato de cada tipo",
                "Lista con slicing",
                "Clase con str, list y dict",
                "Extra — Explorador de tipos (inventado)"]
    while True:
        mostrar_menu("BLOQUE 2 — Variables y tipos de datos", opciones)
        op = pedir_opcion(0, len(opciones))
        if op == 0: break
        [ejercicio_1, ejercicio_2, ejercicio_3, ejercicio_extra][op - 1]()
