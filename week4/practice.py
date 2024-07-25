name = 'kesha'
new_name = ''
for c in name:
    if c == 'e':
        c = '3'
    if c == 's':
        c = '$'
    if c == 'a':
        c = '@'
    new_name += c
    
print(new_name)
# ---------------------------------------------------------------------------------------------------------
import random
numbers = ['1','2','3','4','5','6','7','8','9','10']
def game():
    userSelection = input("Welcome to Ria's Guessing Game! Guess a number between 1 and 10:     ")
    computerSelection = random.choice(numbers)
    # using items in for loop causes it to end after 10 tries
    for items in numbers:
        if computerSelection == userSelection:
            print('')
            print(f'Correct! The number was {computerSelection}')
            print('')
            break
        else:
            print('')
            print("Nope, that's not it. Try again!")
            userSelection = input("Enter a number between 1 and 10:   ")

game()