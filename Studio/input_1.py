def ejemplo_input():
    try:
        # Solicitar un número
        numero = int(input("Por favor, ingresa un número: "))
        print(f"El número que ingresaste es: {numero}")
        
        # Solicitar una cadena de texto
        texto = input("Por favor, ingresa una palabra o frase: ")
        print(f"El texto que ingresaste es: {texto}")
        
    except ValueError:
        print("Error: Ingresaste un valor no válido.")

# Llamar a la función principal
ejemplo_input()
