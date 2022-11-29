import random

player_name = input("Hello, What's your name?")

difficulty = input("Easy or Hard?")

if difficulty == "Easy":
    print('Huh, this is gonna be to easy for me!!')
    number = int(input("Choose een number between 1 and 10"))
    number_of_guesses = 0
    print('Okay! '+ player_name + ' I will guess your number in 5 tries!')
    high_number = 10;
    low_number = 1;
    first_guess = random.randint(low_number, high_number)

    while number_of_guesses < 5:
        guess = int(first_guess)
        number_of_guesses += 1
        if guess < number:
            print('My guess (' + str(guess) + ') was too low')
            low_number = guess
            low_number += 1
            if low_number <= high_number:
                first_guess = random.randint(low_number, high_number)
        if guess > number:
            print('My guess (' + str(guess) + ') was too high')
            high_number = guess
            high_number -= 1
            if high_number >= low_number:
                first_guess = random.randint(low_number, high_number)
        if guess == number:
            break
    if guess == number:
        print('I am way better then you noob, I guessed it in ' + str(number_of_guesses) + ' tries!')
    else:
        print('I am a LOSER, The number was ' + str(number))

if difficulty == "Hard":
    print('Okayyyy, you are giving me a challenge!')
    number = int(input("Choose een number between 1 and 100"))
    number_of_guesses = 0
    print('Okay! '+ player_name + ' I will guess your number in 10 tries!')
    high_number = 100;
    low_number = 1;
    first_guess = random.randint(low_number, high_number)

    while number_of_guesses < 10:
        guess = int(first_guess)
        number_of_guesses += 1
        if guess < number:
            print('My guess (' + str(guess) + ') was too low')
            low_number = guess
            low_number += 1
            if low_number <= high_number:
                first_guess = random.randint(low_number, high_number)
        if guess > number:
            print('My guess (' + str(guess) + ') was too high')
            high_number = guess
            high_number -= 1
            if high_number >= low_number:
                first_guess = random.randint(low_number, high_number)
        if guess == number:
            break
    if guess == number:
        print('This was to easy! ' + str(number_of_guesses) + ' tries!')
    else:
        print('I lost this time but will win the next one! The number was ' + str(number))
