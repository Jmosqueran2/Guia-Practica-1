"""Bloque 13 — Decoradores"""
from utils import mostrar_menu, mostrar_resultado, pedir_con_marco, pedir_opcion, pausar
import time


def iniciando(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@iniciando
def saludar(nombre): return f"Hola, {nombre}! (decorador @iniciando aplicado)"

def ejercicio_1():
    vals = pedir_con_marco("Decorador @iniciando", ["Nombre"])
    nombre = vals[0] if vals[0] else "Mundo"
    mostrar_resultado("Resultado", [
        "Decorador ejecutado antes de la función.",
        saludar(nombre),
    ])
    pausar()


def solo_positivo(func):
    def wrapper(x):
        if x <= 0: return None
        return func(x)
    return wrapper

@solo_positivo
def cuadrado(x): return x ** 2

def ejercicio_2():
    vals = pedir_con_marco("Decorador @solo_positivo", ["Número"])
    try:
        x = float(vals[0])
    except ValueError:
        mostrar_resultado("Error", ["No es un número."]); pausar(); return
    r = cuadrado(x)
    if r is None:
        mostrar_resultado("Resultado", [f"❌ {x} no es positivo — rechazado por decorador."])
    else:
        mostrar_resultado("Resultado", [f"cuadrado({x}) = {r}"])
    pausar()


def log(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@log
def suma(a, b): return a + b

def ejercicio_3():
    mostrar_resultado("@log → suma(2, 3)", [
        "El decorador @log intercepta la llamada.",
        "Registra: 'Llamando función suma...'",
        f"Resultado: suma(2, 3) = {suma(2, 3)}",
    ])
    pausar()


# ── Ejercicio extra ───────────────────────────────────────
_log_llamadas = []

def registrar(func):
    """Decorador que registra cada llamada con timestamp."""
    def wrapper(*args, **kwargs):
        ts = time.strftime("%H:%M:%S")
        resultado = func(*args, **kwargs)
        _log_llamadas.append(f"[{ts}] {func.__name__}({', '.join(str(a) for a in args)}) → {resultado}")
        return resultado
    return wrapper

@registrar
def area_rectangulo(base, altura):
    if base <= 0 or altura <= 0: raise ValueError("Dimensiones deben ser positivas.")
    return base * altura

@registrar
def perimetro_rectangulo(base, altura):
    if base <= 0 or altura <= 0: raise ValueError("Dimensiones deben ser positivas.")
    return 2 * (base + altura)

def ejercicio_extra():
    vals = pedir_con_marco("Extra — Decorador @registrar con geometría",
                           ["Base del rectángulo", "Altura del rectángulo"])
    try:
        b = float(vals[0]); h = float(vals[1])
        a = area_rectangulo(b, h)
        p = perimetro_rectangulo(b, h)
    except ValueError as e:
        mostrar_resultado("Error", [str(e)]); pausar(); return
    mostrar_resultado("Resultado + Log de llamadas", [
        f"Área       : {a}",
        f"Perímetro  : {p}",
        "",
        "── Registro de llamadas ──",
    ] + _log_llamadas[-4:])
    pausar()


def menu():
    opciones = ["Decorador @iniciando",
                "Decorador @solo_positivo",
                "Análisis de @log con suma(2,3)",
                "Extra — Decorador @registrar (inventado)"]
    while True:
        mostrar_menu("BLOQUE 13 — Decoradores", opciones)
        op = pedir_opcion(0, len(opciones))
        if op == 0: break
        [ejercicio_1, ejercicio_2, ejercicio_3, ejercicio_extra][op - 1]()
