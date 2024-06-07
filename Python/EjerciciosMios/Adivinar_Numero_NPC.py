import random

numeroAdivinado = False
intentos = 1
minimo = 0
maximo = 100

print("Piensa un número aleatorio del 0 al 100")

while not numeroAdivinado:
    intentarNumero = (minimo + maximo) // 2
    print(f'Intento {intentos}: {intentarNumero}')
    elegirCercania = input('Indica si es ( + ) mayor, ( - ) menor, o es tu número ( = ): ')

    if elegirCercania == '+':
        intentos += 1
        minimo = intentarNumero + 1
    elif elegirCercania == '-':
        intentos += 1
        maximo = intentarNumero - 1
    elif elegirCercania == '=':
        numeroAdivinado = True
    else:
        print("La opción introducida no es correcta, repita su elección.")

print(f'Tu número es el {intentarNumero} y se ha adivinado en {intentos} intento(s)')