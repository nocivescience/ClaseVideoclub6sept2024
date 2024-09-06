class Socio:
    def __init__(self, id_socio, nombre):
        self.id_socio = id_socio
        self.nombre = nombre
    def __str__(self):
        return f"Socio[ID: {self.id_socio}, Nombre: {self.nombre}]"
    
class Pelicula:
    def __init__(self, id_pelicula, titulo):
        self.id_pelicula = id_pelicula
        self.titulo = titulo
        self.alquilada = False
    def __str__(self):
        estado = "Alquilada" if self.alquilada else "Disponible"
        return f"Pelicula[ID: {self.id_pelicula}, Titulo: {self.titulo}, Estado: {estado}]"
    
class VideoClub:
    def __init__(self):
        self.socios = []
        self.peliculas = []
    def crear_socio(self, id_socio, nombre):
        nuevo_socio = Socio(id_socio, nombre)
        self.socios.append(nuevo_socio)
        print(f"Socio {nombre} creado exitosamente.")
    def eliminar_socio(self, id_socio):
        socio=self.buscar_socio(id_socio)
        if socio:
            self.socios.remove(socio)
            print(f"Socio {id_socio} eliminado exitosamente.")
        else:
            print(f"Socio {id_socio} no encontrado.")
    def crear_pelicula(self, id_pelicula, titulo):
        nueva_pelicula = Pelicula(id_pelicula, titulo)
        self.peliculas.append(nueva_pelicula)
        print(f"Pelicula {titulo} creada exitosamente.")
    def eliminar_pelicula(self, id_pelicula):
        pelicula = self.buscar_pelicula(id_pelicula)
        if pelicula:
            self.peliculas.remove(pelicula)
            print(f"Pelicula {id_pelicula} eliminada exitosamente.")
        else:
            print(f"Pelicula {id_pelicula} no encontrada.")
    def arrendar_pelicula(self, id_socio, id_pelicula):
        socio = self.buscar_socio(id_socio)
        pelicula = self.buscar_pelicula(id_pelicula)
        if socio and pelicula and not pelicula.alquilada:
            pelicula.alquilada = True
            print(f"Pelicula {pelicula.titulo} arrendada por {socio.nombre}.")
        else:
            print("No se pudo arrendar la película.")
    def devolver_pelicula(self, id_pelicula):
        pelicula = self.buscar_pelicula(id_pelicula)
        if pelicula:
            pelicula.alquilada = False
            print(f"Pelicula {pelicula.titulo} devuelta exitosamente.")
        else:
            print(f"Pelicula {id_pelicula} no encontrada.")
    def buscar_pelicula(self, id_pelicula):
        for pelicula in self.peliculas:
            if pelicula.id_pelicula == id_pelicula:
                return pelicula
        return None
    def buscar_socio(self, id_socio):
        for socio in self.socios:
            if socio.id_socio == id_socio:
                return socio
        return None
    
def menu():
    while True:
        try:
            print("EL MEJOR VIDEOCLUB DEL MUNDO")
            print("1. Crear socio")
            print("2. Eliminar socio")
            print("3. Crear película")
            print("4. Eliminar película")
            print("5. Arrendar película")
            print("6. Devolver película")
            print("7. Salir")
            opcion = int(input("Ingrese una opción: "))
            if 1<=opcion<=7:
                return opcion
            else:
                print("Opción no válida. Intente nuevamente.")
        except ValueError:
            print("Opción no válida. Intente nuevamente.")
            
if __name__ == "__main__":
    videoclub = VideoClub()
    while True:
        opcion = menu()
        if opcion == 1:
            id_socio = int(input("Ingrese ID del socio: "))
            nombre = input("Ingrese nombre del socio: ")
            videoclub.crear_socio(id_socio, nombre)
        elif opcion == 2:
            id_socio = int(input("Ingrese ID del socio: "))
            videoclub.eliminar_socio(id_socio)
        elif opcion == 3:
            id_pelicula = int(input("Ingrese ID de la película: "))
            titulo = input("Ingrese título de la película: ")
            videoclub.crear_pelicula(id_pelicula, titulo)
        elif opcion == 4:
            id_pelicula = int(input("Ingrese ID de la película: "))
            videoclub.eliminar_pelicula(id_pelicula)
        elif opcion == 5:
            id_socio = int(input("Ingrese ID del socio: "))
            id_pelicula = int(input("Ingrese ID de la película: "))
            videoclub.arrendar_pelicula(id_socio, id_pelicula)
        elif opcion == 6:
            id_pelicula = int(input("Ingrese ID de la película: "))
            videoclub.devolver_pelicula(id_pelicula)
        elif opcion == 7:
            print("Saliendo...")
        else:
            print("Opción no válida. Intente nuevamente")
        