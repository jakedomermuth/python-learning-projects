import random

word_bank = ['secret', 'cat', 'phone', 'bottle']


def run_game():
    name = input('What is your name? ')
    print(f'Hello {name}, Good Luck!')
    word = random.choice(word_bank)

    guessed = ''  # Store guessed letters here
    tries = 3

    while tries > 0:
        blanks = 0
        print('Word: ', end='')
        for char in word:
            if char in guessed:
                print(char, end='')
            else:
                print('_', end='')
                blanks += 1

        print()

        if blanks == 0:
            print('Congrats, you won!')
            break

        guess = input('Guess a letter: ').lower()
        if guess in guessed:
            print(f'You already used "{guess}".')
            continue

        guessed += guess

        if guess not in word:
            tries -= 1  # Decrement tries if guess is incorrect
            print(f'Incorrect! {tries} tries left.')

            if tries == 0:
                print(f'You Lose! The word was "{word}".')
                break


if __name__ == '__main__':
    run_game()

