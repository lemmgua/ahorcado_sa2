import random, time

#hang man

play_again="y"

while play_again=="y":
    user_lifes = 3

    sample_words = ("Manzana", "Platano", "Pera", "Naranja", "Perejil", "Hamburguesa")

    data_word = random.choice(sample_words)

    game_word = ""

    for i in range(len(data_word)):
        game_word += "_"

    while True:
        print("\033c", end="")
        
        user_guess = input(f"Intenta adviniar una letra:\n{game_word}\n")
        
        if user_guess.lower()==data_word.lower():
            print("Enhorabuena, has ganado.")
            break

        for i in range(len(data_word)):
            if data_word[i] == user_guess:
                game_word = game_word[:i] + user_guess + game_word[i+1:]
            elif data_word[0].lower() == user_guess.lower():
                game_word = user_guess + game_word[1:]
        
        if data_word.lower().count(user_guess.lower()) == False:
            user_lifes -= 1
            print(f"Incorrecto. La palabra no contiene {user_guess}. Te quedan {user_lifes} vida/s.\n")
            time.sleep(3)
        
        if user_lifes <= 0:
            print(f"Has perdido :(\nLa palabra era {data_word}\n")
            break

        if game_word.count("_") == False:
            print(game_word)
            time.sleep(1)
            print("Enhorabuena, has ganado.")
            break
    play_again=input("¿Quieres volver a jugar? y/n\n").lower()