"""Bloque 3 — Operadores"""
from utils import mostrar_menu, mostrar_resultado, pedir_con_marco, pedir_opcion, pausar


def ejercicio_1():
    a, b = 20, 4
    mostrar_resultado("Operadores aritméticos  (a=20, b=4)", [
        f"{a} +  {b}  =  {a+b}   (suma)",
        f"{a} -  {b}  =  {a-b}   (resta)",
        f"{a} *  {b}  =  {a*b}   (multiplicación)",
        f"{a} /  {b}  =  {a/b}   (división)",
        f"{a} // {b}  =  {a//b}   (división entera)",
        f"{a} %  {b}  =  {a%b}    (módulo)",
        f"{a} ** {b}  =  {a**b}  (potencia)",
    ])
    pausar()


def ejercicio_2():
    a=[1,2]; b=[1,2]; c=a
    mostrar_resultado("== vs is", [
        "a = [1,2]   b = [1,2]   c = a",
        "",
        f"a == b  →  {a==b}   (mismo contenido)",
        f"a is b  →  {a is b}  (diferente objeto en memoria)",
        f"a is c  →  {a is c}   (misma referencia)",
    ])
    pausar()


def ejercicio_3():
    x = 2 + 1 * 2 % 2 + (2**1)//2
    mostrar_resultado("Precedencia:  2 + 1*2%2 + (2**1)//2", [
        "Paso 1: 2**1       = 2",
        "Paso 2: 1 * 2      = 2",
        "Paso 3: 2 % 2      = 0",
        "Paso 4: (2**1)//2  = 1",
        "Paso 5: 2 + 0 + 1  = 3",
        "", f"Resultado final  →  {x}",
    ])
    pausar()


# ── Ejercicio extra ───────────────────────────────────────
def ejercicio_extra():
    vals = pedir_con_marco("Extra — Calculadora de operadores", ["Número A", "Número B"])
    try:
        a = float(vals[0]); b = float(vals[1])
    except ValueError:
        mostrar_resultado("Error", ["Ingresa números válidos."]); pausar(); return
    lineas = [
        f"{a} +  {b}  =  {a+b}",
        f"{a} -  {b}  =  {a-b}",
        f"{a} *  {b}  =  {a*b}",
        f"{a} /  {b}  =  {a/b:.4f}" if b != 0 else f"{a} /  {b}  =  División por cero",
        f"{a} ** {b}  =  {a**b}",
        f"{a} == {b}  →  {a==b}",
        f"{a} >  {b}  →  {a>b}",
        f"{a} <  {b}  →  {a<b}",
    ]
    mostrar_resultado(f"Operadores: A={a}  B={b}", lineas)
    pausar()


def menu():
    opciones = ["Operadores aritméticos (a=20, b=4)",
                "Demostración: == vs is",
                "Precedencia de operadores",
                "Extra — Calculadora de operadores (inventado)"]
    while True:
        mostrar_menu("BLOQUE 3 — Operadores", opciones)
        op = pedir_opcion(0, len(opciones))
        if op == 0: break
        [ejercicio_1, ejercicio_2, ejercicio_3, ejercicio_extra][op - 1]()
