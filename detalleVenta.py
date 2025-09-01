from GuardarDatosEnArchivos import GestorArchivos

class DetalleVenta:
    def __init__(self, IDDetalle, IDVenta, IDProducto, Cantidad, Subtotal):
        self.IDDetalle = IDDetalle
        self.IDVenta = IDVenta
        self.IDProducto = IDProducto
        self.Cantidad = int(Cantidad)
        self.Subtotal = float(Subtotal)


class GestorDetalleVentas:
    def __init__(self):
        self.archivo = GestorArchivos("DETALLEVENTAS.txt")
        self.detalles: dict[str, DetalleVenta] = {}
        self.cargar_detalles()

    def cargar_detalles(self):
        lineas = self.archivo.cargar()
        for linea in lineas:
            IDDetalle, IDVenta, IDProducto, Cantidad, Subtotal = linea.strip().split(",")
            self.detalles[IDDetalle] = DetalleVenta(IDDetalle, IDVenta, IDProducto, Cantidad, Subtotal)

    def guardar_detalles(self):
        datos = []
        for d in self.detalles.values():
            datos.append(f"{d.IDDetalle},{d.IDVenta},{d.IDProducto},{d.Cantidad},{d.Subtotal}")
        self.archivo.guardar(datos)

    def agregar_detalle(self, detalle: DetalleVenta):
        self.detalles[detalle.IDDetalle] = detalle
        self.guardar_detalles()

    def mostrar_detalles(self):
        print("\n--- DETALLES DE VENTAS ---")
        for d in self.detalles.values():
            print(f"{d.IDDetalle} | Venta: {d.IDVenta} | Prod: {d.IDProducto} | Cant: {d.Cantidad} | Subtotal: Q{d.Subtotal}")
