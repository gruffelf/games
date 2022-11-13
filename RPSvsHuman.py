import pwinput

inputs = {'r':'rock','p':'paper','s':'scissors'}
print('--- Rock Paper Scissors ---\nInputs : \nr - rock\np - papers\ns - scissors')

def guessing(num):
    guessing = True
    while guessing:
        p = pwinput.pwinput(prompt=f'Player {num}: ')

        if p in inputs.keys(): 
            guessing = False
            return list(inputs.keys()).index(p)+1
        else:
            print('Invalid Input')
game = True
while game:
    p1 = guessing('1')
    p2 = guessing('2')

    if p1 == p2:
        print(f'\nPlayer 1: {list(inputs.values())[p1-1]}\nPlayer 2: {list(inputs.values())[p2-1]}\n!!! Draw !!!')
    elif p1 - p2 == 1 or p1 - p2 == -2:
        print(f"\nPlayer 1: {list(inputs.values())[p1-1]}\nPlayer 2: {list(inputs.values())[p2-1]}\n!!! Player 1 Wins !!!")
    else:
        print(f"\nPlayer 1: {list(inputs.values())[p1-1]}\nPlayer 2: {list(inputs.values())[p2-1]}\n!!! Player 2 wins !!!")

    
    again = input("\nPlay Again? ")
    if str.lower(again) not in ['y','yes']:
        game = False

quit()