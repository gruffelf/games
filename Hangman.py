from random_word import RandomWords
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
guessnum = 10
word = RandomWords().get_random_word()
letters = list(word)
answer = '_ '*len(letters)
letters_guessed = ''
while True:
    print('\n'+answer)
    print('Guessed Letters: '+letters_guessed)
    print('Guesses Remaining: '+str(guessnum))
    if guessnum <= 0:
        print('You Lost! The Word Was: '+word)
        quit()
    elif answer.replace(' ','') == word:
        print('You Win! The Word Was: '+word)
        quit()
    guess = str.lower(input('Guess next letter: '))
    if guess not in alphabet:
        print('\nInvalid Character, Try Again\n')      
    elif guess in letters:        
        numbers = []
        for idx, values in enumerate(letters):
            if values == guess:
                numbers.append(idx*2)        
        for i in range(len(numbers)):                  
            answer = answer[:numbers[i]]+guess+answer[numbers[i]+1:]        
    elif guess not in letters:
        if guess not in letters_guessed:
            letters_guessed += (guess+', ')
            guessnum = guessnum - 1

        print('Wrong Guess')
    