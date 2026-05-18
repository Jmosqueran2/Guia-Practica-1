"""Bloque 1 — El constructor __init__"""
from utils import mostrar_menu, mostrar_resultado, pedir_con_marco, pedir_opcion, pausar


class Producto:
    def __init__(self, codigo: str, nombre: str, precio: float):
        if not codigo: raise ValueError("Código vacío.")
        if not nombre: raise ValueError("Nombre vacío.")
        if precio < 0: raise ValueError("El precio no puede ser negativo.")
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
    def __str__(self):
        return f"[{self.codigo}] {self.nombre} — ${self.precio:.2f}"

def ejercicio_1():
    mostrar_resultado("Clase Producto — 2 instancias", [
        str(Producto("P001","Laptop",900.0)),
        str(Producto("P002","Mouse", 25.0)),
    ])
    pausar()

def ejercicio_2():
    lineas = []
    try:    Producto("P003","Teclado",-10)
    except ValueError as e: lineas.append(f"Error capturado → {e}")
    lineas.append(f"Producto válido  → {Producto('P003','Teclado',45.0)}")
    mostrar_resultado("Validación: precio no negativo", lineas)
    pausar()


class Estudiante:
    def __init__(self, nombre: str, notas=None):
        if not nombre: raise ValueError("Nombre vacío.")
        self.nombre = nombre
        self.notas  = notas if notas is not None else []

    @classmethod
    def desde_diccionario(cls, datos: dict):
        return cls(datos["nombre"], datos.get("notas"))

    def __str__(self):
        return f"Estudiante('{self.nombre}', notas={self.notas})"

def ejercicio_3():
    mostrar_resultado("Estudiante con notas opcionales", [
        str(Estudiante("María")),
        str(Estudiante("Pedro", [8,9,10])),
    ])
    pausar()

def ejercicio_4():
    datos = {"nombre": "Laura", "notas": [7,8,9]}
    e = Estudiante.desde_diccionario(datos)
    mostrar_resultado("@classmethod desde_diccionario", [
        f"Dict  → {datos}", f"Obj   → {e}",
    ])
    pausar()


# ── Ejercicio extra ───────────────────────────────────────
class CuentaBancaria:
    def __init__(self, titular: str, saldo: float = 0.0):
        if not titular:  raise ValueError("Titular vacío.")
        if saldo < 0:    raise ValueError("Saldo inicial negativo.")
        self.titular = titular
        self.saldo   = saldo
    def __str__(self):
        return f"Cuenta({self.titular}) saldo=${self.saldo:.2f}"

def ejercicio_extra():
    vals = pedir_con_marco("Extra — Cuenta Bancaria", ["Titular", "Saldo inicial"])
    try:
        cb = CuentaBancaria(vals[0], float(vals[1]) if vals[1] else 0.0)
        mostrar_resultado("Cuenta creada", [str(cb)])
    except (ValueError, TypeError) as e:
        mostrar_resultado("Error", [str(e)])
    pausar()


def menu():
    opciones = ["Clase Producto — 2 instancias",
                "Validación: precio no negativo",
                "Estudiante con notas opcionales",
                "@classmethod desde_diccionario",
                "Extra — Cuenta Bancaria (inventado)"]
    while True:
        mostrar_menu("BLOQUE 1 — Constructor __init__", opciones)
        op = pedir_opcion(0, len(opciones))
        if op == 0: break
        [ejercicio_1, ejercicio_2, ejercicio_3, ejercicio_4, ejercicio_extra][op - 1]()
