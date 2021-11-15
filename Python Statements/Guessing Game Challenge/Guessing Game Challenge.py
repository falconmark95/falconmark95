from random import randint

# ~ Guessing Game Challenge ~
# This exercise you will be using while loops to create this game
"""
The Challenge:

Write a program that picks a random integer from 1 to 100, and has players guess the number. The rules are:

If a player's guess is less than 1 or greater than 100, say "OUT OF BOUNDS"
On a player's first turn, if their guess is
within 10 of the number, return "WARM!"

further than 10 away from the number, return "COLD!"

On all subsequent turns, if a guess is
closer to the number than the previous guess return "WARMER!"

farther from the number than the previous guess, return "COLDER!"

When the player's guess equals the number, tell them they've guessed correctly and how many guesses it took!

You can try this from scratch, or follow the steps outlined below. A separate Solution notebook has been provided.
Good luck!
"""
rand_int = randint(1, 100) # Generating random number
# rand_int = 50 # Set random number for testing purposes
num_guess = 0 # Variable set if player gets first guess correct
saved_guess = [] # Dynamic list created to keep tally choices and amount of choices made
print("Welcome to the Guessing Game!\n"
      "1.) Guess a number between 0 - 100\n"
      "2.)"
      " If the number is out of bounds you will be prompted with an error message and to try again\n")
user_guess = int(input("Guess the random integer between 1 and 100: "))
num_guess += 1

if user_guess == rand_int: # First guess is correct
    print("\n~~ Congratulations you have guessed the mystery number! ~~")
    print("{1:>15}Amount guessed: {0}{1:<15}".format(num_guess, ' '))
else:
    print("That is not the random integer")
    saved_guess.append(user_guess)

while user_guess != rand_int:
    if user_guess < 1 or user_guess > 100: # Check if out of bounds
        print("Choice is out of bounds try again.")
        user_guess = int(input("\nGuess the random integer between 1 and 100: "))
        saved_guess.append(user_guess)
        num_guess += 1

    elif rand_int - 10 <= user_guess <= rand_int + 10:  # If guess is within 10 of random int
        print('WARM!! Almost there!')
        while rand_int - 10 <= user_guess <= rand_int + 10:
            user_guess = int(input("\nGuess the random integer between 1 and 100: "))
            saved_guess.append(user_guess)
            num_guess += 1
            if abs(saved_guess[-2] - rand_int) > abs(user_guess - rand_int):  # Checking guess is closer than last
                print("Warmer than your last choice!")
                if user_guess == saved_guess[-2]:  # User guesses same number again
                    print('You already guessed that number')
                    continue
                elif user_guess == rand_int:  # Random number is guessed
                    print("\n~~ Congratulations you have guessed the mystery number! ~~")
                    print("{1:>15}Amount guessed: {0}{1:<15}".format(num_guess, ' '))
                    break
                continue
            elif user_guess == saved_guess[-2]:  # User guesses same number again
                print('You already guessed that number')
                continue
            elif user_guess == rand_int:  # Random number is guessed
                print("\n~~ Congratulations you have guessed the mystery number! ~~")
                print("{1:>15}Amount guessed: {0}{1:<15}".format(num_guess, ' '))
                exit(0)
                break
            elif abs(saved_guess[-2] - rand_int) < abs(user_guess - rand_int): # Checking guess is farther than last
                print("Colder than the last choice!")
                continue

    else: # IF user guess is outside of 10 from rand_int
        print('COLD! Try again.')
        user_guess = int(input("\nGuess the random integer between 1 and 100: "))
        saved_guess.append(user_guess)
        num_guess += 1
        if abs(saved_guess[-2] - rand_int) > abs(user_guess - rand_int):
            print("Warmer than your last choice!")
            continue
        else:
            print('Colder than last choice')
