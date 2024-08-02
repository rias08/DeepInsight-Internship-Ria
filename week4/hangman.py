import random

fourWordList = ['Also', 'Able',	'Acid', 'Aged',	'Away',	'Baby', 'Back',	'Bank', 'Been', 'Ball',	'Base',	'Busy',
                'Bend',	'Bell',	'Bird', 'Come',	'Came',	'Calm', 'Card',	'Coat',	'City', 'Chat',	'Cash',	'Crow',
                'Cook',	'Cool',	'Dark', 'Each', 'Evil',	'Even', 'Ever',	'Face',	'Fact', 'Four',	'Five',	'Fair',
                'Feel',	'Fell',	'Fire', 'Fine',	'Fish',	'Game', 'Gone',	'Gold',	'Girl', 'Have',	'Hair',	'Here',
                'Hear',	'Into',	'Iron', 'Jump',	'Kick',	'Kill', 'Life',	'Like',	'Love', 'Main',	'Move',	'Meet',
                'More',	'Nose',	'Near', 'Open',	'Only',	'Push', 'Pull',	'Sell',	'Sale'
]

sixWordList = ["Abroad", 'Casual',	'Around',	'Couple', 'Accept',	'Caught',	'Arrive',	'Course',
               'Access', 'Centre',	'Artist',	'Covers', 'Across',	'Centum',	'Aspect',	'Create',
               'Acting', 'Chance',	'Assess',	'Credit', 'Action',	'Change',	'Assist',	'Crisis',
               'Active', 'Charge',	'Assume',   'Custom', 'Actual',	'Choice',	'Attack',	'Damage',
               'Advice', 'Choose',	'Attend',	'Danger', 'Advise',	'Chosen',	'August',	'Dealer',
               'Affect', 'Church',	'Author',	'Debate', 'Afford',	'Circle',	'Avenue',	'Decade',
               'Afraid', 'Client',	'Backed',	'Decide', 'Agency',	'Closed',	'Barely',	'Defeat',
               'Agenda', 'Closer',	'Battle',	'Defend', 'Almost',	'Coffee',	'Beauty',	'Define',
               'Always', 'Column',	'Became',	'Degree', 'Amount',	'Combat',	'Become',	'Demand',
               'Animal', 'Coming',	'Before',	'Depend', 'Annual',	'Common',	'Behalf',	'Deputy',
               'Answer', 'Comply',	'Behind',	'Desert', 'Anyone',	'Copper',	'Belief',	'Design',
               'Anyway', 'Corner',	'Belong',	'Desire', 'Appeal',	'Costly',	'Beaker',	'Detail',
               'Appear', 'County',	'Better',	'Detect', 'Beyond',	'Budget',	'During',	'Device',
               'Bishop', 'Burden',	'Easily',	'Differ', 'Border',	'Bureau',	'Eating',	'Dinner',
               'Bottle', 'Button',	'Editor',	'Direct', 'Bottom',	'Camera',	'Effect',	'Doctor',
               'Bought', 'Cancer',	'Effort',	'Dollar', 'Branch',	'Cactus',	'Eighth',	'Domain',
               'Breath', 'Carbon',	'Either',	'Double', 'Bridge',	'Career',	'Eleven',	'Driven',
               'Bright', 'Castle',	'Emerge',	'Driver']

def fourWord():
    word = random.choice(fourWordList)
    print(word)

def sixWord():
    word = random.choice(sixWordList)
    print(word)

print("Welcome to Ria's Hangman Game!")
lettersInWord = input("How many letters would you like in your word? (4 or 6)  - ")
if lettersInWord == '4':
    print('')
    print(" __ __ __ __                      +------")
    print("                                  |   |")
    print("                                  |")
    print("                                  |")
    print("                                  |")
    print('')
    fourWord()
else:
    print('')
    print(" __ __ __ __ __ __                     +------")
    print("                                       |   |")
    print("                                       |")
    print("                                       |")
    print("                                       |")
    print('')
    sixWord()


def game():
    print()


