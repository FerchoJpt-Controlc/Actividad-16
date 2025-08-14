class Libro:
    def __init__(self, titulo, autor, año, codigo):
        self.titulo = titulo
        self.autor = autor
        self.año = año
        self.codigo = codigo

    def mostrar_info(self):
        return f"titulo: {self.titulo} - Autor: {self.autor} - Año de publicacion: {self.año} - Codigo del libro: {self.codigo}"

class Usuario:
    def __init__(self, nombre, carnet, carrera):
        self.nombre = nombre
        self.carnet = carnet
        self.carrera = carrera

    def mostrar_info_usuario(self):
        return f"Nombre: {self.nombre} - Carnet: {self.carnet} - Carrera: {self.carrera}"

class Registro_libro(Libro):
    def __init__(self):
        self.libros = {}

        def ingresar(self):
            try:
                codigo = input("Ingrese el codigo del libro: ")
                if codigo in self.libros:
                    print("Ya existe un librop con ese codigo.\n")
                    return

                titulo = input("Ingresar nombre del estudiante: ")
                autor = input("Ingrese el nombre del autor: ")
                año = int(input("Ingrese el año de publicacion: "))

                self.libros[codigo] = Libro(titulo, autor, año)
                print("Estudiante agregado.\n")
            except ValueError:
                print("Error: La edad debe ser un número entero.\n")



class Gestiones:
    def __init__(self):
        self.usuarios = {}
