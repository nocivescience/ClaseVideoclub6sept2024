# Definir datos como tuplas o diccionarios para representar a los socios y películas
def crear_socio(nombre, apellido, edad):
    return {"nombre": nombre, "apellido": apellido, "edad": edad}

def crear_pelicula(titulo, year, director):
    return {"titulo": titulo, "year": year, "director": director}

# Función para agregar un nuevo socio sin modificar el estado global
def agregar_socio(socios, socio):
    return socios + [socio]

# Función para eliminar un socio (inmutable)
def eliminar_socio(socios, nombre):
    return [socio for socio in socios if socio["nombre"] != nombre]

# Función para agregar una película
def agregar_pelicula(peliculas, pelicula):
    return peliculas + [pelicula]

# Función para eliminar una película (inmutable)
def eliminar_pelicula(peliculas, titulo):
    return [pelicula for pelicula in peliculas if pelicula["titulo"] != titulo]

# Función para buscar un socio
def buscar_socio(socios, nombre):
    for socio in socios:
        if socio["nombre"] == nombre:
            return socio
    return None

# Función para buscar una película
def buscar_pelicula(peliculas, titulo):
    for pelicula in peliculas:
        if pelicula["titulo"] == titulo:
            return pelicula
    return None

# Función para arrendar una película
def arrendar_pelicula(socios, peliculas, nombre, titulo):
    socio = buscar_socio(socios, nombre)
    pelicula = buscar_pelicula(peliculas, titulo)
    if socio and pelicula:
        return f"{socio['nombre']} arrendó {pelicula['titulo']}."
    else:
        return "No se pudo arrendar la película."

# Función para devolver una película (en este contexto, la devolución es solo un mensaje)
def devolver_pelicula(peliculas, titulo):
    pelicula = buscar_pelicula(peliculas, titulo)
    if pelicula:
        return f"{pelicula['titulo']} devuelta exitosamente."
    else:
        return f"Pelicula {titulo} no encontrada."

# Función para el menú (función pura)
def mostrar_menu():
    print("1. Crear socio")
    print("2. Eliminar socio")
    print("3. Crear película")
    print("4. Eliminar película")
    print("5. Arrendar película")
    print("6. Devolver película")
    print("7. Salir")
    return int(input("Ingrese una opción: "))

# Función principal que maneja la interacción con el sistema (sin estado mutable global)
def main():
    socios = []
    peliculas = []
    opcion = 0
    while opcion != 7:
        opcion = mostrar_menu()
        if opcion == 1:
            nombre = input("Ingrese el nombre del socio: ")
            apellido = input("Ingrese el apellido del socio: ")
            edad = int(input("Ingrese la edad del socio: "))
            nuevo_socio = crear_socio(nombre, apellido, edad)
            socios = agregar_socio(socios, nuevo_socio)
            print(f"Socio {nombre} creado exitosamente.")
        elif opcion == 2:
            nombre = input("Ingrese el nombre del socio a eliminar: ")
            socios = eliminar_socio(socios, nombre)
            print(f"Socio {nombre} eliminado exitosamente.")
        elif opcion == 3:
            titulo = input("Ingrese el título de la película: ")
            year = int(input("Ingrese el año de la película: "))
            director = input("Ingrese el director de la película: ")
            nueva_pelicula = crear_pelicula(titulo, year, director)
            peliculas = agregar_pelicula(peliculas, nueva_pelicula)
            print(f"Pelicula {titulo} creada exitosamente.")
        elif opcion == 4:
            titulo = input("Ingrese el título de la película a eliminar: ")
            peliculas = eliminar_pelicula(peliculas, titulo)
            print(f"Pelicula {titulo} eliminada exitosamente.")
        elif opcion == 5:
            nombre = input("Ingrese el nombre del socio: ")
            titulo = input("Ingrese el título de la película: ")
            print(arrendar_pelicula(socios, peliculas, nombre, titulo))
        elif opcion == 6:
            titulo = input("Ingrese el título de la película a devolver: ")
            print(devolver_pelicula(peliculas, titulo))
        elif opcion == 7:
            print("Saliendo...")
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
