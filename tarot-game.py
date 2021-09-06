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

intro = "Welcome to Jasiah's Mystical Tarot Reading!"

random_cards = []

# Get's 3 RANDOM cards & their ATTRIBUTES
for i in range(3): 
    random_i = random.randint(1,78)
    random_cards.append(data['cards'][random_i])


class Player:
    def __init__(self, name):
        self.name = name 


class Card:
    def __init__(self, name, name_short, value, value_int, suit, identifier, meaning_up, meaning_rev, desc):
        self.name = name
        self.name_short = name_short
        self.value = value 
        self.value_int = value_int
        self.suit = suit 
        self.identifier = identifier 
        self.meaning_up = meaning_up
        self.meaning_rev = meaning_rev
        self.desc = desc

player_name = Player(input("What is your name? "))

# Initialize our randomly generated cards (between 1-78)
card1 = Card(random_cards[0]["name"], random_cards[0]["name_short"], random_cards[0]["value"], random_cards[0]["value_int"], random_cards[0]["suit"], random_cards[0]["type"], random_cards[0]["meaning_up"], random_cards[0]["meaning_rev"], random_cards[0]["desc"])
card2 = Card(random_cards[1]["name"], random_cards[1]["name_short"], random_cards[1]["value"], random_cards[1]["value_int"], random_cards[1]["suit"], random_cards[1]["type"], random_cards[1]["meaning_up"], random_cards[1]["meaning_rev"], random_cards[1]["desc"])
card3 = Card(random_cards[2]["name"], random_cards[2]["name_short"], random_cards[2]["value"], random_cards[2]["value_int"], random_cards[2]["suit"], random_cards[2]["type"], random_cards[2]["meaning_up"], random_cards[2]["meaning_rev"], random_cards[2]["desc"])


# --- Tests --- #
print(card1.name + '\n' + card1.desc)
print(card2.name + '\n' + card2.desc)
print(card3.name + '\n' + card3.desc)
time.sleep(5)