'''
    Escribir un programa en Python que gestione una biblioteca. La biblioteca contiene una colección de libros y cada 
    libro tiene un título, un autor y un año de publicación. El programa debe ofrecer las siguientes funcionalidades mediante el uso de funciones:

        · Añadir un nuevo libro: Se pedirá al usuario el título, el autor y el año de publicación del libro, y se añadirá a la colección.
        · Mostrar todos los libros: Se mostrarán todos los libros en la colección.
        · Buscar libros por autor: Se pedirá al usuario el nombre de un autor y se mostrarán todos los libros escritos por ese autor.
        · Eliminar un libro: Se pedirá al usuario el título de un libro y se eliminará de la colección si existe.
        · Terminar el programa: Finalizar la ejecución del programa.
'''
import os
libros = []

def AddLibro():
    '''
        Funcion para agregar un nuevo libro y añadirlo a la lista de libros
        Se preguntará por el titulo, autor y fecha para incluirlo primero en un diccionario y luego en la lista
    '''
    tituloLibro = input('Introduzca el título del libro: ').title()
    if tituloLibro == "":
        print("No se pueden introducir campos vacios")
        AddLibro()
    autorLibro = input('Introduzca el autor del libro: ').title()
    if autorLibro == "":
        print("No se pueden introducir campos vacios")
        AddLibro()
    fechaLibro = input('Introduzca la fecha de lanzamiento (dd/mm/aaaa)')
    if fechaLibro == "":
        print("No se pueden introducir campos vacios")
        AddLibro()
    nuevoLibro = {
        'Titulo' : tituloLibro,
        'Autor' : autorLibro,
        'Fecha' : fechaLibro
    }
    libros.append(nuevoLibro)

def BibliotecaVacia():
    '''
        Funcion para comprobar si la biblioteca esta vacia devolviendo una condición verdadera o falsa
    '''
    estaVacia = True
    if len(libros) > 0:
        estaVacia = False
    return estaVacia

def MostrarLibros():
    '''
        Funcion para mostrar todos los libros dentro de la lista
        Accederemos a BibliotecaVacia() para comprobar si la lista esta vacia
        Imprimiremos en cada fila los datos del libro seleccionado en el for
    '''
    if BibliotecaVacia() == False:
        for libro in libros:
            print(f"Título: {libro['Titulo']} | Autor: {libro['Autor']} | Fecha: {libro['Fecha']}")
    else:
        print("La biblioteca está vacía")

def BuscarLibros():
    '''
        Funcion para buscar los libros en función del nombre del autor aportado por el usuario
        Haremos un bucle por compresion para encontrar los libros donde Autor sea coincidente y almacenarlos en una lista bajo el nombre "encontrados"
        Por ultimo la imprimiremos un libro por fila
    '''
    if BibliotecaVacia() == False:
        MostrarLibros()
        autorIn = input('Introduce el autor para buscar si tenemos libros suyos: ').title()
        encontrados = [libro for libro in libros if autorIn in libro['Autor']]
        if encontrados:
            for libro in encontrados:
                print(f"Título: {libro['Titulo']} | Autor: {libro['Autor']} | Fecha: {libro['Fecha']}")
        else:
            print("No se ha encontrado libros del autor")
    else:
        print("La biblioteca está vacía")
                
def EliminarLibro():
    '''
        Funcion para buscar el libro coincidente con el título y proceder a borrarlo con un remove() e imprimir el libro borrado
    '''
    if BibliotecaVacia() == False:
        MostrarLibros()
        tituloIn = input('Introduce el título del libro para eliminarlo: ').title()
        libroEncontrado = None
        for libro in libros:
            if libro['Titulo'] == tituloIn:
                libroEncontrado = libro
                break
        if libroEncontrado:
            libros.remove(libroEncontrado)
            print(f"Se ha eliminado el libro: Título: {libroEncontrado['Titulo']} | Autor: {libroEncontrado['Autor']} | Fecha: {libroEncontrado['Fecha']}")
        else:
            print(f"No se ha encontrado ningún libro con el título {tituloIn}")
    else:
        print("La biblioteca está vacía")

def MenuPrincipal():
    '''
        Funcion donde hayaremos el menú principal del programa por donde se va a manejar nuestro gestor de la biblioteca
    '''
    opcion = None
    os.system('cls')
    while opcion != 5:
        print("\n1.Agregar un libro | 2.Mostrar Biblioteca | 3.Buscar un libro | 4.Eliminar un libro | 5.Salir\n")
        try:
            opcion = int(input('Introduzca la opción deseada: '))
        except ValueError:
            print("Error: El dato introducido no es correcto")
            opcion = None
        if opcion == 1:
            os.system('cls')
            AddLibro()
        elif opcion == 2:
            os.system('cls')
            MostrarLibros()
        elif opcion == 3:
            os.system('cls')
            BuscarLibros()
        elif opcion == 4:
            os.system('cls')
            EliminarLibro()
        elif opcion == 5:
            os.system('cls')
            print("¡Hasta la próxima!")
        else:
            os.system('cls')
            print("La opcion introducida no coincide con ninguna anterior")

MenuPrincipal()