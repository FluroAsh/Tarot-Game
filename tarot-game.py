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

random_cards = []

# Get's 3 RANDOM cards & their ATTRIBUTES
for i in range(3): 
    random_i = random.randint(0,78)
    # Add code to PREVENT duplicates!!
    random_cards.append(data['cards'][random_i])

class Player:
    def __init__(self, name):
        self.name = name 


class Card:
    def __init__(self, name, name_short, value, value_int, identifier, meaning_up, meaning_rev, desc):
        self.name = name
        self.name_short = name_short
        self.value = value 
        self.value_int = value_int
        self.identifier = identifier 
        self.meaning_up = meaning_up
        self.meaning_rev = meaning_rev
        self.desc = desc

print('\t' + intro + '\n\n')
player_name = Player(input("What is your name?: "))
time.sleep(1)
print("Welcome " + player_name.name + " may the cards bless you with good fortune...\n")
time.sleep(3)

# Initialize our randomly generated cards (between 1-78)
card1 = Card(random_cards[0]["name"], random_cards[0]["name_short"], random_cards[0]["value"], random_cards[0]["value_int"], random_cards[0]["type"], random_cards[0]["meaning_up"], random_cards[0]["meaning_rev"], random_cards[0]["desc"])
card2 = Card(random_cards[1]["name"], random_cards[1]["name_short"], random_cards[1]["value"], random_cards[1]["value_int"], random_cards[1]["type"], random_cards[1]["meaning_up"], random_cards[1]["meaning_rev"], random_cards[1]["desc"])
card3 = Card(random_cards[2]["name"], random_cards[2]["name_short"], random_cards[2]["value"], random_cards[2]["value_int"], random_cards[2]["type"], random_cards[2]["meaning_up"], random_cards[2]["meaning_rev"], random_cards[2]["desc"])

# -- Fortune Teller Text
print("Your first card...\n")
time.sleep(3)
print(card1.name + '\n' + card1.desc + '\n')
time.sleep(3)

print("Fate has a sense of humour, it seems...\n")
time.sleep(8)

print("Your second card...\n")
time.sleep(3)
print(card2.name + '\n' + card2.desc + '\n')
time.sleep(3)

print("Hmmm... Interesting...\n")
time.sleep(8)

print("Your third, and FINAL card...\n ")
time.sleep(3)
print(card3.name + '\n' + card3.desc + '\n')

time.sleep(8)
print("***Though your fate is in the cards, your choices define your path... Let them guide you to your final destination.***")

time.sleep(30)