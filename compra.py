from GuardarDatosEnArchivos import GestorArchivos

#compra
class Compra:
    def __init__(self, IDCompra, IDProveedor, IDEmpleado, Fecha, Total):
        self.IDCompra = IDCompra
        self.IDProveedor = IDProveedor
        self.IDEmpleado = IDEmpleado
        self.Fecha = Fecha
        self.Total = float(Total)

class GestorCompras:
    def __init__(self):
        self.archivo = GestorArchivos("COMPRAS.txt")
        self.compras: dict[str, Compra] = {}
        self.cargar_compras()

    def cargar_compras(self):
        lineas = self.archivo.cargar()
        for linea in lineas:
            IDCompra, IDProveedor, IDEmpleado, Fecha, Total = linea.strip().split(",")
            self.compras[IDCompra] = Compra(IDCompra, IDProveedor, IDEmpleado, Fecha, Total)

    def guardar_compras(self):
        datos = [f"{c.IDCompra},{c.IDProveedor},{c.IDEmpleado},{c.Fecha},{c.Total}"
                 for c in self.compras.values()]
        self.archivo.guardar(datos)

    def agregar_compra(self, compra: Compra):
        self.compras[compra.IDCompra] = compra
        self.guardar_compras()

    def mostrar_compras(self):
        print("\n--- LISTA DE COMPRAS ---")
        for c in self.compras.values():
            print(f"IDcompra{c.IDCompra} | Prov: {c.IDProveedor} | Emp: {c.IDEmpleado} | FechaCompra{c.Fecha} | Tot: Q{c.Total}")


#detcompra
class DetalleCompra:
    def __init__(self, IDCompra, IDProducto, Cantidad, Subtotal):
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
            IDCompra, IDProducto, Cantidad, Subtotal = linea.strip().split(",")
            self.DetalleCompra(IDCompra, IDProducto, Cantidad, Subtotal)

    def guardar_detalles(self):
        datos = [f"{d.IDCompra},{d.IDProducto},{d.Cantidad},{d.Subtotal}"
                 for d in self.detalles.values()]
        self.archivo.guardar(datos)

    def agregar_detalle(self, detalle: DetalleCompra):
        self.detalles[detalle] = detalle
        self.guardar_detalles()

    def mostrar_detalles(self):
        print("\n--- DETALLES DE COMPRAS ---")
        for d in self.detalles.values():
            print(f"Compra: {d.IDCompra} | Prod: {d.IDProducto} | Cant: {d.Cantidad} | Subtotal: Q{d.Subtotal}")




