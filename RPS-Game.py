choices = ['rock', 'paper', 'scissors', 'quit']
import random

def user_input():
    while True:
        user_input = input('Select: rock, paper, or scissors (Enter quit to exit) ')
        user_choice = user_input.lower()
        if user_choice in choices:
            break
        else:
            print('Please enter a valid option! ')
    return user_choice


def main():
    print('Welcome to RPC!')
    user_score = 0
    ai_score = 0
    while True:
        user_pick = user_input()
        if user_pick == 'quit':
            break
        ai_input = random.choice(choices)
        print(f'You: {user_pick}')
        print(f'Opponet: {ai_input}')

        if user_pick == ai_input:
            print('Tie!')
        elif user_pick == 'rock' and ai_input == 'scissors':
            print('You Win!')
            user_score += 1
        elif user_pick == 'paper' and ai_input == 'rock':
            print('You Win!')
            user_score += 1
        elif user_pick == 'scissors' and ai_input == 'paper':
            print('You Win')
            user_score += 1
        else:
            print('You Lose')
            ai_score += 1
        print(f'Your score: {user_score} \n Opponet Score: {ai_score}', sep='')
    print('Thank you for playing!')

main()

