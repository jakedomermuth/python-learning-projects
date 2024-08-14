from random import randint

MIN_ROLL = 1
MAX_ROLL = 6

def amount_of_dice():
    while True:
        dice = input('How many dice would you like to roll? (Type "quit" to exit) ')
        if dice.lower() == 'quit':
            return 'quit'
        elif dice.isdigit():
            dice = int(dice)
            if dice > 0:
                return dice
            else:
                print('The amount of dice must be greater than 0')
        else:
            print('Please enter a valid number of dice')

def main():
    while True:
        dice_to_roll = amount_of_dice()
        if dice_to_roll == 'quit':
            print('Thank you for playing!')
            break
        else:
            for i in range(dice_to_roll):
                random_roll = randint(MIN_ROLL, MAX_ROLL)
                print(random_roll, end=' ')
            print()

main()




