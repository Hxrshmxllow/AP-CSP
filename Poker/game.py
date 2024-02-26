import random
from logic import *

class Card:
    def __init__(self):
        Card.suit = ""
        Card.number = ""

numbers = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
suits = ["Spade", "Diamond", "Heart", "Club"]
deck = []

for suit in suits:
    for number in numbers:
        card = Card()
        card.suit = suit
        card.number = number
        deck.append(card)
        card = Card()

communityCards = []
playerCards = []
computerCards = []

round = 1
while round < 4:
    if round == 1:
        for i in range(2):
            card = random.choice(deck)
            deck.remove(card)
            playerCards.append(card)
            card = Card()
            card = random.choice(deck)
            deck.remove(card)
            computerCards.append(card)
            card = Card()
        for i in range(3):
            card = random.choice(deck)
            deck.remove(card)
            communityCards.append(card)
            card = Card()
    else:
        card = random.choice(deck)
        deck.remove(card)
        communityCards.append(card)
        card = Card()
    round += 1

check(communityCards, playerCards, computerCards)

print("Player:")
for card in playerCards:
    print(card.suit + card.number)
print()
print("Computer:")
for card in computerCards:
    print(card.suit + card.number)
print()
print("Community:")
for card in communityCards:
    print(card.suit + card.number)