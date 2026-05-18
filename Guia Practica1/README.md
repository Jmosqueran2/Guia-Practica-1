# Guía Práctica Experimental 1 — POO en Python

## Descripción

Proyecto desarrollado como parte de la **Guía Práctica Experimental 1** de la asignatura
**Programación Orientada a Objetos en Python**.

Contiene los ejercicios resueltos de los 17 bloques temáticos, organizados en un sistema
de menús interactivo navegable desde la consola.

---

## Estructura del proyecto

```
poo_python/
├── main.py              # Punto de entrada — Menú General
├── README.md            # Este archivo
├── utils/
│   ├── __init__.py
│   └── menu.py          # Helpers reutilizables: mostrar_menu, pedir_opcion, pausar
└── bloques/
    ├── __init__.py
    ├── bloque_00.py     # Introducción a la POO
    ├── bloque_01.py     # Constructor __init__
    ├── bloque_02.py     # Variables y tipos de datos
    ├── bloque_03.py     # Operadores
    ├── bloque_04.py     # Entrada y salida
    ├── bloque_05.py     # Condicionales
    ├── bloque_06.py     # Bucles
    ├── bloque_07.py     # Funciones
    ├── bloque_08.py     # Listas
    ├── bloque_09.py     # Tuplas
    ├── bloque_10.py     # Diccionarios
    ├── bloque_11.py     # Conjuntos
    ├── bloque_12.py     # Excepciones
    ├── bloque_13.py     # Decoradores
    ├── bloque_14.py     # Unpacking
    ├── bloque_15.py     # Funciones de orden superior
    ├── bloque_16.py     # Archivos y JSON
    └── bloque_17.py     # Mixins
```

---

## Cómo ejecutar

```bash
python main.py
```

Navega con los números que aparecen en cada menú. `0` siempre vuelve al menú anterior o sale.

---

## Bloques y temas

| # | Tema |
|---|------|
| 0 | Introducción a la POO |
| 1 | Constructor `__init__` |
| 2 | Variables y tipos de datos |
| 3 | Operadores |
| 4 | Entrada y salida (`input` / `print`) |
| 5 | Condicionales (`if` / `elif` / `else`) |
| 6 | Bucles (`for` / `while`) |
| 7 | Funciones |
| 8 | Listas |
| 9 | Tuplas |
| 10 | Diccionarios |
| 11 | Conjuntos (`set`) |
| 12 | Excepciones (`try` / `except`) |
| 13 | Decoradores |
| 14 | Unpacking |
| 15 | Funciones de orden superior |
| 16 | Archivos y JSON |
| 17 | Mixins |

---

## Uso de Inteligencia Artificial

Según los requisitos de la guía, se documenta el uso de IA en cada ejercicio.

### Formato de documentación por ejercicio

```
IA utilizada:      Claude (Anthropic)
Prompt principal:  [mensaje usado para entender el concepto]
Prompt similar:    [mensaje usado para generar un proceso parecido]
Resolución propia: [código resuelto de forma independiente]
```

### Registro de prompts

> Este apartado se completa a medida que se resuelven los ejercicios.

#### Bloque 0 — Introducción a la POO

| Ejercicio | IA | Prompt principal | Prompt similar |
|-----------|-----|-----------------|----------------|
| 1 | Claude | _pendiente_ | _pendiente_ |
| 2 | Claude | _pendiente_ | _pendiente_ |
| 3 | Claude | _pendiente_ | _pendiente_ |

<!-- Repetir tabla para cada bloque -->

---

## Convenciones de código

- Todos los datos tienen **validaciones** en el constructor o en la función correspondiente.
- Cada bloque expone una función `menu()` que es invocada desde `main.py`.
- Las utilidades de menú están centralizadas en `utils/menu.py`.

---

## Requisitos

- Python 3.10 o superior (se usa `match-case` en el bloque 5).
- No requiere dependencias externas.
