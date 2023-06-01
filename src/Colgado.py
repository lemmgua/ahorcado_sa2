import random, time, database, helper
from rich import print
from rich.align import Align
from rich.panel import Panel
from sys import maxsize
from unidecode import unidecode

ajustes = helper.CargarAjustes()
esquema_colores = helper.ConseguirEsquemaDeColor(ajustes["color-scheme"])

PRIMARY_COLOR = esquema_colores["primary"]
SECONDARY_COLOR = esquema_colores["secondary"]
THIRD_COLOR = esquema_colores["third"]
difficulty = ajustes["difficulty"]
wantsToExit = False
play_again="y"
cheat_win = "001"

startText = f'''[b {SECONDARY_COLOR}]¡Bienvenido! ¿Qué desea hacer?[/b {SECONDARY_COLOR}]
[{THIRD_COLOR}][1] - Jugar una nueva partida
[2] - Ver puntuaciones
[3] - Ajustes de juego
[4] - Salir del juego[/{THIRD_COLOR}]
'''

#hang man

#main menu


while wantsToExit == False:
    helper.Clear()
    print(Panel(startText, title="Ahorcado", title_align="left", style=PRIMARY_COLOR+" b"))
    playerDecision = input()
    while playerDecision.isnumeric() == False or int(playerDecision) < 1 or int(playerDecision) > 4:
        playerDecision = input("No se ha introducido una opción correcta.\n"+startText)
    playerDecision = int(playerDecision)

    if playerDecision == 1:
        while play_again=="y":
            print(f"[b {PRIMARY_COLOR}]¿Cómo te llamas, jugador/a?[/b {PRIMARY_COLOR}]: ", end="")
            name = input()
            if difficulty == "easy":
                user_lifes = 10
            elif difficulty == "normal":
                user_lifes = 5
            elif difficulty == "hard":
                user_lifes = 3
            elif difficulty == "impossible":
                user_lifes = 1
            
            points = 0
            racha = 0
            mayor_racha = -maxsize #Numero infinitamente negativo
            letras_adivinadas = list()
            letras_utilizadas = list()

            data_word = unidecode(helper.ConseguirPalabraAleatoria())

            play=True

            while play:
                helper.Clear()

                game_word = ""

                for letra in data_word:
                    if letra in letras_adivinadas:
                        game_word += letra
                    else:
                        game_word += "_"
                
                #si ya no hay más letras por adivinar
                if game_word.count("_") == False:
                    print("[b green]Enhorabuena, has ganado![/b green]")
                    print(f"[b]Tú puntuación es de {points}![/b]")
                    play=False
                else:

                    """ print("[b green]Intenta adviniar una letra:[/b green]")
                    print(f"[b white]LETRAS YA UTILIZADAS: {', '.join(letras_utilizadas)}[/b white]") if len(letras_utilizadas) > 0 else None
                    print(game_word)
                    print(Padding(str(user_lifes))) """
                    print(Panel((f"[b {SECONDARY_COLOR}]Intenta adviniar una letra:[/b {SECONDARY_COLOR}]\n"+f"[b white]LETRAS YA UTILIZADAS: {', '.join(letras_utilizadas)}[/b white]\n" + game_word), title="Ahorcado", title_align="left", style=PRIMARY_COLOR))
                    user_guess = unidecode(input("> "))
                    if user_guess != "":
                        letras_utilizadas.append(user_guess)

                    #truco para ganar directamente
                    if user_guess == cheat_win:
                        game_word = data_word

                    #adivina palabra directamente
                    elif user_guess.lower()==data_word.lower():
                        points += game_word.count("_")*20
                        racha += 1

                        #print("Enhorabuena, has ganado.")
                        #print(f"Tú puntuación es de {points}")
                        play=False
                    
                    #si el jugador adivina una letra
                    elif user_guess in data_word:
                        letras_adivinadas.append(user_guess)
                        points += 10

                    #si la letra no está en la palabra
                    elif user_guess.lower() not in data_word.lower():
                        user_lifes -= 1
                        print(f"[b red]Incorrecto. La palabra no contiene {user_guess}. Te quedan {user_lifes} vida/s.[/b red]\n")
                        points -= 10
                        racha=0
                        helper.PulsaEnterParaContinuar()
                    
                    #Si el jugador se queda sin vidas
                    if user_lifes <= 0:
                        print(f"[red b]Has perdido :(\nLa palabra era {data_word}[/red b]\n")
                        points=0
                        print(f"[b blue]Tú puntuación es de {points}[/b blue]")
                        play=False

            print("[bold]¿Desea guardar su partida?[/bold]\n[green][1] - Guardar[/green]\n[red][2] - No guardar[/red]\n")
            response = input()
            while response.isnumeric() == False or int(response) < 1 or int(response) > 2:
                print("[underline bold red]La opción introducida no es correcta[/underline bold red]\n[bold]¿Desea guardar su partida?[/bold]\n[green][1] - Guardar[/green]\n[red][2] - No guardar[/red]\n")
                response = input()
            response = int(response)
            if response == 1:
                database.InsertarPuntuacion(name, points, racha)
            play_again_text = "¿Quieres volver a jugar?\n[green][Y] - Sí\n[red][N] - No[/red]"
            print(play_again_text)
            play_again = input().lower()
            while play_again != "y" and play_again != "n":
                helper.Clear()
                print("Esa opción no es correcta\n"+play_again_text)
                play_again = input().lower()
            if play_again == "n":
                wantsToExit = True
    #leer puntuaciones
    if playerDecision == 2:
        textoPregunta = '''[b blue]¿Qué puntuación deseas ver?[/b blue]
[1] - De jugador
[2] - La más alta
'''
        print(textoPregunta)
        playerDecision = input()
        while playerDecision.isnumeric() == False or int(playerDecision) < 1 or int(playerDecision) > 2:
            playerDecision = input("No se ha introducido una opción correcta\n"+textoPregunta)
        playerDecision = int(playerDecision)
        if playerDecision == 1:
            playerSearch = input("Introduce el nombre del jugador a buscar: > ")
            puntuaciones = database.LeerDatos(playerSearch)
            if puntuaciones == []:
                print("[red b]No se ha encontrado ninguna puntuación[/red b]")
            else:
                for i in puntuaciones:
                    print(i["nombre"] + " - " + str(i["score"]))
            helper.PulsaEnterParaContinuar()
    elif playerDecision == 3:
        helper.Clear()
        textoPregunta = f'''[b {SECONDARY_COLOR}] ¿Qué desea hacer? [/b {SECONDARY_COLOR}]
[{THIRD_COLOR}][1] - Cambiar esquema de colores
[2] - Cambiar nombre
[3] - Cambiar dificultad
[4] - Volver al menú principal
'''
        print(Panel(textoPregunta, title="Ajustes de juego", title_align="left", style=PRIMARY_COLOR))
        playerDecision = input()
        while playerDecision.isnumeric() == False or int(playerDecision) < 1 or int(playerDecision) > 3:
            playerDecision = input("No se ha introducido una opción correcta\n"+textoPregunta)
        playerDecision = int(playerDecision)

        if playerDecision == 1: #Cambiar esquema de colores
            helper.Clear()
            textoPregunta = f'''[b {SECONDARY_COLOR}] ¿Qué esquema desea? [/b {SECONDARY_COLOR}]
[{THIRD_COLOR}][1] - Predeterminado
[2] - Navidad
[3] - Neon
[4] - Oro
[5] - Frío'''
            print(Panel(textoPregunta, title="Esquema de color", title_align="left", style=PRIMARY_COLOR+" b"))
            playerDecision = input()
            while playerDecision.isnumeric() == False or int(playerDecision) < 1 or int(playerDecision) > 5:
                playerDecision = input("No se ha introducido una opción correcta\n"+textoPregunta)
            playerDecision = int(playerDecision)

            #Lógica de cambiar esquema de colores
            if playerDecision == 1:
                color_scheme = "default"
            elif playerDecision == 2:
                color_scheme = "xmas"
            elif playerDecision == 3:
                color_scheme = "neon"
            elif playerDecision == 4:
                color_scheme = "gold"
            elif playerDecision == 5:
                color_scheme = "cold"
            ajustes["color-scheme"] = color_scheme
            helper.GuardarAjustes(ajustes)

            esquema_colores = helper.ConseguirEsquemaDeColor(ajustes["color-scheme"])

            PRIMARY_COLOR = esquema_colores["primary"]
            SECONDARY_COLOR = esquema_colores["secondary"]
            THIRD_COLOR = esquema_colores["third"]

            startText = f'''[b {SECONDARY_COLOR}]¡Bienvenido! ¿Qué desea hacer?[/b {SECONDARY_COLOR}]
[{THIRD_COLOR}][1] - Jugar una nueva partida
[2] - Ver puntuaciones
[3] - Ajustes de juego
[4] - Salir del juego[/{THIRD_COLOR}]
'''
        elif playerDecision == 3:
            helper.Clear()
            textoPregunta = f'''[b {SECONDARY_COLOR}] ¿Qué dificultad desea? [/b {SECONDARY_COLOR}]
[{THIRD_COLOR}][1] - Fácil (10 Vidas)
[2] - Normal (5 Vidas)
[3] - Difícil (3 Vidas)
[4] - Imposible (1 vida)'''
            print(Panel(textoPregunta, title="Dificultad", title_align="left", subtitle="Dificultad actual: "+difficulty.capitalize(), subtitle_align="left", style=PRIMARY_COLOR + " b"))
            playerDecision = input()
            while playerDecision.isnumeric() == False or int(playerDecision) < 1 or int(playerDecision) > 4:
                print(Panel("No se ha introducido una opción correcta\n"+textoPregunta, title="Dificultad", title_align="left", style=PRIMARY_COLOR + " b"))
                playerDecision = input()
            playerDecision = int(playerDecision)

            if playerDecision == 1:
                ajustes["difficulty"] = "easy"
                difficulty = "easy"
            elif playerDecision == 2:
                ajustes["difficulty"] = "normal"
                difficulty = "normal"
            elif playerDecision == 3:
                ajustes["difficulty"] = "hard"
                difficulty = "hard"
            elif playerDecision == 4:
                ajustes["difficulty"] = "impossible"
                difficulty = "impossible"
            
            helper.GuardarAjustes(ajustes)

        elif playerDecision == 4: #Volver al menú
            continue

    #salir del juego
    elif playerDecision == 4:
        wantsToExit = True
helper.Clear()
print("[b red]Juego finalizado[/b red]")
