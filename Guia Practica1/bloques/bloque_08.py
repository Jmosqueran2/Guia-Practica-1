"""Bloque 8 — Listas"""
from utils import mostrar_menu, mostrar_resultado, pedir_con_marco, pedir_opcion, pausar


def ejercicio_1():
    lista = [5,3,8]
    for x in [12,1,7]: lista.append(x)
    mostrar_resultado("append() y sort()", [
        f"Original  : [5, 3, 8]",
        f"+ 3 elem  : {lista}",
        f"Ordenada  : {sorted(lista)}",
    ])
    pausar()


def ejercicio_2():
    nums = [5,3,8,1,9,3]
    mostrar_resultado("Suma, máximo y mínimo", [
        f"Lista  : {nums}",
        f"Suma   : {sum(nums)}",
        f"Máximo : {max(nums)}",
        f"Mínimo : {min(nums)}",
    ])
    pausar()


def ejercicio_3():
    lista=[1,2,3]; ref=lista; copia=lista.copy()
    ref.append(4)
    mostrar_resultado("Referencia vs copia", [
        f"lista      → {lista}   ← también cambió",
        f"referencia → {ref}",
        f"copia      → {copia}  ← no cambió (.copy())",
    ])
    pausar()


# ── Ejercicio extra ───────────────────────────────────────
def ejercicio_extra():
    vals = pedir_con_marco("Extra — Gestión de lista de compras",
                           ["Producto 1","Producto 2","Producto 3","Producto 4","Producto 5"])
    items = [v for v in vals if v]
    if not items:
        mostrar_resultado("Error", ["No ingresaste productos."]); pausar(); return
    items.sort()
    mostrar_resultado("Lista de compras", [
        f"Total productos : {len(items)}",
        f"Ordenados       : {items}",
        f"Primero (sort)  : {items[0]}",
        f"Último  (sort)  : {items[-1]}",
    ])
    pausar()


def menu():
    opciones = ["append() y sort()",
                "Suma, máximo y mínimo",
                "Referencia vs copia",
                "Extra — Gestión de lista de compras (inventado)"]
    while True:
        mostrar_menu("BLOQUE 8 — Listas", opciones)
        op = pedir_opcion(0, len(opciones))
        if op == 0: break
        [ejercicio_1, ejercicio_2, ejercicio_3, ejercicio_extra][op - 1]()
