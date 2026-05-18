"""Bloque 0 — Introducción a la POO"""
from utils import mostrar_menu, mostrar_resultado, pedir_con_marco, pedir_opcion, pausar


def ejercicio_1():
    mostrar_resultado("Clases — Sistema de Biblioteca", [
        "1. Libro", "2. Usuario", "3. Prestamo", "4. Autor", "5. Categoria",
    ])
    pausar()


class Persona:
    def __init__(self, nombre: str, edad: int):
        if not nombre: raise ValueError("Nombre vacío.")
        if edad < 0:   raise ValueError("Edad negativa.")
        self.nombre = nombre
        self.edad   = edad
    def __str__(self):
        return f"Persona(nombre='{self.nombre}', edad={self.edad})"

def ejercicio_2():
    personas = [Persona("Daniel",20), Persona("Ana",25), Persona("Luis",30)]
    mostrar_resultado("Clase Persona — 3 instancias", [str(p) for p in personas])
    pausar()


def ejercicio_3():
    mostrar_resultado("Clase vs Objeto", [
        "CLASE  → molde/plantilla que define atributos y métodos.",
        "         Ejemplo: 'Persona' define nombre y edad.",
        "",
        "OBJETO → instancia concreta creada desde el molde.",
        "         Ejemplo: Persona('Daniel', 20) es un objeto.",
        "",
        "Analogia: clase = plano de casa | objeto = casa construida.",
    ])
    pausar()


# ── Ejercicio extra ───────────────────────────────────────
class Vehiculo:
    def __init__(self, marca: str, modelo: str, anio: int):
        if not marca:  raise ValueError("Marca vacía.")
        if not modelo: raise ValueError("Modelo vacío.")
        if anio < 1886: raise ValueError("Año inválido.")
        self.marca  = marca
        self.modelo = modelo
        self.anio   = anio
    def __str__(self):
        return f"{self.anio} {self.marca} {self.modelo}"

def ejercicio_extra():
    vals = pedir_con_marco("Extra — Clase Vehiculo", ["Marca", "Modelo", "Año"])
    try:
        v = Vehiculo(vals[0], vals[1], int(vals[2]))
        mostrar_resultado("Vehículo creado", [str(v), "", "Objeto instanciado correctamente."])
    except (ValueError, TypeError) as e:
        mostrar_resultado("Error", [str(e)])
    pausar()


def menu():
    opciones = ["Clases para sistema de biblioteca",
                "Clase Persona — 3 instancias",
                "Diferencia: clase vs objeto",
                "Extra — Clase Vehiculo (inventado)"]
    while True:
        mostrar_menu("BLOQUE 0 — Introducción a la POO", opciones)
        op = pedir_opcion(0, len(opciones))
        if op == 0: break
        [ejercicio_1, ejercicio_2, ejercicio_3, ejercicio_extra][op - 1]()
