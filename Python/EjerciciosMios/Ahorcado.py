'''
    El autor de este Script, es consciente de no ser pitoniso en su magnífico esplendor, pero
    tampoco es su objetivo en este script.

    A continuación vemos un prototipo del juego del Ahorcado.

    Reto a que se clasifique las características y funciones de este codigo en Métodos y que tenga una estructura ideal
    para su correcto funcionamiento (No alterar el funcionamiento que actualmente ya tiene)
'''
# Importamos las librerias que usaremos en este script
import random, os

# Inicializamos nuestro diccionario de palabras que usaremos para el juego
palabras = (
    "Manzana", "Escalera", "Teléfono", "Mariposa", "Llave", "Taza", "Azul", "Montaña",
    "Relámpago", "Espejo", "Alegría", "Reloj", "Río", "Guitarra", "Castillo", "Arena",
    "Pluma", "Diamante", "Cielo", "Sol", "Lluvia", "Estrella", "Bosque", "Faro",
    "Jardín", "Viento", "Nube", "Carro", "Luna", "Libro", "Pájaro", "Vela", "Barco",
    "Flor", "Cometa", "Faro", "Cereza", "Olas", "Pelota", "Árbol", "Ventana", "Papel",
    "Sombrero", "Barco", "Fruta", "Trébol", "Camino", "Tesoro", "Desierto", "Cueva",
    "Fantasma", "Nieve", "Trueno", "Caballo", "Piano", "Coche", "Mapa", "Hielo",
    "Enigma", "Coral", "Sol", "Rayo", "Joya", "Refugio", "Gruta", "Cascada", "Faro",
    "Isla", "Arena", "Trébol", "Relato", "Aurora", "Eco", "Murciélago", "Fantasía",
    "Neblina", "Sirena", "Gaviota", "Horizonte", "Planeta", "Cometa", "Aventura",
    "Eclipse", "Horizonte", "Destino", "Sirena", "Magia", "Horizonte", "Castillo",
    "Atardecer", "Sombrero", "Horizonte", "Amanecer", "Marea", "Faro", "Tesoro",
    "Arena", "Faro", "Trébol", "Nube"
)

acertijos = (
    "Fruta roja que crece en un árbol.",                # Manzana
    "Herramienta para subir a lugares altos.",          # Escalera
    "Dispositivo para hacer llamadas.",                 # Teléfono
    "Insecto con alas coloridas.",                      # Mariposa
    "Objeto para abrir cerraduras.",                    # Llave
    "Recipiente para beber café o té.",                 # Taza
    "Color del cielo despejado.",                       # Azul
    "Elevación natural del terreno.",                   # Montaña
    "Luz brillante durante una tormenta.",              # Relámpago
    "Superficie que refleja imágenes.",                 # Espejo
    "Sentimiento de felicidad.",                        # Alegría
    "Objeto para medir el tiempo.",                     # Reloj
    "Cuerpo de agua que fluye.",                        # Río
    "Instrumento musical de cuerdas.",                  # Guitarra
    "Edificio fortificado medieval.",                   # Castillo
    "Granos pequeños en la playa.",                     # Arena
    "Parte del cuerpo de las aves.",                    # Pluma
    "Piedra preciosa muy dura.",                        # Diamante
    "Espacio sobre la tierra donde están las nubes.",   # Cielo
    "Estrella que ilumina la Tierra.",                  # Sol
    "Agua que cae de las nubes.",                       # Lluvia
    "Cuerpo celeste que brilla en el cielo nocturno.",  # Estrella
    "Área grande llena de árboles.",                    # Bosque
    "Torre con luz para guiar a los barcos.",           # Faro
    "Lugar con plantas y flores.",                      # Jardín
    "Aire en movimiento.",                              # Viento
    "Vapor de agua en el cielo.",                       # Nube
    "Vehículo con ruedas.",                             # Carro
    "Satélite natural de la Tierra.",                   # Luna
    "Conjunto de hojas con texto.",                     # Libro
    "Animal con plumas que puede volar.",               # Pájaro
    "Fuente de luz con cera.",                          # Vela
    "Vehículo para viajar por agua.",                   # Barco
    "Parte colorida de una planta.",                    # Flor
    "Juguete que vuela en el viento.",                  # Cometa
    "Torre con luz en la costa.",                       # Faro
    "Pequeña fruta roja con hueso.",                    # Cereza
    "Movimientos del agua en el mar.",                  # Olas
    "Objeto redondo usado en deportes.",                # Pelota
    "Planta grande con tronco.",                        # Árbol
    "Abertura en una pared para la luz.",               # Ventana
    "Material para escribir o dibujar.",                # Papel
    "Prenda para cubrir la cabeza.",                    # Sombrero
    "Vehículo acuático.",                               # Barco
    "Producto comestible de una planta.",               # Fruta
    "Planta de hojas con forma de corazón.",            # Trébol
    "Sendero para caminar o conducir.",                 # Camino
    "Conjunto de riquezas.",                            # Tesoro
    "Área árida con poca vegetación.",                  # Desierto
    "Cavidad natural en la tierra.",                    # Cueva
    "Ser imaginario o espíritu.",                       # Fantasma
    "Precipitación blanca y fría.",                     # Nieve
    "Sonido fuerte después del relámpago.",             # Trueno
    "Animal grande que se puede montar.",               # Caballo
    "Instrumento musical con teclas.",                  # Piano
    "Vehículo de motor para transporte.",               # Coche
    "Representación gráfica de un área.",               # Mapa
    "Agua congelada.",                                  # Hielo
    "Algo difícil de entender o resolver.",             # Enigma
    "Estructura marina hecha por organismos.",          # Coral
    "Estrella central del sistema solar.",              # Sol
    "Descarga eléctrica en una tormenta.",              # Rayo
    "Objeto de adorno con piedras preciosas.",          # Joya
    "Lugar seguro para protegerse.",                    # Refugio
    "Caverna o cueva pequeña.",                         # Gruta
    "Caída de agua en un río.",                         # Cascada
    "Torre para guiar barcos.",                         # Faro
    "Tierra rodeada de agua.",                          # Isla
    "Granitos pequeños en la playa.",                   # Arena
    "Planta con hojas en forma de corazón.",            # Trébol
    "Narración de una historia.",                       # Relato
    "Luz del amanecer.",                                # Aurora
    "Sonido que se repite al rebotar.",                 # Eco
    "Mamífero volador nocturno.",                       # Murciélago
    "Imaginación creativa.",                            # Fantasía
    "Nube baja que reduce la visibilidad.",             # Neblina
    "Criatura mítica mitad pez, mitad mujer.",          # Sirena
    "Ave que vive cerca del mar.",                      # Gaviota
    "Línea donde el cielo y la tierra parecen encontrarse.", # Horizonte
    "Cuerpo celeste que orbita una estrella.",          # Planeta
    "Cuerpo celeste con cola luminosa.",                # Cometa
    "Suceso extraordinario o inesperado.",              # Aventura
    "Ocultación de un astro por otro.",                 # Eclipse
    "Línea donde el cielo se encuentra con la tierra.", # Horizonte
    "Fuerza que determina el futuro.",                  # Destino
    "Criatura marina mítica.",                          # Sirena
    "Arte de realizar actos inexplicables.",            # Magia
    "Línea donde el cielo y la tierra se unen.",        # Horizonte
    "Edificio fortificado.",                            # Castillo
    "Momento en que el sol se oculta.",                 # Atardecer
    "Prenda para cubrir la cabeza.",                    # Sombrero
    "Línea donde el cielo y la tierra se encuentran.",  # Horizonte
    "Momento en que el sol aparece.",                   # Amanecer
    "Subida y bajada del nivel del mar.",               # Marea
    "Torre con luz para guiar a los barcos.",           # Faro
    "Conjunto de riquezas.",                            # Tesoro
    "Granos pequeños en la playa.",                     # Arena
    "Torre con luz en la costa.",                       # Faro
    "Planta de hojas con forma de corazón.",            # Trébol
    "Vapor de agua en el cielo.",                       # Nube
)
# Inicializamos todas las variables iniciales de la partida a nuestra conveniencia
contadorLetras = 0
palabraEscogida = ""
vidas = 6
palabraCompletada = False
letraDescubierta = True
letraSavedImpresa = False
listaLetras = []
indice = random.randint(0,99)
palabraEscogida = palabras[indice].lower()
acertijoEscogido = acertijos[indice]

# Comenzamos a mostrar la palabra oculta
for letra in range(0, palabraEscogida.__len__()):
    print("_", end=" ")

# Aquí tenemos nuestro bucle principal del juego
while vidas > 0 and palabraCompletada == False:
    # Comprobaremos que todas las letras de la palabra han sido descubiertas
    if contadorLetras >= palabraEscogida.__len__():
        palabraCompletada = True
        break
    elif letraDescubierta == False and palabraCompletada == False:
        vidas -= 1

    # En caso contrario inicializaremos el contador de letras de nuevo a 0 para iniciar nueva partida para descubrir las restantes
    contadorLetras = 0
    os.system('cls')
    letraDescubierta = False
    print(f"\n\nVidas: {vidas}")
    if vidas < 4:
        print(f"Pista: {acertijoEscogido}\n")
    # Aqui pedimos la letra que el jugador decide introducir en la ronda actual
    letraIn = input('Introduce una letra: ').lower()

    '''
        Aqui vamos a procesar la letra introducida comparandola con la palabra oculta imprimiento asi en su lugar la letra
        en vez de el guión que lo oculta y almacenaremos esa letra en una lista de letras, que irá en aumento a medida
        que se descubran mas letras.
        
        Por lo tanto para que encada ronda aparezcan las letras ya previamente descubiertas recorreremos la lista de letras
        comparando esa lista con la palabra oculta e ir mostrandolas las coincidentes.

        Como plus, en caso de haber una vocal, esta puede tener acento, entonces crearemos un nido de condicionales para
        abarcar todas las posibilidades y que represente que si se introdujo una (a) equivaldria tambien a la (á) y la
        agreguemos también a la lista de letras
    '''
    
    for letra in range(palabraEscogida.__len__()):
        letraSavedImpresa = False
        for letraSaved in listaLetras:
            if letraSaved == palabraEscogida[letra]:
                print(f"{letraSaved}", end=" ")
                letraSavedImpresa = True
                contadorLetras += 1
        if palabraEscogida[letra] == letraIn and letraSavedImpresa == False:
            print(f"{letraIn}", end=" ")
            letraDescubierta = True
            listaLetras.append(letraIn)
        elif letraIn == 'a' and palabraEscogida[letra] == 'á':
            print("á", end=" ")
            letraDescubierta = True
            listaLetras.append('á')
        elif letraIn == 'e' and palabraEscogida[letra] == 'é':
            print("é", end=" ")
            letraDescubierta = True
            listaLetras.append('é')
        elif letraIn == 'i' and palabraEscogida[letra] == 'í':
            print("í", end=" ")
            letraDescubierta = True
            listaLetras.append('í')
        elif letraIn == 'o' and palabraEscogida[letra] == 'ó':
            print("ó", end=" ")
            letraDescubierta = True
            listaLetras.append('ó')
        elif letraIn == 'u' and palabraEscogida[letra] == 'ú':
            print("ú", end=" ")
            letraDescubierta = True
            listaLetras.append('ú')
        elif palabraEscogida[letra] != letraIn and letraSavedImpresa == False:
            print("_", end=" ")

# Limpiamos consola y una vez que se ha salido del bucle principal, solo tenemos 2 opciones, o perder o ganar en función de las vidas
os.system('cls')
if vidas >= 1:
    print(f"\nMuy bien! Adivinaste la palabra: ({palabraEscogida})\nCon aun {vidas} vidas restante/s")
else:
    print(f"\nLo sentimos mucho! Te quedaste sin vidas\nLa palabra era: {palabraEscogida}")