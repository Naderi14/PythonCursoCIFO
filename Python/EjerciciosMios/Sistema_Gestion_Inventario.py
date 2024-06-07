import os

def AgregarProducto(inventario, id):
    nombre = input("Introduzca el nombre del nuevo producto: ").title()
    while True:
        try:
            precio = round(float(input("Introduzca el precio del producto: ")), 2)
            if precio <= 0:
                os.system('cls')
                print("El precio no puede ser 0 o negativo")
            cantidad = int(input(f"Introduzca la cantidad de {nombre}(Por defecto 1u.): "))
            if not cantidad or cantidad <= 0:
                cantidad = 1
            break
        except ValueError:
            os.system('cls')
            print("-----=====¡¡ El precio debe ser un número !!=====-----\n")
    id = id + 1
    producto = {
        'ID' : id,
        'NombreProducto' : nombre,
        'Precio' : precio,
        'Cantidad' : cantidad
    }
    inventario.append(producto)
    os.system('cls')
    print("-----Producto agregado correctamente-----\n")
    return id

def EliminarProducto(inventario):
    if InventarioVacio(inventario) == False:
        MostrarInventario(inventario)
        try:
            productoID = int(input("Introduzca la ID del producto que desea eliminar: "))
        except ValueError:
            os.system('cls')
            print("-----=====¡¡ Dato erróneo introducido, vuelva a repetir !!=====-----\n")
        for producto in inventario:
            if productoID == producto['ID']:
                os.system('cls')
                print(f"Se ha borrado del inventario: {producto['NombreProducto']}")
                inventario.remove(producto)
            else:
                os.system('cls')
                print(f"No se ha encontrado ningún producto con ID #{productoID}\n")
    else:
        os.system('cls')
        print("-----El inventario está vacío-----\n")

def ActualizarProducto(inventario):
    if InventarioVacio(inventario) == False:
        MostrarInventario(inventario)
        try:
            productoID = int(input("Introduzca la ID del producto que desea actualizar: "))
        except ValueError:
            os.system('cls')
            print("-----=====¡¡ Dato erróneo introducido, vuelva a repetir !!=====-----\n")
        for producto in inventario:
            if productoID == producto['ID']:
                print("-----Producto actual en Inventario-----")
                print(f"#{producto['ID']} / Producto: {producto['NombreProducto']} / Precio: {producto['Precio']}€ / Cantidad: {producto['Cantidad']}")
                while True:
                    try:
                        nuevoPrecio = float(input('\nIntroduzca nuevo Precio(Enter para mantener actual): '))
                        nuevaCantidad = int(input('\nIntroduzca nueva Cantidad(Enter para mantener actual): '))
                        break
                    except ValueError:
                        print("-----=====¡¡ Dato erróneo introducido, vuelva a repetir !!=====-----\n")
                if nuevoPrecio != None:
                    producto['Precio'] = nuevoPrecio
                if nuevaCantidad != None:
                    producto['Cantidad'] = nuevaCantidad
    else:
        print("-----El inventario está vacío-----\n")

def MostrarInventario(inventario):
    if InventarioVacio(inventario) == False:
        for producto in inventario:
            print(f"#{producto['ID']} / Producto: {producto['NombreProducto']} / Precio: {producto['Precio']}€ / Cantidad: {producto['Cantidad']}")
    else:
        print("-----El inventario está vacío-----\n")

def InventarioVacio(inventario):
    return len(inventario) == 0

def SGI_MenuPrincipal():
    inventario = []
    id = 0
    opcion = None
    os.system('cls')
    while opcion != 5:
        print("-----=====S.G.I. (v1.04) Manager=====-----")
        print(
            "    1. Agregar un producto\n",
            "   2. Actualizar un producto\n",
            "   3. Eliminar un producto\n",
            "   4. Mostrar inventario\n",
            "   5. Salir de S.G.I.\n"
        )
        try:
            opcion = int(input('Seleccionar opción: '))
        except ValueError:
            os.system('cls')
            print("-----=====¡¡ Dato erróneo introducido, vuelva a repetir !!=====-----\n")
        if opcion == 1:
            os.system('cls')
            id = AgregarProducto(inventario, id)
        elif opcion == 2:
            os.system('cls')
            ActualizarProducto(inventario)
        elif opcion == 3:
            os.system('cls')
            EliminarProducto(inventario)
        elif opcion == 4:
            os.system('cls')
            MostrarInventario(inventario)
        elif opcion == 5:
            os.system('cls')
            print("¡Hasta la próxima!\n")
        else:
            print("Opción no válida\n")

SGI_MenuPrincipal()