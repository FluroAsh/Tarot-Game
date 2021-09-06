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

data_structure = {"nhits": 0, "cards": [{"name_short": "string", "name": "string", "value": "string", "value_int": 0, "type": "major", "meaning_up": "string", "meaning_rev": "string", "desc": "string"}]}

# Gets our first card!
# Need to look into how to implement this so we can assign it to our card class in a 3-card spread scenario... 
# add an extra [] if you want to get a specific element in the list, i.e. ["desc"]
print(data["cards"][0])

intro = "Welcome to Jasiah's Mystical Tarot Reading!"

# def recursive_items(data):
#     for key, value in data.items():a
#         if type(value) is dict:
#             yield from recursive_items(value)
#         else:
#             yield (key, value)

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