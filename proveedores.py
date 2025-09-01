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



    def menu(self):
        while True:
            print("\n--- GESTION DE PROVEEDORES ---")
            print("1. Ver proveedores")
            print("2. Agregar proveedor")
            print("0. Volver")

            try:
                opcion = input("Seleccione: ").strip()

                match opcion:
                    case "1":
                        self.mostrar_proveedores()
                    case "2":
                        try:
                            ID = input("NIT del proveedor: ").strip()
                            Nombre = input("Nombre del proveedor: ").strip()
                            Telefono = input("Teléfono: ").strip()
                            Correo = input("Correo: ").strip()

                            if not ID or not Nombre:
                                raise ValueError("ID y Nombre son obligatorios")

                            self.agregar_proveedor(Proveedor(ID, Nombre, Telefono, Correo))
                            print("Proveedor agregado correctamente.")
                        except Exception as e:
                            print(f"Error al agregar proveedor: {e}")
                    case "0":
                        print("Volviendo al menu principal...")
                        break
                    case _:
                        print("Opcion invalida")
            except Exception as e:
                print(f"Ocurrio un error: {e}")

