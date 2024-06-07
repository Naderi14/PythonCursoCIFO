'''
    1. Consultar precio
    2. Calcular precio producto
    3. Consultar nueva fruta
    4. Salir
'''
import os

def Productos():
    frutas = {
    'platano' : 1.35,
    'manzana' : 1.9,
    'naranja': 1.25,
    'uva': 3.45,
    'pera': 2.30,
    'aranja' : 1.85
    }
    return frutas

def inputFruta(frutas):
    global frutaSeleccionada
    frutaSeleccionada = input('Introduce la fruta con la que quieres consultar el precio: ').lower()
    if frutaSeleccionada == 'plátano':
        frutaSeleccionada = 'platano'
    if frutaSeleccionada in frutas:
        os.system('cls')
        print("Fruta seleccionada\n")
    else:
        print("La fruta que ha seleccionado no corresponde con ninguna de nuestra base de datos\n")
        inputFruta()

def ConsultarPrecios(frutas):
    os.system('cls')
    for fruta, precio in frutas.items():
        print(f"- {fruta}: {precio}€/kg")
    print("\n")

def CalcularPrecio(frutas):
    if flag == True:
        try:
            kg = float(input(f"\nIntroduzca cantidad de {frutaSeleccionada} en Kg: "))
            print(f"Precio total: {round(frutas[frutaSeleccionada] * kg, 2)}€\n")
        except:
            print("El valor introducido es erróneo, tiene que repetir la operación\n")
            CalcularPrecio()
    else:
        print("No tiene ninguna fruta seleccionada\n")

def MenuPrincipal(frutas):
    global flag
    flag = False
    os.system('cls')
    opcion = 0
    while opcion != 4:
        print(f"1.Seleccionar nueva Fruta")
        print(f"2.Consultar precios")
        if flag == True:
            
            print(f"3.Calcular total {frutaSeleccionada}", end='s\n')
            print(f"4.Salir\n")
        else:
            print(f"3.Salir\n")

        opcion = int(input("Introduzca la opción: "))

        if flag == True:
            if opcion == 1:
                inputFruta(frutas)
            elif opcion == 2:
                ConsultarPrecios(frutas)
            elif opcion == 3 and flag == True:
                CalcularPrecio(frutas)
            elif opcion == 4:
                print("¡Hasta la próxima!")
            else:
                os.system('cls')
                print("Opción introducida incorrecta\n")
        else:
            if opcion == 1:
                inputFruta(frutas)
                flag = True
            elif opcion == 2:
                ConsultarPrecios(frutas)
            elif opcion == 3:
                print("¡Hasta la próxima!")
                break
            else:
                os.system('cls')
                print("Opción introducida incorrecta\n")

MenuPrincipal(Productos())