from GuardarDatosEnArchivos import GestorArchivos

class Proveedor:
    def __init__(self, IDProveedor, Nombre, Telefono, Correo):
        self.IDProveedor = IDProveedor
        self.Nombre = Nombre
        self.Telefono = Telefono
        self.Correo = Correo


class GestorProveedores:
    def __init__(self):
        self.archivo = GestorArchivos("PROVEEDORES.txt")
        self.proveedores: dict[str, Proveedor] = {}
        self.cargar_proveedores()

    def cargar_proveedores(self):
        lineas = self.archivo.cargar()
        for linea in lineas:
            IDProveedor, Nombre, Telefono, Correo = linea.strip().split(",")
            self.proveedores[IDProveedor] = Proveedor(IDProveedor, Nombre, Telefono, Correo)

    def guardar_proveedores(self):
        datos = []
        for p in self.proveedores.values():
            datos.append(f"{p.IDProveedor},{p.Nombre},{p.Telefono},{p.Correo}")
        self.archivo.guardar(datos)

    def agregar_proveedor(self, proveedor: Proveedor):
        self.proveedores[proveedor.IDProveedor] = proveedor
        self.guardar_proveedores()

    def mostrar_proveedores(self):
        print("\n--- LISTA DE PROVEEDORES ---")
        for p in self.proveedores.values():
            print(f"{p.IDProveedor} | {p.Nombre} | {p.Telefono} | {p.Correo}")
