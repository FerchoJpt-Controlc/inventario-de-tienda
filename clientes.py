from GuardarDatosEnArchivos import GestorArchivos

class Cliente:
    def __init__(self, IDCliente, Nombre, Direccion, Telefono, Correo):
        self.IDCliente = IDCliente
        self.Nombre = Nombre
        self.Direccion = Direccion
        self.Telefono = Telefono
        self.Correo = Correo


class GestorClientes:
    def __init__(self):
        self.archivo = GestorArchivos("CLIENTES.txt")
        self.clientes: dict[str, Cliente] = {}
        self.cargar_clientes()

    def cargar_clientes(self):
        lineas = self.archivo.cargar()
        for linea in lineas:
            IDCliente, Nombre, Direccion, Telefono, Correo = linea.strip().split(",")
            self.clientes[IDCliente] = Cliente(IDCliente, Nombre, Direccion, Telefono, Correo)

    def guardar_clientes(self):
        datos = []
        for cliente in self.clientes.values():
            datos.append(f"{cliente.IDCliente},{cliente.Nombre},{cliente.Direccion},{cliente.Telefono},{cliente.Correo}")
        self.archivo.guardar(datos)

    def agregar_cliente(self, cliente: Cliente):
        self.clientes[cliente.IDCliente] = cliente
        self.guardar_clientes()

    def mostrar_clientes(self):
        print("\n--- LISTA DE CLIENTES ---")
        for c in self.clientes.values():
            print(f"{c.IDCliente} | {c.Nombre} | {c.Direccion} | {c.Telefono} | {c.Correo}")

    def menu(self):
        while True:
            print("\n--- GESTIÓN DE CLIENTES ---")
            print("1. Ver clientes")
            print("2. Agregar cliente")
            print("0. Volver")

            try:
                opcion = input("Seleccione: ").strip()

                match opcion:
                    case "1":
                        self.mostrar_clientes()
                    case "2":
                        try:
                            ID = input("NIT: ").strip()
                            Nombre = input("Nombre: ").strip()
                            Direccion = input("Dirección: ").strip()
                            Telefono = input("Teléfono: ").strip()
                            Correo = input("Correo: ").strip()

                            if not ID or not Nombre:
                                raise ValueError("NIT y Nombre son obligatorios")

                            self.agregar_cliente(Cliente(ID, Nombre, Direccion, Telefono, Correo))
                            print("Cliente agregado correctamente.")
                        except Exception as e:
                            print(f"Error al agregar cliente: {e}")
                    case "0":
                        print("Volviendo al menú principal...")
                        break
                    case _:
                        print("Opción inválida")
            except Exception as e:
                print(f"Ocurrió un error: {e}")

