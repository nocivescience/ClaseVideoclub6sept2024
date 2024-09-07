def crear_socio(nombre, rut, edad):
    return {"nombre": nombre, "rut": rut, "edad": edad}
def crear_pelicula(titulo, year, director):
    return {"titulo": titulo, "year": year, "director": director}
def agregar_socio(socios, socio):
    return socios + [socio]
def eliminar_socio(socios, nombre):
    return [socio for socio in socios if socio["nombre"] != nombre]
def agregar_pelicula(peliculas, pelicula):
    return peliculas + [pelicula]
def eliminar_pelicula(peliculas, titulo):
    return [pelicula for pelicula in peliculas if pelicula["titulo"] != titulo]
def buscar_socio(socios, nombre):
    for socio in socios:
        if socio["nombre"] == nombre:
            return socio
    return None

def buscar_pelicula(peliculas, titulo):
    for pelicula in peliculas:
        if pelicula["titulo"] == titulo:
            return pelicula
    return None

def arrendar_pelicula(socios, peliculas, nombre, titulo):
    socio = buscar_socio(socios, nombre)
    pelicula = buscar_pelicula(peliculas, titulo)
    if socio and pelicula:
        return f"{socio['nombre']} arrendó {pelicula['titulo']}."
    else:
        return "No se pudo arrendar la película."

def devolver_pelicula(peliculas, titulo):
    pelicula = buscar_pelicula(peliculas, titulo)
    if pelicula:
        return f"{pelicula['titulo']} devuelta exitosamente."
    else:
        return f"Pelicula {titulo} no encontrada."
    
def mostrar_menu():
    print("1. Crear socio")
    print("2. Eliminar socio")
    print("3. Crear película")
    print("4. Eliminar película")
    print("5. Arrendar película")
    print("6. Devolver película")
    print("7. Salir")
    
def main():
    socios = []
    peliculas = []
    opcion = 0
    while opcion != 7:
        mostrar_menu()
        opcion = int(input("Ingrese una opción: "))
        if opcion == 1:
            nombre = input("Ingrese el nombre del socio: ")
            rut = input("Ingrese el rut del socio: ")
            edad = int(input("Ingrese la edad del socio: "))
            socio = crear_socio(nombre, rut, edad)
            socios = agregar_socio(socios, socio)
        elif opcion == 2:
            nombre = input("Ingrese el nombre del socio: ")
            socios = eliminar_socio(socios, nombre)
        elif opcion == 3:
            titulo = input("Ingrese el título de la película: ")
            year = int(input("Ingrese el año de la película: "))
            director = input("Ingrese el director de la película: ")
            pelicula = crear_pelicula(titulo, year, director)
            peliculas = agregar_pelicula(peliculas, pelicula)
        elif opcion == 4:
            titulo = input("Ingrese el título de la película: ")
            peliculas = eliminar_pelicula(peliculas, titulo)
        elif opcion == 5:
            nombre = input("Ingrese el nombre del socio: ")
            titulo = input("Ingrese el título de la película: ")
            print(arrendar_pelicula(socios, peliculas, nombre, titulo))
        elif opcion == 6:
            titulo = input("Ingrese el título de la película: ")
            print(devolver_pelicula(peliculas, titulo))
            
if __name__ == "__main__":
    main()