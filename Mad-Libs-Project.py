def person_input():
    noun = input('Enter a name: ')
    return noun

def verb_input():
    verb = input('Enter a present tense verb: ')
    return verb

def main():
    person1 = person_input()
    verb1 = verb_input()
    person2 = person_input()
    verb2 = verb_input()
    print(f'Once upon a time, there was a person named {person1}, who loved to {verb1} all day.')
    print(f'One day, {person2} noticed that {person1} was constantly {verb1}ing. \n\n')
    print(f'{person2}: I think you should take a break from {verb1}ing, and try to {verb2} instead.')
    print(f'{person1}: Okay! I think I will try {verb2}ing instead.')

main()