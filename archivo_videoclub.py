# Clase para gestionar los socios
class Socio:
    def __init__(self, id_socio, nombre):
        self.id_socio = id_socio
        self.nombre = nombre

    def __str__(self):
        return f"Socio[ID: {self.id_socio}, Nombre: {self.nombre}]"

# Clase para gestionar las películas
class Pelicula:
    def __init__(self, id_pelicula, titulo):
        self.id_pelicula = id_pelicula
        self.titulo = titulo
        self.alquilada = False

    def __str__(self):
        estado = "Alquilada" if self.alquilada else "Disponible"
        return f"Pelicula[ID: {self.id_pelicula}, Titulo: {self.titulo}, Estado: {estado}]"

# Clase para gestionar los alquileres
class VideoClub:
    def __init__(self):
        self.socios = []
        self.peliculas = []

    def crear_socio(self, id_socio, nombre):
        nuevo_socio = Socio(id_socio, nombre)
        self.socios.append(nuevo_socio)
        print(f"Socio {nombre} creado exitosamente.")

    def eliminar_socio(self, id_socio):
        self.socios = [s for s in self.socios if s.id_socio != id_socio]
        print(f"Socio {id_socio} eliminado exitosamente.")

    def crear_pelicula(self, id_pelicula, titulo):
        nueva_pelicula = Pelicula(id_pelicula, titulo)
        self.peliculas.append(nueva_pelicula)
        print(f"Pelicula {titulo} creada exitosamente.")

    def eliminar_pelicula(self, id_pelicula):
        self.peliculas = [p for p in self.peliculas if p.id_pelicula != id_pelicula]
        print(f"Pelicula {id_pelicula} eliminada exitosamente.")

    def arrendar_pelicula(self, id_socio, id_pelicula):
        socio = self.buscar_socio(id_socio)
        pelicula = self.buscar_pelicula(id_pelicula)
        if socio and pelicula and not pelicula.alquilada:
            pelicula.alquilada = True
            print(f"Pelicula {pelicula.titulo} arrendada por {socio.nombre}.")
        else:
            print(f"No se puede arrendar la pelicula {id_pelicula}.")

    def devolver_pelicula(self, id_pelicula):
        pelicula = self.buscar_pelicula(id_pelicula)
        if pelicula and pelicula.alquilada:
            pelicula.alquilada = False
            print(f"Pelicula {pelicula.titulo} devuelta exitosamente.")
        else:
            print(f"No se puede devolver la pelicula {id_pelicula}.")

    def buscar_socio(self, id_socio):
        for socio in self.socios:
            if socio.id_socio == id_socio:
                return socio
        print(f"Socio {id_socio} no encontrado.")
        return None

    def buscar_pelicula(self, id_pelicula):
        for pelicula in self.peliculas:
            if pelicula.id_pelicula == id_pelicula:
                return pelicula
        print(f"Pelicula {id_pelicula} no encontrada.")
        return None

# Funcion del menú principal con manejo de errores
def menu():
    while True:
        try:
            print("\n***VIDEO CLUB***")
            print("1.- Crear socio")
            print("2.- Eliminar socio")
            print("3.- Crear pelicula")
            print("4.- Eliminar pelicula")
            print("5.- Arrendar pelicula")
            print("6.- Devolver pelicula")
            print("7.- Salir")
            opcion = int(input("Ingresa opción: "))
            if 1 <= opcion <= 7:
                return opcion
            else:
                print("Por favor, ingresa un número entre 1 y 7.")
        except ValueError:
            print("Error: Por favor, ingresa un número válido.")

# Programa principal con control de entradas
if __name__ == "__main__":
    video_club = VideoClub()
    opcion = 0
    while opcion != 7:
        opcion = menu()
        if opcion == 1:
            id_socio = input("ID del socio: ")
            nombre = input("Nombre del socio: ")
            video_club.crear_socio(id_socio, nombre)
        elif opcion == 2:
            id_socio = input("ID del socio a eliminar: ")
            video_club.eliminar_socio(id_socio)
        elif opcion == 3:
            id_pelicula = input("ID de la pelicula: ")
            titulo = input("Titulo de la pelicula: ")
            video_club.crear_pelicula(id_pelicula, titulo)
        elif opcion == 4:
            id_pelicula = input("ID de la pelicula a eliminar: ")
            video_club.eliminar_pelicula(id_pelicula)
        elif opcion == 5:
            id_socio = input("ID del socio: ")
            id_pelicula = input("ID de la pelicula: ")
            video_club.arrendar_pelicula(id_socio, id_pelicula)
        elif opcion == 6:
            id_pelicula = input("ID de la pelicula a devolver: ")
            video_club.devolver_pelicula(id_pelicula)
        elif opcion == 7:
            print("Saliendo...")
        else:
            print("Opción no válida.")
