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

def Menu():
    opcion = 0

    while opcion != 5:
        print("-_M E N U_-")
        print("1. AGREGAR LIBRO")
        print("2. AGREGAR USUSARIO")
        print("3. PREWSTAR LIBRO")
        print("4. DEVOLVER LIBRO")
        print("5. SALIR")
        print("//si decea salir de adentro de alguna opcion escriba 'salir' ")

        try:
            opcion_input = salir("\nIngrese su opción: ")
            if opcion_input is None:
                continue

            if opcion_input.isdigit():
                opcion = int(opcion_input)

                if opcion == 1:
                    print("")

                elif opcion == 2:
                    print("")

                elif opcion == 3:
                    print("")

                elif opcion == 4:
                    print("")

                elif opcion == 5:
                    print("\nAdiós, regrese pronto CHAUUU...")
                else:
                    print("\nOpción inválida, vuelva a intentar")
            else:
                print("\nError: ingreso de datos no numéricos")
                opcion = 0

        except Exception as e:
            print(f"\nOcurrió un error inesperado: {e}")

        if opcion != 5:
            input("\nPresione ENTER para continuar...")


Menu()
