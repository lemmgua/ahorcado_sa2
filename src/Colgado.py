import random, time

#hang man


play_again="y"

while play_again=="y":
    user_lifes = 3
    points=0
    streak=0
    sample_words = []

    with open("src/words.txt", "r") as file:
        for i in file:
            sample_words.append(i)


    data_word = random.choice(sample_words)
    
    data_word=data_word[:len(data_word)-1]

    game_word = ""

    for i in range(len(data_word)):
        game_word += "_"

    play=True

    while play==True:
        
        print(data_word)
        user_guess = input(f"Intenta adviniar una letra:\n{game_word}\n")

        if user_guess.lower()==data_word.lower():
            points=points+game_word.count("_")*20

            print("Enhorabuena, has ganado.")
            print(f"Tú puntuación es de {points}")
            play=False

        for i in range(len(data_word)):
            print(f"racha {streak}")
            print(f"puntos {points}")
            if data_word[i] == user_guess:
                
                if streak>2 and user_guess not in game_word and user_guess in data_word:
                    points=points+15
                    streak=streak+1                 
                elif user_guess not in game_word and user_guess in data_word:
                    points=points+10
                    streak=streak+1 
                    
                game_word = game_word[:i] + user_guess + game_word[i+1:]
                       
            elif data_word[0].lower() == user_guess.lower():
                if streak>2 and user_guess not in game_word and user_guess in data_word:
                    points=points+15
                    streak=streak+1                 
                elif user_guess not in game_word and user_guess in data_word:
                    points=points+10
                    streak=streak+1 
                game_word = user_guess + game_word[1:]


        if data_word.lower().count(user_guess.lower()) == False:
            user_lifes -= 1
            print(f"Incorrecto. La palabra no contiene {user_guess}. Te quedan {user_lifes} vida/s.\n")
            points=points-20
            streak=0
            time.sleep(3)
        
        
        
        if user_lifes <= 0:
            print(f"Has perdido :(\nLa palabra era {data_word}\n")
            points=0
            print(f"Tú puntuación es de {points}")
            play=False
            
        if game_word.count("_") == False:
            print(game_word)
            time.sleep(1)
            print("Enhorabuena, has ganado.")
            print(f"Tú puntuación es de {points}")
            play=False
    play_again=input("¿Quieres volver a jugar? y/n\n").lower()    