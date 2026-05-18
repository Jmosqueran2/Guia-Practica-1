"""Bloque 17 — Mixins"""
import json, csv, io
from utils import mostrar_menu, mostrar_resultado, pedir_con_marco, pedir_opcion, pausar


# ── Ejercicio 1 — PromedioMixin ───────────────────────────
class PromedioMixin:
    def calcular_promedio(self, notas: list) -> float:
        if not notas: raise ValueError("Lista vacía.")
        return sum(notas) / len(notas)

class EstudianteProm(PromedioMixin):
    def __init__(self, nombre: str, notas: list):
        if not nombre: raise ValueError("Nombre vacío.")
        self.nombre = nombre; self.notas = notas

def ejercicio_1():
    e1 = EstudianteProm("María",[8,9,10])
    e2 = EstudianteProm("Pedro",[6,7,5])
    mostrar_resultado("PromedioMixin", [
        f"Estudiante : {e1.nombre}  notas={e1.notas}  prom={e1.calcular_promedio(e1.notas):.2f}",
        f"Estudiante : {e2.nombre}  notas={e2.notas}  prom={e2.calcular_promedio(e2.notas):.2f}",
    ])
    pausar()


# ── Ejercicio 2 — ValidacionMixin ────────────────────────
class ValidacionMixin:
    def validar_email(self, c): return "@" in c and c.endswith(".com")
    def validar_edad(self, e):  return isinstance(e,int) and e >= 18

class Usuario(ValidacionMixin):
    def __init__(self, nombre, email, edad):
        if not nombre:               raise ValueError("Nombre vacío.")
        if not self.validar_email(email): raise ValueError(f"Email inválido: '{email}'")
        if not self.validar_edad(edad):   raise ValueError(f"Edad inválida: {edad} (mínimo 18).")
        self.nombre=nombre; self.email=email; self.edad=edad
    def __str__(self): return f"Usuario('{self.nombre}', {self.email}, {self.edad} años)"

def ejercicio_2():
    casos = [("Ana","ana@gmail.com",22),("Luis","luisgmail.com",25),("Eva","eva@gmail.com",16)]
    lineas = []
    for nombre,email,edad in casos:
        try:    lineas.append(f"✅ {Usuario(nombre,email,edad)}")
        except ValueError as e: lineas.append(f"❌ {nombre}: {e}")
    mostrar_resultado("ValidacionMixin", lineas)
    pausar()


# ── Ejercicio 3 — ExportarMixin ──────────────────────────
class ExportarMixin:
    def exportar_json(self, datos):
        if not datos: raise ValueError("Datos vacíos.")
        return json.dumps(datos, indent=2, ensure_ascii=False)
    def exportar_csv(self, datos):
        if not datos: raise ValueError("Datos vacíos.")
        buf = io.StringIO()
        w = csv.DictWriter(buf, fieldnames=datos[0].keys())
        w.writeheader(); w.writerows(datos)
        return buf.getvalue()

class Reporte(ExportarMixin):
    def __init__(self, titulo):
        if not titulo: raise ValueError("Título vacío.")
        self.titulo = titulo

def ejercicio_3():
    ventas = [{"producto":"Laptop","precio":900},{"producto":"Mouse","precio":25}]
    r = Reporte("Ventas")
    mostrar_resultado("ExportarMixin — JSON y CSV", [
        "── JSON ─────────────────────────────",
        *r.exportar_json(ventas).splitlines(),
        "",
        "── CSV ──────────────────────────────",
        *r.exportar_csv(ventas).splitlines(),
    ])
    pausar()


# ── Ejercicio extra ───────────────────────────────────────
class LogMixin:
    _historial: list = []
    def registrar(self, accion: str):
        from time import strftime
        self._historial.append(f"[{strftime('%H:%M:%S')}] {accion}")
    def ver_historial(self): return list(self._historial)

class SistemaInventario(LogMixin):
    def __init__(self):
        self._historial = []
        self.productos = {}
    def agregar(self, nombre: str, stock: int):
        if not nombre: raise ValueError("Nombre vacío.")
        if stock < 0:  raise ValueError("Stock negativo.")
        self.productos[nombre] = self.productos.get(nombre, 0) + stock
        self.registrar(f"Agregado: {nombre} (+{stock}) → total={self.productos[nombre]}")
    def retirar(self, nombre: str, cantidad: int):
        if nombre not in self.productos: raise KeyError(f"'{nombre}' no existe.")
        if cantidad > self.productos[nombre]: raise ValueError("Stock insuficiente.")
        self.productos[nombre] -= cantidad
        self.registrar(f"Retirado: {nombre} (-{cantidad}) → total={self.productos[nombre]}")

def ejercicio_extra():
    vals = pedir_con_marco("Extra — Sistema inventario con LogMixin",
                           ["Producto", "Cantidad a agregar", "Cantidad a retirar"])
    if not vals[0]:
        mostrar_resultado("Error", ["El producto es obligatorio."]); pausar(); return
    try:
        agregar = int(vals[1]) if vals[1] else 0
        retirar = int(vals[2]) if vals[2] else 0
        if agregar < 0 or retirar < 0: raise ValueError("Cantidades deben ser ≥ 0.")
    except ValueError as e:
        mostrar_resultado("Error", [str(e)]); pausar(); return

    inv = SistemaInventario()
    lineas = []
    try:
        if agregar > 0: inv.agregar(vals[0], agregar)
        if retirar > 0: inv.retirar(vals[0], retirar)
        lineas = [f"Stock final: {inv.productos.get(vals[0], 0)}", "", "── Historial (LogMixin) ──"] + inv.ver_historial()
    except (ValueError, KeyError) as e:
        lineas = [f"❌ {e}"] + (["── Historial ──"] + inv.ver_historial() if inv.ver_historial() else [])
    mostrar_resultado(f"Inventario: {vals[0]}", lineas)
    pausar()


def menu():
    opciones = ["PromedioMixin — calcular_promedio()",
                "ValidacionMixin — email y edad",
                "ExportarMixin — JSON y CSV",
                "Extra — SistemaInventario con LogMixin (inventado)"]
    while True:
        mostrar_menu("BLOQUE 17 — Mixins", opciones)
        op = pedir_opcion(0, len(opciones))
        if op == 0: break
        [ejercicio_1, ejercicio_2, ejercicio_3, ejercicio_extra][op - 1]()
