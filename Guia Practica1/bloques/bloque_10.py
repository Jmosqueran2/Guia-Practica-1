"""Bloque 10 — Diccionarios"""
from utils import mostrar_menu, mostrar_resultado, pedir_con_marco, pedir_opcion, pausar


def ejercicio_1():
    p = {"nombre":"Juan","edad":25,"ciudad":"Guayaquil"}
    mostrar_resultado("Acceso con [] y get()", [
        f"['nombre']             = {p['nombre']}",
        f".get('edad')           = {p.get('edad')}",
        f".get('telefono','N/A') = {p.get('telefono','N/A')}",
    ])
    pausar()


def ejercicio_2():
    p = {"nombre":"Juan","edad":25,"ciudad":"Guayaquil"}
    mostrar_resultado("Iterar con items()",
                      [f"{k:<12} → {v}" for k,v in p.items()])
    pausar()


def ejercicio_3():
    datos={"a":1}; ref=datos; copia=datos.copy()
    ref["b"] = 2
    mostrar_resultado("Referencia vs copia en dict", [
        f"datos      → {datos}   ← también cambió",
        f"referencia → {ref}",
        f"copia      → {copia}  ← intacta (.copy())",
    ])
    pausar()


# ── Ejercicio extra ───────────────────────────────────────
def ejercicio_extra():
    vals = pedir_con_marco("Extra — Agenda de contacto",
                           ["Nombre", "Teléfono", "Email", "Ciudad"])
    if not vals[0].strip():
        mostrar_resultado("Error", ["El nombre es obligatorio."]); pausar(); return
    telefono = vals[1].strip()
    if telefono and not telefono.replace("+","").replace("-","").replace(" ","").isdigit():
        mostrar_resultado("Error", ["Teléfono inválido: solo dígitos, +, - y espacios."]); pausar(); return
    email = vals[2].strip()
    if email and ("@" not in email or "." not in email.split("@")[-1]):
        mostrar_resultado("Error", ["Email inválido: debe contener @ y dominio."]); pausar(); return
    contacto = {
        "nombre":   vals[0].strip(),
        "telefono": telefono if telefono else "N/A",
        "email":    email    if email    else "N/A",
        "ciudad":   vals[3].strip() if vals[3].strip() else "N/A",
    }
    mostrar_resultado("Contacto guardado", [
        f"{k:<12} : {v}" for k,v in contacto.items()
    ] + ["", f"Claves  : {list(contacto.keys())}",
              f"Valores : {list(contacto.values())}"])
    pausar()


def menu():
    opciones = ["Acceso con [] y get()",
                "Iterar con items()",
                "Referencia vs copia en dict",
                "Extra — Agenda de contacto (inventado)"]
    while True:
        mostrar_menu("BLOQUE 10 — Diccionarios", opciones)
        op = pedir_opcion(0, len(opciones))
        if op == 0: break
        [ejercicio_1, ejercicio_2, ejercicio_3, ejercicio_extra][op - 1]()
