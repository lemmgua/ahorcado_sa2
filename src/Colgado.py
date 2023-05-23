import random, time, database, helper
from rich import print

startText = '''[b blue]¡Bienvenido! ¿Qué desea hacer?[/b blue]
[1] - Jugar una nueva partida
[2] - Ver puntuaciones
[3] - Salir del juego
'''

#hang man

#main menu
wantsToExit = False
play_again="y"
cheat_win = "001"

while wantsToExit == False:
    helper.Clear()
    print(startText)
    playerDecision = input()
    while playerDecision.isnumeric() == False or int(playerDecision) < 1 or int(playerDecision) > 3:
        playerDecision = input("No se ha introducido una opción correcta.\n"+startText)
    playerDecision = int(playerDecision)

    if playerDecision == 1:
        while play_again=="y":
            name=input("Dime tu nombre:\n")
            user_lifes = 5
            points=0
            streak=0
            sample_words = []
            letras_adivinadas = list()

            #with open("src/words.txt", "r") as file:
            #    for i in file:
            #        sample_words.append(i)


            #data_word = random.choice(sample_words)
            data_word = helper.ConseguirPalabraAleatoria()

            play=True

            while play:

                game_word = ""

                for letra in data_word:
                    if letra in letras_adivinadas:
                        game_word += letra
                    else:
                        game_word += "_"

                user_guess = input(f"Intenta adviniar una letra:\n{game_word}\n")

                #truco para ganar directamente
                if user_guess == cheat_win:
                    game_word = data_word

                #adivina palabra directamente
                elif user_guess.lower()==data_word.lower():
                    points += game_word.count("_")*20

                    #print("Enhorabuena, has ganado.")
                    #print(f"Tú puntuación es de {points}")
                    play=False

                #si la letra no está en la palabra
                elif user_guess.lower() not in data_word.lower():
                    user_lifes -= 1
                    print(f"Incorrecto. La palabra no contiene {user_guess}. Te quedan {user_lifes} vida/s.\n")
                    points -= 10
                    streak=0
                    time.sleep(3)
                
                #Si el jugador se queda sin vidas
                if user_lifes <= 0:
                    print(f"Has perdido :(\nLa palabra era {data_word}\n")
                    points=0
                    print(f"Tú puntuación es de {points}")
                    play=False
                
                #si ya no hay más letras por adivinar
                if game_word.count("_") == False:
                    print(game_word)
                    time.sleep(1)
                    print("[b green]Enhorabuena, has ganado![/b green]")
                    print(f"[b]Tú puntuación es de {points}![/b]")
                    play=False

            print("[bold]¿Desea guardar su partida?[/bold]\n[green][1] - Guardar[/green]\n[red][2] - No guardar[/red]\n")
            response = input()
            while response.isnumeric() == False or int(response) < 1 or int(response) > 2:
                print("[underline bold red]La opción introducida no es correcta[/underline bold red]\n[bold]¿Desea guardar su partida?[/bold]\n[green][1] - Guardar[/green]\n[red][2] - No guardar[/red]\n")
                response = input()
            response = int(response)
            if response == 1:
                database.InsertarPuntuacion(name, points, streak)
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
            print("[u b i]Pulsa INTRO para continuar[/u b i]", end="")
            input()
    #salir del juego
    if playerDecision == 3:
        wantsToExit = True
time.sleep(0.5)
print("Juego finalizado")
