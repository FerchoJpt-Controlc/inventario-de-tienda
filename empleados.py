from GuardarDatosEnArchivos import GestorArchivos

class Empleado:
    def __init__(self, IDEmpleado, Nombre, Direccion, Telefono, Correo, Puesto):
        self.IDEmpleado = IDEmpleado
        self.Nombre = Nombre
        self.Direccion = Direccion
        self.Telefono = Telefono
        self.Correo = Correo
        self.Puesto = Puesto


class GestorEmpleados:
    def __init__(self):
        self.archivo = GestorArchivos("EMPLEADOS.txt")
        self.empleados: dict[str, Empleado] = {}
        self.cargar_empleados()

    def cargar_empleados(self):
        lineas = self.archivo.cargar()
        for linea in lineas:
            datos = linea.strip().split(",")
            if len(datos) == 6:  # aseguramos que tenga todos los campos
                IDEmpleado, Nombre, Direccion, Telefono, Correo, Puesto = datos
                self.empleados[IDEmpleado] = Empleado(
                    IDEmpleado, Nombre, Direccion, Telefono, Correo, Puesto
                )
            else:
                print(f"⚠ Línea inválida en EMPLEADOS.txt: {linea}")

    def guardar_empleados(self):
        datos = []
        for e in self.empleados.values():
            datos.append(
                f"{e.IDEmpleado},{e.Nombre},{e.Direccion},{e.Telefono},{e.Correo},{e.Puesto}"
            )
        self.archivo.guardar(datos)

    def agregar_empleado(self, empleado: Empleado):
        self.empleados[empleado.IDEmpleado] = empleado
        self.guardar_empleados()

    def mostrar_empleados(self):
        print("\n--- LISTA DE EMPLEADOS ---")
        for e in self.empleados.values():
            print(
                f"{e.IDEmpleado} | {e.Nombre} | {e.Direccion} | {e.Telefono} | {e.Correo} | {e.Puesto}"
            )

    def menu(self):
        while True:
            print("\n--- GESTIÓN DE EMPLEADOS ---")
            print("1. Ver empleados")
            print("2. Agregar empleado")
            print("0. Volver")

            try:
                opcion = input("Seleccione: ").strip()

                match opcion:
                    case "1":
                        self.mostrar_empleados()
                    case "2":
                        try:
                            ID = input("ID: ").strip()
                            Nombre = input("Nombre: ").strip()
                            Direccion = input("Direccion: ").strip()
                            Telefono = input("Telefono: ").strip()
                            Correo = input("Correo: ").strip()
                            Puesto = input("Puesto: ").strip()

                            if not ID or not Nombre:
                                raise ValueError("ID y Nombre son obligatorios")

                            self.agregar_empleado(
                                Empleado(ID, Nombre, Direccion, Telefono, Correo, Puesto)
                            )
                            print("Empleado agregado correctamente.")
                        except Exception as e:
                            print(f"Error al agregar empleado: {e}")
                    case "0":
                        print("Volviendo al menú principal...")
                        break
                    case _:
                        print("Opción inválida")
            except Exception as e:
                print(f"Ocurrió un error: {e}")




