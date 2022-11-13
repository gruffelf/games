import random

print('--- Guessing Game! ---')

max = int(input('Guess out of: '))

answer = random.randint(0,max)
guesses = 0
game = True

while game:
    guess = int(input('Guess: '))
    guesses = guesses +1
    if guess > answer:
        print('Too high!')
    elif guess < answer:
        print('Too low!')
    elif guess == answer:
        game = False
print('You Win in '+str(guesses)+' guesses!')
quit()