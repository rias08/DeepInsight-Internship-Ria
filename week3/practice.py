sentence = 'Hello World'
upper = True
new_sentence = ''
for char in sentence:
    if upper:
        char = char.upper()
        upper = False
    else:
        char = char.lower()
        upper = True
    new_sentence += char
    
print(new_sentence)
#----------------------------------------------------------------------------------------#

import random
options = ["Rock", "Paper", "Scissors"]
play_again = []

def game():
    userSelection = input("Choose a sign: ")
    computerSelection = random.choice(options)

    print("You chose: ", userSelection)
    print("Computer chose: ", computerSelection)

    if userSelection == computerSelection:
        print("It's a tie!")
    elif userSelection == "Rock" and computerSelection == "Scissors":
        print("You win!")
    elif userSelection == "Paper" and computerSelection == "Rock":
        print("You win!")
    elif userSelection == "Scissors" and computerSelection == "Paper":
        print("You win!")
    else:
        print("Computer wins!")

    play_again = input('Would you like to try again? (yes/no)')
game()

while play_again == 'yes':
    game()
else:
    print("Thank you for playing!")