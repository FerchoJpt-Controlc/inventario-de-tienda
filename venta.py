from GuardarDatosEnArchivos import GestorArchivos

class Venta:
    def __init__(self, IDVenta, IDCliente, IDEmpleado, Fecha, Total):
        self.IDVenta = IDVenta
        self.IDCliente = IDCliente
        self.IDEmpleado = IDEmpleado
        self.Fecha = Fecha
        self.Total = float(Total)


class GestorVentas:
    def __init__(self):
        self.archivo = GestorArchivos("VENTAS.txt")
        self.ventas: dict[str, Venta] = {}
        self.cargar_ventas()

    def cargar_ventas(self):
        lineas = self.archivo.cargar()
        for linea in lineas:
            IDVenta, IDCliente, IDEmpleado, Fecha, Total = linea.strip().split(",")
            self.ventas[IDVenta] = Venta(IDVenta, IDCliente, IDEmpleado, Fecha, Total)

    def guardar_ventas(self):
        datos = []
        for v in self.ventas.values():
            datos.append(f"{v.IDVenta},{v.IDCliente},{v.IDEmpleado},{v.Fecha},{v.Total}")
        self.archivo.guardar(datos)

    def agregar_venta(self, venta: Venta):
        self.ventas[venta.IDVenta] = venta
        self.guardar_ventas()

    def mostrar_ventas(self):
        print("\n--- LISTA DE VENTAS ---")
        for v in self.ventas.values():
            print(f"{v.IDVenta} | Cliente: {v.IDCliente} | Emp: {v.IDEmpleado} | {v.Fecha} | Total: Q{v.Total}")
