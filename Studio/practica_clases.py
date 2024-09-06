class Socio:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad=edad
    def __str__(self):
        return f"Socio[Nombre: {self.nombre}, Apellido: {self.apellido}, Edad: {self.edad}]"
class Pelicula:
    def __init__(self, titulo, year, director):
        self.titulo = titulo
        self.year = year
        self.director = director
    def __str__(self):
        return f"Pelicula[Titulo: {self.titulo}, Año: {self.year}, Director: {self.director}]"
class VideoClub:
    def __init__(self) -> None:
        self.socios = []
        self.peliculas = []
    def __str__(self):
        return f"VideoClub[Socios: {len(self.socios)}, Peliculas: {len(self.peliculas)}]"
class VideoClub:
    def __init__(self):
        self.socios = []
        self.peliculas = []
    def crear_socio(self, nombre, apellido, edad):
        nuevo_socio = Socio(nombre, apellido, edad)
        self.socios.append(nuevo_socio)
        print(f"Socio {nombre} creado exitosamente.")
    def eliminar_socio(self, nombre):
        socio = self.buscar_socio(nombre)
        if socio:
            self.socios.remove(socio)
            print(f"Socio {nombre} eliminado exitosamente.")
        else:
            print(f"Socio {nombre} no encontrado.")
    def crear_pelicula(self, titulo, year, director):
        nueva_pelicula = Pelicula(titulo, year, director)
        self.peliculas.append(nueva_pelicula)
        print(f"Pelicula {titulo} creada exitosamente.")
    def eliminar_pelicula(self, titulo):
        pelicula = self.buscar_pelicula(titulo)
        if pelicula:
            self.peliculas.remove(pelicula)
            print(f"Pelicula {titulo} eliminada exitosamente.")
        else:
            print(f"Pelicula {titulo} no encontrada.")
    def buscar_socio(self, nombre):
        for socio in self.socios:
            if socio.nombre == nombre:
                return socio
        return None
    def buscar_pelicula(self, titulo):
        for pelicula in self.peliculas:
            if pelicula.titulo == titulo:
                return pelicula
        return None
    def arrendar_pelicula(self, nombre, titulo):
        socio = self.buscar_socio(nombre)
        pelicula = self.buscar_pelicula(titulo)
        if socio and pelicula:
            print(f"{socio.nombre} arrendó {pelicula.titulo}.")
        else:
            print("No se pudo arrendar la película.")
    def devolver_pelicula(self, titulo):
        pelicula = self.buscar_pelicula(titulo)
        if pelicula:
            print(f"{pelicula.titulo} devuelta exitosamente.")
        else:
            print(f"Pelicula {titulo} no encontrada.")

def main():
    while True:
        try:
            print("1. Crear socio")
            print("2. Eliminar socio")
            print("3. Crear película")
            print("4. Eliminar película")
            print("5. Arrendar película")
            print("6. Devolver película")
            print("7. Salir")
            opcion = int(input("Ingrese una opción: "))
            if 1 <= opcion <= 7:
                return opcion
            else:
                print("Opción inválida.")
        except ValueError:
            print("Opción inválida.")

if __name__ == "__main__":
    video_club = VideoClub()
    opcion = 0  
    while opcion != 7:
        opcion = main()
        if opcion == 1:
            nombre = input("Ingrese el nombre del socio: ")
            apellido = input("Ingrese el apellido del socio: ")
            edad = int(input("Ingrese la edad del socio: "))
            video_club.crear_socio(nombre, apellido, edad)
        elif opcion == 2:
            nombre = input("Ingrese el nombre del socio a eliminar: ")
            video_club.eliminar_socio(nombre)
        elif opcion == 3:
            titulo = input("Ingrese el título de la película: ")
            year = int(input("Ingrese el año de la película: "))
            director = input("Ingrese el director de la película: ")
            video_club.crear_pelicula(titulo, year, director)
        elif opcion == 4:
            titulo = input("Ingrese el título de la película a eliminar: ")
            video_club.eliminar_pelicula(titulo)
        elif opcion == 5:
            nombre = input("Ingrese el nombre del socio: ")
            titulo = input("Ingrese el título de la película: ")
            video_club.arrendar_pelicula(nombre, titulo)
        elif opcion == 6:
            titulo = input("Ingrese el título de la película a devolver: ")
            video_club.devolver_pelicula(titulo)
        elif opcion == 7:
            print("Saliendo...")
        else:
            print("Opción no válida.")