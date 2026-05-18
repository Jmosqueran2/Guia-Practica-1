"""
Utilidades para el sistema de menús.
Marcos centrados, gotoxy, limpiar, pedir_opcion, pausar.
"""
import os
import sys
import shutil


# ── Terminal ──────────────────────────────────────────────
def _cols() -> int:
    return shutil.get_terminal_size((80, 24)).columns

def _rows() -> int:
    return shutil.get_terminal_size((80, 24)).lines

def gotoxy(x: int, y: int):
    sys.stdout.write(f"\033[{y};{x}H")
    sys.stdout.flush()

def limpiar():
    """Limpia la pantalla completamente."""
    cols = _cols()
    rows = _rows()
    # 1) Borrar pantalla y scrollback buffer
    sys.stdout.write("\033[2J\033[3J")
    # 2) Ir a (1,1) y sobrescribir fila por fila con espacios
    sys.stdout.write("\033[H")
    for _ in range(rows):
        sys.stdout.write("\r" + " " * cols)
    # 3) Volver a (1,1) para dibujar encima
    sys.stdout.write("\033[H")
    sys.stdout.flush()

# ── Marcos ────────────────────────────────────────────────
MARCOS = {
    "simple": {
        "tl": "+",  "tr": "+",  "bl": "+",  "br": "+",
        "sl": "+",  "sr": "+",
        "h":  "-",  "v":  "|",
    },
    "doble": {
        "tl": "╔",  "tr": "╗",  "bl": "╚",  "br": "╝",
        "sl": "╠",  "sr": "╣",
        "h":  "═",  "v":  "║",
    },
    "redondeado": {
        "tl": "╭",  "tr": "╮",  "bl": "╰",  "br": "╯",
        "sl": "├",  "sr": "┤",
        "h":  "─",  "v":  "│",
    },
    "grueso": {
        "tl": "┏",  "tr": "┓",  "bl": "┗",  "br": "┛",
        "sl": "┣",  "sr": "┫",
        "h":  "━",  "v":  "┃",
    },
}

# ── Colores ───────────────────────────────────────────────
COLORES = {
    "blanco":   "\033[97m",
    "cyan":     "\033[96m",
    "verde":    "\033[92m",
    "amarillo": "\033[93m",
    "magenta":  "\033[95m",
    "azul":     "\033[94m",
}
RESET = "\033[0m"
BOLD  = "\033[1m"

# ── Config activa ─────────────────────────────────────────
_config = {"marco": "doble", "color": "cyan"}

def set_marco(n: str):
    if n in MARCOS:   _config["marco"] = n
def set_color(n: str):
    if n in COLORES:  _config["color"] = n
def get_config() -> dict:
    return dict(_config)


# ── Helpers internos ──────────────────────────────────────
def _cx(ancho: int) -> int:
    return max(1, (_cols() - ancho) // 2)

def _cy(alto: int) -> int:
    return max(1, (_rows() - alto) // 2)

def _ir(cx, cy, fila):
    gotoxy(cx, cy + fila)

def _borde(col, m, izq, interior, der):
    sys.stdout.write(col + izq + m["h"] * interior + der + RESET)
    sys.stdout.flush()

def _fila_centrada(col, m, interior, texto, negrita=False):
    b = BOLD if negrita else ""
    t = texto.center(interior)
    sys.stdout.write(col + m["v"] + RESET + b + t + RESET + col + m["v"] + RESET)
    sys.stdout.flush()

def _fila_izq(col, m, interior, texto):
    t = f"  {texto}".ljust(interior)
    sys.stdout.write(col + m["v"] + RESET + t + col + m["v"] + RESET)
    sys.stdout.flush()


# ── API pública ───────────────────────────────────────────
def mostrar_menu(titulo: str, opciones: list[str]) -> None:
    """Limpia pantalla y dibuja menú centrado con marco."""
    limpiar()
    m   = MARCOS[_config["marco"]]
    col = COLORES[_config["color"]]

    max_txt  = max(len(titulo), max(len(o) for o in opciones))
    ancho    = max(max_txt + 6, 46)
    interior = ancho - 2
    # filas: top + titulo + sep + N opciones + sep + opcion0 + bot
    alto = len(opciones) + 6

    cx = _cx(ancho)
    cy = _cy(alto)

    _ir(cx,cy,0); _borde(col,m, m["tl"], interior, m["tr"])
    _ir(cx,cy,1); _fila_centrada(col,m, interior, titulo, negrita=True)
    _ir(cx,cy,2); _borde(col,m, m["sl"], interior, m["sr"])
    for i, op in enumerate(opciones, 1):
        _ir(cx,cy, 2+i)
        _fila_centrada(col,m, interior, f"{i:>2}. {op}")
    _ir(cx,cy, 2+len(opciones)+1); _borde(col,m, m["sl"], interior, m["sr"])
    _ir(cx,cy, 2+len(opciones)+2); _fila_centrada(col,m, interior, "0. Volver / Salir")
    _ir(cx,cy, 2+len(opciones)+3); _borde(col,m, m["bl"], interior, m["br"])

    # Cursor de input justo debajo del marco
    gotoxy(cx, cy + alto)
    sys.stdout.write("\n")
    sys.stdout.flush()


def mostrar_resultado(titulo: str, lineas: list[str]) -> None:
    """Limpia pantalla y dibuja resultado centrado con marco."""
    limpiar()
    m   = MARCOS[_config["marco"]]
    col = COLORES[_config["color"]]

    max_txt  = max(len(titulo), max((len(l) for l in lineas), default=0))
    ancho    = max(max_txt + 6, 46)
    interior = ancho - 2
    alto     = len(lineas) + 4   # top + titulo + sep + lineas + bot

    cx = _cx(ancho)
    cy = _cy(alto)

    _ir(cx,cy,0); _borde(col,m, m["tl"], interior, m["tr"])
    _ir(cx,cy,1); _fila_centrada(col,m, interior, titulo, negrita=True)
    _ir(cx,cy,2); _borde(col,m, m["sl"], interior, m["sr"])
    for i, l in enumerate(lineas):
        _ir(cx,cy, 3+i)
        _fila_izq(col,m, interior, l)
    _ir(cx,cy, 3+len(lineas)); _borde(col,m, m["bl"], interior, m["br"])

    gotoxy(cx, cy + alto)
    sys.stdout.write("\n")
    sys.stdout.flush()


def pedir_con_marco(titulo: str, campos: list[str]) -> list[str]:
    """
    Muestra un marco con título y N campos de input.
    Retorna lista con los valores ingresados.
    """
    limpiar()
    m   = MARCOS[_config["marco"]]
    col = COLORES[_config["color"]]

    max_txt  = max(len(titulo), max(len(c) for c in campos)) + 20
    ancho    = max(max_txt + 6, 50)
    interior = ancho - 2
    # filas: top + titulo + sep + N campos + bot
    alto = len(campos) + 4

    cx = _cx(ancho)
    cy = _cy(alto)

    # Dibujar marco completo primero
    _ir(cx,cy,0); _borde(col,m, m["tl"], interior, m["tr"])
    _ir(cx,cy,1); _fila_centrada(col,m, interior, titulo, negrita=True)
    _ir(cx,cy,2); _borde(col,m, m["sl"], interior, m["sr"])
    for i, campo in enumerate(campos):
        _ir(cx,cy, 3+i)
        _fila_izq(col,m, interior, f"{campo}: ")
    _ir(cx,cy, 3+len(campos)); _borde(col,m, m["bl"], interior, m["br"])

    # Ahora recoger inputs posicionando el cursor en cada campo
    resultados = []
    for i, campo in enumerate(campos):
        # Posicionar cursor al final del texto del campo
        label = f"  {campo}: "
        gotoxy(cx + len(label), cy + 3 + i)
        sys.stdout.write(col)
        sys.stdout.flush()
        valor = input()
        sys.stdout.write(RESET)
        resultados.append(valor)

    return resultados


def pedir_opcion(minimo: int, maximo: int) -> int:
    col = COLORES[_config["color"]]
    while True:
        sys.stdout.write(col + "  › " + RESET)
        sys.stdout.flush()
        try:
            op = int(input())
            if minimo <= op <= maximo:
                return op
            print(f"  ⚠  Número entre {minimo} y {maximo}.")
        except ValueError:
            print("  ⚠  Solo números enteros.")


def pausar() -> None:
    col = COLORES[_config["color"]]
    sys.stdout.write(col + "\n  Presiona Enter para continuar..." + RESET)
    sys.stdout.flush()
    input()
