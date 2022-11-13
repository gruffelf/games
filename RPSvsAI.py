import random,time

game = (["0","r","p","s"])

print("-----Rock Paper Scissors-----")

playing = True
score = [0,0]
games = int(input("Play First to: "))
while playing == True:
    usr = input("Your Move (r/p/s): ")

    usr = game.index(usr)

    ai = random.randint(1,3)

    print("AI chose " + game[ai])

    if usr == ai:
        print("Draw!")
    elif usr - ai == 1 or usr - ai == -2:
        print("You win!")
        score[0]=score[0]+1
    else:
        print("AI wins!")
        score[1]=score[1]+1

    time.sleep(0.5)
    print(f"""Scoreboard:
    You: {score[0]}
    AI: {score[1]}
    """)
    time.sleep(0.5)
    if score[0] >= games:
        print("You have won the game!")
        break
    elif score[1] >= games:
        print('AI has won the game!')
        break


