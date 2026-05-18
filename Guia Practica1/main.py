"""
Guía Práctica Experimental 1 — POO en Python
Punto de entrada principal — Menú General
"""
from utils import mostrar_menu, pedir_opcion, pausar, limpiar
from utils import preferencias
from bloques import BLOQUES

TITULOS_BLOQUES = [
    "Bloque  0  —  Introducción a la POO",
    "Bloque  1  —  Constructor __init__",
    "Bloque  2  —  Variables y tipos de datos",
    "Bloque  3  —  Operadores",
    "Bloque  4  —  Entrada y salida",
    "Bloque  5  —  Condicionales",
    "Bloque  6  —  Bucles",
    "Bloque  7  —  Funciones",
    "Bloque  8  —  Listas",
    "Bloque  9  —  Tuplas",
    "Bloque 10  —  Diccionarios",
    "Bloque 11  —  Conjuntos (set)",
    "Bloque 12  —  Excepciones",
    "Bloque 13  —  Decoradores",
    "Bloque 14  —  Unpacking",
    "Bloque 15  —  Funciones de orden superior",
    "Bloque 16  —  Archivos y JSON",
    "Bloque 17  —  Mixins",
    "⚙  Preferencias de apariencia",
]


class MenuGeneral:
    def ejecutar(self):
        while True:
            mostrar_menu("GUÍA POO EN PYTHON", TITULOS_BLOQUES)
            op = pedir_opcion(0, len(TITULOS_BLOQUES))
            if op == 0:
                limpiar()
                print("\n  👋 ¡Hasta pronto!\n")
                break
            limpiar()
            if op == len(TITULOS_BLOQUES):          # última opción = preferencias
                preferencias.menu()
            else:
                self._abrir_bloque(op - 1)

    def _abrir_bloque(self, indice: int):
        try:
            BLOQUES[indice].menu()
        except Exception as e:
            print(f"\n  ❌ Error: {e}")
            pausar()


if __name__ == "__main__":
    MenuGeneral().ejecutar()
