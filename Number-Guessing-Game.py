from random import randint

MIN_NUM = 1
MAX_NUM = 10
guess_count = 0
allowed_guesses = 3
random_number: int = randint(MIN_NUM, MAX_NUM)

def take_input():
    while True:
        num_guess = input(f"Pick a number between {MIN_NUM} and {MAX_NUM}. ")
        if num_guess.isdigit():
            num_guess =int(num_guess)
            if num_guess >= MIN_NUM and num_guess <= MAX_NUM:
                break
            else:
                print('Number must be between 1 - 10')
        else:
            print('Please enter a valid number.')
    return num_guess


def main():
    guess_count = 0
    while guess_count <3:
        user_guess = take_input()
        if user_guess > random_number:
                print('Your guess is to high!')
                guess_count += 1
                print(f'Guesses Used: {guess_count}/{allowed_guesses}')
        elif user_guess < random_number:
                print('Your guess is to low!')
                guess_count +=1
                print(f'Guesses Used: {guess_count}/{allowed_guesses}')
        else:
                print('Correct!')
                break
    else:
        print('You Lose!')
main()