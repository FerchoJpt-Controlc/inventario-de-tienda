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
            IDEmpleado, Nombre, Direccion, Telefono, Correo, Puesto = linea.strip().split(",")
            self.empleados[IDEmpleado] = Empleado(IDEmpleado, Nombre, Direccion, Telefono, Correo, Puesto)

    def guardar_empleados(self):
        datos = []
        for e in self.empleados.values():
            datos.append(f"{e.IDEmpleado},{e.Nombre},{e.Direccion},{e.Telefono},{e.Correo},{e.Puesto}")
        self.archivo.guardar(datos)

    def agregar_empleado(self, empleado: Empleado):
        self.empleados[empleado.IDEmpleado] = empleado
        self.guardar_empleados()

    def mostrar_empleados(self):
        print("\n--- LISTA DE EMPLEADOS ---")
        for e in self.empleados.values():
            print(f"{e.IDEmpleado} | {e.Nombre} | {e.Puesto} ")


