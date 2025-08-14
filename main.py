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

class Gestiones:
    def __init__(self):
        self.usuarios = {}
        self.libros = {}

    def ingreso_libro(self, libro):