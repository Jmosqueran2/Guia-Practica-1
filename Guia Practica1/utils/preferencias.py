"""
Submenú de preferencias de apariencia del menú.
Permite al usuario elegir marco y color en tiempo de ejecución.
"""
from .menu import (
    limpiar, gotoxy, mostrar_menu, pedir_opcion, pausar,
    set_marco, set_color, get_config, MARCOS, COLORES,
)


def menu_marcos():
    """Submenú para elegir el estilo de marco."""
    nombres = list(MARCOS.keys())
    ejemplos = {
        "simple":     "+ --- +  |   |  + --- +",
        "doble":      "╔ ═══ ╗  ║   ║  ╚ ═══ ╝",
        "redondeado": "╭ ─── ╮  │   │  ╰ ─── ╯",
        "grueso":     "┏ ━━━ ┓  ┃   ┃  ┗ ━━━ ┛",
    }
    opciones = [f"{n.capitalize():<14} {ejemplos[n]}" for n in nombres]
    while True:
        mostrar_menu("ESTILO DE MARCO", opciones)
        op = pedir_opcion(0, len(opciones))
        if op == 0:
            break
        set_marco(nombres[op - 1])
        # Mostrar preview inmediato
        mostrar_menu(f"Marco '{nombres[op-1]}' aplicado ✓", ["El menú ahora luce así"])
        pedir_opcion(0, 1)
        break


def menu_colores():
    """Submenú para elegir el color del marco."""
    nombres = list(COLORES.keys())
    opciones = [n.capitalize() for n in nombres]
    while True:
        mostrar_menu("COLOR DE MARCO", opciones)
        op = pedir_opcion(0, len(opciones))
        if op == 0:
            break
        set_color(nombres[op - 1])
        mostrar_menu(f"Color '{nombres[op-1]}' aplicado ✓", ["El menú ahora luce así"])
        pedir_opcion(0, 1)
        break


def menu():
    """Menú principal de preferencias."""
    cfg = get_config()
    while True:
        cfg = get_config()
        opciones = [
            f"Estilo de marco   (actual: {cfg['marco']})",
            f"Color del marco   (actual: {cfg['color']})",
        ]
        mostrar_menu("⚙  PREFERENCIAS DE APARIENCIA", opciones)
        op = pedir_opcion(0, len(opciones))
        if op == 0:
            break
        limpiar()
        if op == 1:
            menu_marcos()
        elif op == 2:
            menu_colores()
