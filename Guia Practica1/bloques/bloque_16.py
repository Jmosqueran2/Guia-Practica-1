"""Bloque 16 — Archivos y JSON"""
import json, os, tempfile
from utils import mostrar_menu, mostrar_resultado, pedir_con_marco, pedir_opcion, pausar

TMP = tempfile.gettempdir()

def ejercicio_1():
    ruta = os.path.join(TMP, "poo_texto.txt")
    with open(ruta,"w") as f:
        f.write("Python\n"); f.write("Programación Orientada a Objetos\n")
    with open(ruta,"r") as f:
        lineas = [l.strip() for l in f.readlines()]
    mostrar_resultado("Escribir y leer archivo .txt", [
        f"Archivo : {ruta}", "",
        "── Contenido leído ──",
    ] + lineas)
    pausar()


def ejercicio_2():
    ruta = os.path.join(TMP, "poo_datos.json")
    datos = {"x":10,"y":20}
    with open(ruta,"w") as f: json.dump(datos,f,indent=2)
    with open(ruta,"r") as f: cargado = json.load(f)
    mostrar_resultado("Guardar y cargar dict en JSON", [
        f"Guardado → {datos}",
        f"Cargado  → {cargado}",
    ])
    pausar()


def ejercicio_3():
    ruta = os.path.join(TMP, "poo_usuarios.json")
    usuarios = [{"nombre":"Ana","edad":20},{"nombre":"Luis","edad":30}]
    with open(ruta,"w") as f: json.dump(usuarios,f,indent=2)
    with open(ruta,"r") as f: data = json.load(f)
    mostrar_resultado("Lista de usuarios en JSON",
                      [f"→ {u['nombre']}, {u['edad']} años" for u in data])
    pausar()


# ── Ejercicio extra ───────────────────────────────────────
def ejercicio_extra():
    vals = pedir_con_marco("Extra — Guardar inventario en JSON",
                           ["Producto", "Cantidad", "Precio unitario ($)"])
    if not vals[0]:
        mostrar_resultado("Error", ["El producto es obligatorio."]); pausar(); return
    try:
        qty   = int(vals[1])   if vals[1] else 0
        price = float(vals[2]) if vals[2] else 0.0
        if qty < 0 or price < 0: raise ValueError("Valores negativos.")
    except ValueError as e:
        mostrar_resultado("Error", [str(e)]); pausar(); return

    ruta = os.path.join(TMP, "poo_inventario.json")
    # Cargar existente o empezar vacío
    try:
        with open(ruta,"r") as f: inventario = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        inventario = []

    inventario.append({"producto": vals[0], "cantidad": qty, "precio": price})
    with open(ruta,"w") as f: json.dump(inventario, f, indent=2)

    total_items = sum(i["cantidad"] for i in inventario)
    mostrar_resultado("Inventario actualizado", [
        f"Producto guardado : {vals[0]}",
        f"Cantidad          : {qty}",
        f"Precio            : ${price:.2f}",
        f"Total en archivo  : {len(inventario)} producto(s)",
        f"Unidades totales  : {total_items}",
        f"Archivo           : {ruta}",
    ])
    pausar()


def menu():
    opciones = ["Escribir y leer archivo de texto",
                "Guardar y cargar dict en JSON",
                "Lista de usuarios en JSON",
                "Extra — Guardar inventario en JSON (inventado)"]
    while True:
        mostrar_menu("BLOQUE 16 — Archivos y JSON", opciones)
        op = pedir_opcion(0, len(opciones))
        if op == 0: break
        [ejercicio_1, ejercicio_2, ejercicio_3, ejercicio_extra][op - 1]()
