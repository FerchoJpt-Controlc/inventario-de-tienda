from abc import ABC, abstractmethod
from GuardarDatosEnArchivos import GestorArchivos


class IProducto(ABC):
    @abstractmethod
    def obtener_precio(self):
        pass


class Producto(IProducto):
    def __init__(self, IDProducto, Nombre, Precio, Stock):
        self.IDProducto = IDProducto
        self.Nombre = Nombre
        self.Precio = float(Precio)
        self.Stock = int(Stock)

    def obtener_precio(self):
        return self.Precio


class GestorProductos:
    def __init__(self):
        self.archivo = GestorArchivos("PRODUCTOS.txt")
        self.productos: dict[str, Producto] = {}

        self.cargar_productos()

    def cargar_productos(self):
        lineas = self.archivo.cargar()
        for linea in lineas:
            IDProducto, Nombre, Precio, Stock = linea.strip().split(",")
            self.productos[IDProducto] = Producto(IDProducto, Nombre, Precio, Stock)

    def guardar_productos(self):
        datos = []
        for producto in self.productos.values():
            datos.append(f"{producto.IDProducto},{producto.Nombre},{producto.Precio},{producto.Stock}")
        self.archivo.guardar(datos)

    def agregar_producto(self, producto: Producto, IDEmpleado=None):
        self.productos[producto.IDProducto] = producto
        self.guardar_productos()

        if producto.IDProducto in self.productos:
            self.productos[producto.IDProducto].Stock += producto.Stock
            print(f"Stock aumentado en {producto.Stock} unidades.")
        else:
            self.productos[producto.IDProducto] = producto
            print(f"Producto {producto.Nombre} agregado al inventario.")

        self.guardar_productos()

        # Registrar en compras automáticamente
        if self.gestor_compras:
            self.gestor_compras.registrar_compra(producto, IDEmpleado)

    def mostrar_productos(self):
        print("\n--- LISTA DE PRODUCTOS ---")
        for p in self.productos.values():
            print(f"{p.IDProducto} | {p.Nombre} | Q{p.Precio} | Stock: {p.Stock}")



    def menu(self):
        while True:
            print("\n--- GESTION DE PRODUCTOS ---")
            print("1. Ver productos")
            print("2. Agregar producto")
            print("0. Volver")

            opcion = input("Seleccione una opcion: ")

            if opcion == "1":
                self.mostrar_productos()

            elif opcion == "2":
                ID = input("ID: ")
                Nombre = input("Nombre: ")
                Precio = input("Precio: ")
                Stock = input("Stock: ")
                self.agregar_producto(Producto(ID, Nombre, Precio, Stock))

            elif opcion == "0":
                break
            else:
                print("Opción inválida")