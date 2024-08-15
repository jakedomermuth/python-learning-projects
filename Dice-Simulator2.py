import random

def amount_of_rolls(amount: int =2) -> list[int]:
    total_sum = 0
    if amount <= 0:
        raise ValueError

    rolls: list[int] = []
    for i in range(amount):
        random_value: int = random.randint(1, 6)
        rolls.append(random_value)
        total_sum += random_value

    return rolls, total_sum

def main():
    while True:
        user_input = input('How many dice would you like to roll? (Type quit to exit). ')
        try:
            if user_input.lower() == 'quit':
                print('Thank you for playing!')
                break

            print(*amount_of_rolls(int(user_input)), sep=', Total ')
        except ValueError:
            print('Please enter a valid number')


if __name__ == '__main__':
    main()


