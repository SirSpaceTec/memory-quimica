import random
import time
import os
from colorama import Fore, Style

ELEMENTOS = [
    ['Actinio', 'Ac', 89], ['Aluminio', 'Al', 13], ['Americio', 'Am', 95], ['Antimonio', 'Sb', 51],
    ['Argón', 'Ar', 18], ['Arsénico', 'As', 33], ['Ástato', 'At', 85], ['Azufre', 'S', 16],
    ['Bario', 'Ba', 56], ['Berkelio', 'Bk', 97], ['Berilio', 'Be', 4], ['Bismuto', 'Bi', 83],
    ['Bohrio', 'Bh', 107], ['Boro', 'B', 5], ['Bromo', 'Br', 35], ['Cadmio', 'Cd', 48],
    ['Calcio', 'Ca', 20], ['Californio', 'Cf', 98], ['Carbono', 'C', 6], ['Cerio', 'Ce', 58],
    ['Cesio', 'Cs', 55], ['Cloro', 'Cl', 17], ['Cobalto', 'Co', 27], ['Cobre', 'Cu', 29],
    ['Cromo', 'Cr', 24], ['Curio', 'Cm', 96], ['Darmstadtio', 'Ds', 110], ['Dubnio', 'Db', 105],
    ['Disprosio', 'Dy', 66], ['Einstenio', 'Es', 99], ['Escandio', 'Sc', 21], ['Estaño', 'Sn', 50],
    ['Estroncio', 'Sr', 38], ['Europio', 'Eu', 63], ['Fermio', 'Fm', 100], ['Flerovio', 'Fl', 114],
    ['Flúor', 'F', 9], ['Francio', 'Fr', 87], ['Galio', 'Ga', 31], ['Gadolinio', 'Gd', 64],
    ['Germanio', 'Ge', 32], ['Hafnio', 'Hf', 72], ['Hassio', 'Hs', 108], ['Helio', 'He', 2],
    ['Hidrógeno', 'H', 1], ['Hierro', 'Fe', 26], ['Holmio', 'Ho', 67], ['Indio', 'In', 49],
    ['Iridio', 'Ir', 77], ['Itrio', 'Y', 39], ['Iterbio', 'Yb', 70], ['Krypton', 'Kr', 36],
    ['Lantano', 'La', 57], ['Laurencio', 'Lr', 103], ['Litio', 'Li', 3], ['Livermorio', 'Lv', 116],
    ['Lutecio', 'Lu', 71], ['Magnesio', 'Mg', 12], ['Manganeso', 'Mn', 25], ['Meitnerio', 'Mt', 109],
    ['Mendelevio', 'Md', 101], ['Mercurio', 'Hg', 80], ['Molibdeno', 'Mo', 42], ['Moscovio', 'Mc', 115],
    ['Neodimio', 'Nd', 60], ['Neón', 'Ne', 10], ['Nihonio', 'Nh', 113], ['Níquel', 'Ni', 28],
    ['Niobio', 'Nb', 41], ['Nitrógeno', 'N', 7], ['Nobelio', 'No', 102], ['Oganesón', 'Og', 118],
    ['Oro', 'Au', 79], ['Osmio', 'Os', 76], ['Oxígeno', 'O', 8], ['Paladio', 'Pd', 46],
    ['Plata', 'Ag', 47], ['Plomo', 'Pb', 82], ['Plutonio', 'Pu', 94], ['Polonio', 'Po', 84],
    ['Potasio', 'K', 19], ['Praseodimio', 'Pr', 59], ['Prometio', 'Pm', 61], ['Protactinio', 'Pa', 91],
    ['Radio', 'Ra', 88], ['Radón', 'Rn', 86], ['Renio', 'Re', 75], ['Rodio', 'Rh', 45],
    ['Roentgenio', 'Rg', 111], ['Rubidio', 'Rb', 37], ['Rutenio', 'Ru', 44], ['Rutherfordio', 'Rf', 104],
    ['Samario', 'Sm', 62], ['Seaborgio', 'Sg', 106], ['Selenio', 'Se', 34], ['Silicio', 'Si', 14],
    ['Sodio', 'Na', 11], ['Talio', 'Tl', 81], ['Tantalio', 'Ta', 73], ['Tecnecio', 'Tc', 43],
    ['Telurio', 'Te', 52], ['Tenesino', 'Ts', 117], ['Terbio', 'Tb', 65], ['Titanio', 'Ti', 22],
    ['Torio', 'Th', 90], ['Tulio', 'Tm', 69], ['Uranio', 'U', 92], ['Vanadio', 'V', 23],
    ['Wolframio', 'W', 74], ['Xenón', 'Xe', 54], ['Zinc', 'Zn', 30], ['Zirconio', 'Zr', 40]
]


def generar_tabla(num_memo):
    global cantidad_elementos
    cantidad_elementos = num_memo * 2
    seleccionados = random.sample(ELEMENTOS, num_memo)
    elementos_repetidos = elementosRepetidos(seleccionados * 2)
    random.shuffle(elementos_repetidos)
    step = 3
    return [elementos_repetidos[i:i+step] for i in range(0,cantidad_elementos,step)]

def elementosRepetidos(seleccionados):
    repetidos = []
    for elemento in (seleccionados):
        element = elemento[0] + ' ' + elemento[1] + ' ' + str(elemento[2])
        repetidos.append(element)
    return repetidos

def mostrar_tabla(tabla):
    for fila in tabla:
        print(" | ".join(f"{Fore.GREEN}{celda:^20}{Style.RESET_ALL}" if celda else "     " for celda in fila))

def ocultar_tabla(tabla):
    contador = 1
    return [[contador + i + j * len(tabla[0]) for i in range(len(fila))] for j, fila in enumerate(tabla)]

def countdown_timer(seconds):
    for i in range(seconds, -1, -1):
        print(f"{Fore.YELLOW}Tiempo restante: {i} segundos{Style.RESET_ALL}", end="\r")
        time.sleep(1)
        print(" " * 50, end="\r")

def tiempo_memorizar(tabla, mensaje, time):
    limpiar_consola()
    print(f"{Fore.CYAN}{mensaje}{Style.RESET_ALL}")
    mostrar_tabla(tabla)
    countdown_timer(time)

def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')

def comprobar_ganador(tabla):
    cuenta_atras = cantidad_elementos
    for fila in tabla:
        for element in fila:
            try:
                int(element)
            except:
                cuenta_atras -= 1
                continue
    return cuenta_atras


def presentation():
    # Preguntar cantidad jugadores 1 o 2.
    print("🧪💡 ¡Bienvenido al laboratorio de la tabla periódica! 💡🧪\n")
    time.sleep(1)
    while True:
        try:
            cantidad_jugadores = int(input("¿Cuántos jugadores van a participar en este juego 1 o 2? "))
            if cantidad_jugadores < 1 and cantidad_jugadores > 2: 
                print(f"{Fore.RED}Debes elegir un número del 1 al 2.{Style.RESET_ALL}")
            else:
                break
        except ValueError:
            print(f"{Fore.RED}Eso no parece un número válido. Inténtalo de nuevo.{Style.RESET_ALL}")
    time.sleep(1)
    if cantidad_jugadores > 1:
        jugador1 = input("🤔 Primero, dime, ¿cómo debo llamar al jugador 1? ")
        jugador2 = input("¿Y a tí jugador 2? ")
        print(f"\n🎉 Genial, {jugador1} y {jugador2}! 🎉\n")
        time.sleep(1)
        print("📚 Hoy vais a poner a prueba vuestra memoria con los elementos de la tabla periódica.\n")
        time.sleep(1)
        print("✨ Pero cuidado... ¡no será tan fácil como parece! ¿Quién ganará?😏\n")
        time.sleep(1)
    else:
        name = input("🤔 Primero, dime, ¿cómo debo llamarte? ")
        print(f"\n🎉 Genial, {name}! 🎉\n")
        time.sleep(1)
        print("📚 Hoy vas a poner a prueba tu memoria con los elementos de la tabla periódica.\n")
        time.sleep(1)
        print("✨ Pero cuidado... ¡no será tan fácil como parece!😏\n")
        time.sleep(1)

    while True:
        if cantidad_jugadores > 1:
            mensaje_cantidad = f"Elegid la cantidad de elementos que quereis memorizar {Fore.CYAN}(para empezar os recomiendo 12){Style.RESET_ALL}: "
            mensaje_cero = f"{Fore.RED}Debeis elegir un número mayor que 0. Inténtalo de nuevo.{Style.RESET_ALL}"
        else:
            mensaje_cantidad = f"Elige la cantidad de elementos que quieres memorizar {Fore.CYAN}(para empezar te recomiendo 6){Style.RESET_ALL}: "
            mensaje_cero = f"{Fore.RED}Debes elegir un número mayor que 0. Inténtalo de nuevo.{Style.RESET_ALL}"
        try:
            cantidad = int(input(mensaje_cantidad))
            if cantidad < 1:
                print(mensaje_cero)
            else:
                break
        except ValueError:
                print(f"{Fore.RED}Eso no parece un número válido.{Style.RESET_ALL}")

    if cantidad < 7:
        print('Buena elección!')
        time.sleep(1)
    elif cantidad > 6 and cantidad < 10:
        print('¡Que atrevida elección!')
        time.sleep(1)
    else:
        print('¡WOW! ¡perfecto!')
        time.sleep(1)
    
    if cantidad_jugadores > 1:
        print("¡Prepararos para aprender y divertiros! Comencemos... 🚀\n")
        time.sleep(2)
    else:
        print("¡Prepárate para aprender y divertirte! Comencemos... 🚀\n")
        time.sleep(2)

    return (cantidad, cantidad_jugadores)
    
def juego_preguntas(tabla):
    print(f"{Fore.CYAN}¡Ahora vamos con las preguntas para verificar tu memoria!")
    tabla_set = []
    for fila in tabla:
        for element in fila:
            tabla_set.append(element)
    tabla_set = list(set(tabla_set))
    tabla_sin_repetidos = list(tabla_set)
    preguntas_elementos = []
    for elemento in tabla_sin_repetidos:
        elemento_completo = elemento.split()
        preguntas_elementos.append((f'¿Qué número atómico tiene el elemento {elemento_completo[0]}?', [elemento_completo[2]]))
        preguntas_elementos.append((f'¿Cuál es el nombre del elemento con el número atómico {elemento_completo[2]}?', [elemento_completo[0]]))
        preguntas_elementos.append((f'¿Cuál es el símbolo del elemento {elemento_completo[0]} con el número atómico {elemento_completo[2]}?', [elemento_completo[1]]))
        preguntas_elementos.append((f'¿A qué elemento pertenecen las siglas {elemento_completo[1]}?', [elemento_completo[0]]))
    seleccionados = random.sample(preguntas_elementos, 4)
    respuestas = []
    while True:
        for pregunta in seleccionados:
            respuesta = input(f'{Fore.BLUE}{pregunta[0]}{Style.RESET_ALL} ')
            if respuesta in pregunta[1]:
                respuestas.append(f'{Fore.GREEN}✅ {pregunta[0]} {str(respuesta)}{Style.RESET_ALL}')
            else:
                respuestas.append(f'{Fore.RED}🚫 {pregunta[0]} {str(respuesta)}{Style.RESET_ALL}')
        break
    for respuesta in respuestas:
        print(respuesta)

    time.sleep(3)

def juego_jugador1(tabla_oculta, tabla):
    intentos = 7
    valor1 = None
    valor2 = None
    posicion1 = None
    posicion2 = None

    while intentos > 0:
        limpiar_consola()
        print(f"{Fore.MAGENTA}Adivina las posiciones de los elementos repetidos tienes {intentos - 1} intentos:{Style.RESET_ALL}")
        mostrar_tabla(tabla_oculta)

        try:
            respuesta = int(input(f'{Fore.BLUE}Selecciona la posición (1-{cantidad_elementos}):{Style.RESET_ALL} '))
        except ValueError:
            print(f'{Fore.RED}Respuesta no válida. Debes ingresar un número entre 1 y {cantidad_elementos}.{Style.RESET_ALL}')
            time.sleep(1)
            continue

        if respuesta < 1 or respuesta > cantidad_elementos:
            print(f'{Fore.RED}Número fuera de rango. Debes ingresar un número entre 1 y {cantidad_elementos}.{Style.RESET_ALL}')
            time.sleep(1)
            continue

        # Cómo comprobar esto desde un método? 
        for i, fila in enumerate(tabla_oculta):
            for j, element in enumerate(fila):
                if respuesta == element:
                    tabla_oculta[i][j] = tabla[i][j]
                    if not valor1:
                        valor1 = tabla[i][j]
                        posicion1 = (i, j)
                    elif not valor2:
                        valor2 = tabla[i][j]
                        posicion2 = (i, j)
        limpiar_consola()
        mostrar_tabla(tabla_oculta)
        
        if valor1 and valor2:
            if valor1 != valor2:
                print(f"{Fore.RED}¡Incorrecto! 😰 Los elementos no coinciden.{Style.RESET_ALL}")
                time.sleep(1)            
                tabla_oculta[posicion1[0]][posicion1[1]] = posicion1[0] * len(tabla_oculta[0]) + posicion1[1] + 1
                tabla_oculta[posicion2[0]][posicion2[1]] = posicion2[0] * len(tabla_oculta[0]) + posicion2[1] + 1
                intentos -= 1
            else:
                is_win = comprobar_ganador(tabla_oculta)
                if is_win > 0:
                    print(f"{Fore.GREEN}¡Correcto! 🧠 Los elementos coinciden.{Style.RESET_ALL}")
                    time.sleep(1)
                elif is_win == 0:
                    print(f"{Fore.GREEN}¡Felicidades! 🎉 Has memorizado todos los elementos. 🥳{Style.RESET_ALL}")
                    time.sleep(2)
                    print(f"{Fore.GREEN}¡Pero esto todavía no termina! 💀{Style.RESET_ALL}")
                    time.sleep(2)
                    tiempo_memorizar(tabla, 'Memoriza los nombres, siglas y números de los elementos:', 10)
                    intentos = 0

            valor1 = None
            valor2 = None
            posicion1 = None
            posicion2 = None

        if intentos == 1:
            res = input(f'{Fore.RED}Perdiste! Quieres volver a intentarlo? sí(y)/no(n){Style.RESET_ALL} ')
            if res.lower() in ['n', 'no']:
                limpiar_consola()
                break
            else:
                intentos = 7
                tiempo_memorizar(tabla, 'Memoriza los nombres, siglas y números de los elementos:', 10)
                tabla_oculta = ocultar_tabla(tabla)

    if intentos == 0:
        limpiar_consola()
        juego_preguntas(tabla)

def juego_memoria():
    cantidad, cantidad_jugadores = presentation()
    tabla = generar_tabla(cantidad)

    if cantidad_jugadores > 1:
        mensaje_memorizar = 'Memorizar los elementos:'
    else:
        mensaje_memorizar = 'Memoriza los elementos:'

    tiempo_memorizar(tabla, mensaje_memorizar, cantidad)
    tabla_oculta = ocultar_tabla(tabla)
    # Lógica para jugador 1
    juego_jugador1(tabla_oculta, tabla)

    
if __name__ == "__main__":
    limpiar_consola()
    juego_memoria()