import time
import random
import json
from typing import Type
import urllib.request as request

'''
Card names, descriptions, and divinatory meanings according to AE Waite's Pictorial Key to the Tarot (1910), 
the companion to the Rider-Waite-Smith (RWS) deck upon which most newer decks are based
'''

# Pull data from our rws-cards-api
with request.urlopen('https://rws-cards-api.herokuapp.com/api/v1/cards') as response:       
    if response.getcode() == 200:
        source = response.read()
        data = json.loads(source)
    else:
        print('An error occurred while attempting to retrieve data from the API.')

intro = "Welcome to Ashley's Mystical Tarot Reading!"
print("         _...._")
print("       .`      `.")
print("      / ***      \         The Crystal Ball")
print("     : **         :         says.........")
print("     :            :        You don't really")
print("      \          /       believe in fortunes")
print("       `-.,,,,.-'              do you?")
print("        _(    )_")
print("       )        (")
print("      (          )")
print("       `-......-`lc\n")


class Player:
    def __init__(self, name):
        self.name = name 

class Card:
    random_cards = []
    meaning_u_r = 0
    def __init__(self, name, name_short, value, value_int, identifier, meaning_up, meaning_rev, desc):
        self.name = name
        self.name_short = name_short
        self.value = value 
        self.value_int = value_int
        self.identifier = identifier 
        self.meaning_up = meaning_up
        self.meaning_rev = meaning_rev
        self.desc = desc
    
    def get_cards():
        for i in range(3): 
            random_i = random.randint(0,77)
            # Add code to PREVENT duplicates!!
            Card.random_cards.append(data['cards'][random_i])

    def up_rev():
        Card.meaning_u_r = random.randint(1,16)


print('\t' + intro + '\n\n')
player_name = Player(str(input("What is your name?: ")))
time.sleep(1)
print(">>> Welcome " + player_name.name.title() + " may the cards bless you with good fortune...\n")
time.sleep(3)

# Get's 3 RANDOM cards & their ATTRIBUTES
Card.get_cards()

# Initialize our randomly generated cards (between 1-78)
card1 = Card(Card.random_cards[0]["name"], Card.random_cards[0]["name_short"], Card.random_cards[0]["value"], Card.random_cards[0]["value_int"], Card.random_cards[0]["type"], Card.random_cards[0]["meaning_up"], Card.random_cards[0]["meaning_rev"], Card.random_cards[0]["desc"])
card2 = Card(Card.random_cards[1]["name"], Card.random_cards[1]["name_short"], Card.random_cards[1]["value"], Card.random_cards[1]["value_int"], Card.random_cards[1]["type"], Card.random_cards[1]["meaning_up"], Card.random_cards[1]["meaning_rev"], Card.random_cards[1]["desc"])
card3 = Card(Card.random_cards[2]["name"], Card.random_cards[2]["name_short"], Card.random_cards[2]["value"], Card.random_cards[2]["value_int"], Card.random_cards[2]["type"], Card.random_cards[2]["meaning_up"], Card.random_cards[2]["meaning_rev"], Card.random_cards[2]["desc"])

# -- Fortune Teller Text

## CARD 1
print(">>> The PAST...\n")
time.sleep(3)

Card.up_rev() 
if Card.meaning_u_r <= 10: # Logic to determine up or reverse orientation -- 66% chance to get up
    print('[' + card1.name.upper() + ']' + '\n' + card1.desc + '\n\n' + card1.meaning_up + '\n')
else:
    print('[' + card1.name.upper()  + ']' + '\n' + card1.desc + '\n\n' + '**REVERSED: ' + card1.meaning_rev + '\n')
time.sleep(15)

print(">>> Fate has a sense of humour, it seems...\n")
time.sleep(8)

## CARD 2 
print(">>> The PRESENT...\n")
time.sleep(3)

Card.up_rev() # Refresh our meaning_u_r variable
if Card.meaning_u_r <= 10:
    print('[' + card2.name.upper() + ']' + '\n' + card2.desc + '\n\n' + card2.meaning_up + '\n')
else:
    print('[' + card2.name.upper() + ']' + '\n' + card2.desc + '\n\n' + '**REVERSED: ' + card2.meaning_rev + '\n')
time.sleep(15)

print(">>> Hmmm... Interesting...\n")
time.sleep(10)

## CARD 3
print(">>> Your third, and FINAL card... The FUTURE!\n")
time.sleep(3)

Card.up_rev()
if Card.meaning_u_r <= 10:
    print('[' + card3.name.upper()  + ']' + '\n' + card3.desc + '\n\n' + card3.meaning_up + '\n')
else:
    print('[' + card3.name.upper()  + ']' + '\n' + card3.desc + '\n\n' + '**REVERSED: ' + card3.meaning_rev + '\n')
time.sleep(15)

print('----------------------------------------------------------------------------------------------------------------------')
print("***Though your fate is in the cards, your choices define your path... Let them guide you to your final destination.***")

# Time out after 30 seconds
time.sleep(30)