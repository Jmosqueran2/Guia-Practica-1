"""Bloque 12 — Excepciones"""
from utils import mostrar_menu, mostrar_resultado, pedir_con_marco, pedir_opcion, pausar


def ejercicio_1():
    vals = pedir_con_marco("Capturar ValueError", ["Valor a convertir a int"])
    try:
        n = int(vals[0])
        mostrar_resultado("Resultado", [f"✅ Convertido correctamente → {n}"])
    except ValueError:
        mostrar_resultado("Resultado", [f"❌ ValueError: '{vals[0]}' no es entero."])
    pausar()


def ejercicio_2():
    lista = [10,20,30]
    try:    _ = lista[5]; lineas = ["Sin error (inesperado)"]
    except IndexError as e:
        lineas = [f"Lista: {lista}  (índices 0-2)", f"❌ IndexError → {e}"]
    mostrar_resultado("Capturar IndexError", lineas)
    pausar()


def ejercicio_3():
    vals = pedir_con_marco("ValueError y ZeroDivisionError", ["Divisor (100 / x)"])
    try:
        n = int(vals[0]); r = 100 / n
        mostrar_resultado("Resultado", [f"100 / {n} = {r}"])
    except ValueError:
        mostrar_resultado("Error", [f"❌ ValueError: '{vals[0]}' no es número."])
    except ZeroDivisionError:
        mostrar_resultado("Error", ["❌ ZeroDivisionError: división por cero."])
    pausar()


# ── Ejercicio extra ───────────────────────────────────────
class SaldoInsuficienteError(Exception):
    pass

def retirar(saldo: float, monto: float) -> float:
    if monto <= 0:        raise ValueError("El monto debe ser positivo.")
    if monto > saldo:     raise SaldoInsuficienteError(f"Saldo insuficiente (disponible: ${saldo:.2f}).")
    return saldo - monto

def ejercicio_extra():
    vals = pedir_con_marco("Extra — Retiro bancario con excepciones",
                           ["Saldo actual ($)", "Monto a retirar ($)"])
    try:
        saldo = float(vals[0]); monto = float(vals[1])
        nuevo = retirar(saldo, monto)
        mostrar_resultado("Retiro exitoso", [
            f"Saldo anterior : ${saldo:.2f}",
            f"Retiro         : ${monto:.2f}",
            f"Saldo nuevo    : ${nuevo:.2f}",
        ])
    except ValueError as e:
        mostrar_resultado("ValueError", [str(e)])
    except SaldoInsuficienteError as e:
        mostrar_resultado("SaldoInsuficienteError", [str(e)])
    except Exception as e:
        mostrar_resultado("Error inesperado", [str(e)])
    pausar()


def menu():
    opciones = ["Capturar ValueError",
                "Capturar IndexError",
                "ValueError y ZeroDivisionError juntos",
                "Extra — Retiro bancario con excepciones (inventado)"]
    while True:
        mostrar_menu("BLOQUE 12 — Excepciones", opciones)
        op = pedir_opcion(0, len(opciones))
        if op == 0: break
        [ejercicio_1, ejercicio_2, ejercicio_3, ejercicio_extra][op - 1]()
