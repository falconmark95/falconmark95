# Piece: Comparing last guess with current guess
# initializing variables
rand_int = 50
saved_guess = [61]

# user input
user_guess = int(input("Guess the random integer between 1 and 100: "))
saved_guess.append(user_guess)

# while loop process
if rand_int - 10 <= user_guess <= rand_int + 10:
    print('WARM!! Almost there!')
    while rand_int - 10 <= user_guess <= rand_int + 10:
        user_guess = int(input("Guess the random integer between 1 and 100: "))
        saved_guess.append(user_guess)
        if abs(saved_guess[-2] - rand_int) > abs(user_guess - rand_int):  # Checking guess is closer than last
            print("Warmer than your last choice!")
            if user_guess == saved_guess[-2]:  # User guesses same number again
                print('You already guessed that number')
                continue
            elif user_guess == rand_int:  # Random number is guessed
                print("You guessed the number!")
                break
            continue
        elif user_guess == saved_guess[-2]:  # User guesses same number again
            print('You already guessed that number')
            continue
        elif user_guess == rand_int:  # Random number is guessed
            print("You guessed the number!")

        elif abs(saved_guess[-2] - rand_int) < abs(user_guess - rand_int):
            print("Colder than the last choice!")
            continue
    print("You're back in the cold zone!")
