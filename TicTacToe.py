def start():
    global time
    import time
    global score
    score = {1:0,2:0}

def init():
    global movemap
    movemap = {
        'a1':'0','b1':'1','c1':'2',
        'a2':'3','b2':'4','c2':'5',
        'a3':'6','b3':'7','c3':'8'
        }

    global winconditions
    winconditions = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]

    global symbols
    symbols = {1:'x',2:'o'}

    global movehist
    movehist = {1:[],2:[]}

    global board
    board = ['_'] * 9

def printboard():
    print(f"""
Player 1 - {symbols[1]}   Player 2 - {symbols[2]}

       a b c
    1 |\u0332{board[0]}|\u0332{board[1]}|\u0332{board[2]}|
    2 |\u0332{board[3]}|\u0332{board[4]}|\u0332{board[5]}|
    3 |\u0332{board[6]}|\u0332{board[7]}|\u0332{board[8]}|
    """)

def move(playerNum):
    while True:
        printboard()
        loc = str.lower(input(f'Player {playerNum} Enter Coordinates: '))
        if (loc in movemap.keys()) and board[int(movemap[loc])] == '_':            
            break
        else:
            print('Invalid Coordinates') 
    loc = int(movemap[loc])   
    board[loc] = symbols[playerNum]
    movehist[playerNum].append(loc)

def wincheck(playerNum):
    for i in range(len(winconditions)):
        y = 0
        for x in range(len(winconditions[i])):            
            if winconditions[i][x] in movehist[playerNum]:
                y += 1
        if y >= 3:
            printboard()
            score[playerNum] += 1
            print(f'Player {playerNum} Wins!') 
            time.sleep(1)        
            print(f'\n---Score---\nPlayer 1: {score[1]}\nPlayer 2: {score[2]}')
            time.sleep(1)
            return True

def game():
    while True:
        move(1)
        if wincheck(1):
            break

        move(2)    
        if wincheck(2):        
            break 

def main():
    while True:
        init()
        game() 
        i = input('\nRematch? ')
        if (str.lower(i) != 'yes') and (str.lower(i) != 'y'):
            break

start()
main()