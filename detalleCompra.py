from GuardarDatosEnArchivos import GestorArchivos

class DetalleCompra:
    def __init__(self, IDDetalle, IDCompra, IDProducto, Cantidad, Subtotal):
        self.IDDetalle = IDDetalle
        self.IDCompra = IDCompra
        self.IDProducto = IDProducto
        self.Cantidad = int(Cantidad)
        self.Subtotal = float(Subtotal)


class GestorDetalleCompras:
    def __init__(self):
        self.archivo = GestorArchivos("DETALLECOMPRAS.txt")
        self.detalles: dict[str, DetalleCompra] = {}
        self.cargar_detalles()

    def cargar_detalles(self):
        lineas = self.archivo.cargar()
        for linea in lineas:
            IDDetalle, IDCompra, IDProducto, Cantidad, Subtotal = linea.strip().split(",")
            self.detalles[IDDetalle] = DetalleCompra(IDDetalle, IDCompra, IDProducto, Cantidad, Subtotal)

    def guardar_detalles(self):
        datos = []
        for d in self.detalles.values():
            datos.append(f"{d.IDDetalle},{d.IDCompra},{d.IDProducto},{d.Cantidad},{d.Subtotal}")
        self.archivo.guardar(datos)

    def agregar_detalle(self, detalle: DetalleCompra):
        self.detalles[detalle.IDDetalle] = detalle
        self.guardar_detalles()

    def mostrar_detalles(self):
        print("\n--- DETALLES DE COMPRAS ---")
        for d in self.detalles.values():
            print(f"{d.IDDetalle} | Compra: {d.IDCompra} | Prod: {d.IDProducto} | Cant: {d.Cantidad} | Subtotal: Q{d.Subtotal}")
