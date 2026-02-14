from enum import Enum, auto
import random

class Rank(Enum) :
    TWO = auto()
    THREE = auto()
    FOUR = auto()
    FIVE = auto()
    SIX = auto()
    SEVEN = auto()
    EIGHT = auto()
    NINE = auto()
    TEN = auto()
    JACK = auto()
    QUEEN = auto()
    KING = auto()
    ACE = auto()

class Suit(Enum) :
    DIAMONDS = auto()
    CLUBS = auto()
    HEARTS = auto()
    SPADES = auto()

class Card():
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        return f"{self.rank} of {self.suit}"
    
    def __eq__(self, other):
        if isinstance(other, Card):
            return self.rank == other.rank and self.suit == other.suit
        return False

ORDERED_DECK = [Card(r, s) for s in Suit for r in Rank]

        
class Deck():
    def __init__(self):
        ORDERED_DECK = [Card(r, s) for s in Suit for r in Rank]
        self.cards = ORDERED_DECK

    def __repr__(self):
        deck_string = ""
        for card in self.cards:
            deck_string += card.__repr__() + ", "
        return deck_string[:-2]
    
    def deck_size(self):
        return len(self.cards)

    def remove_card(self, card):
        if self.cards != []:
            if card in self.cards:
                index = self.cards.index(card)
                self.cards.pop(index)
                return
            raise Exception("card not in deck")
        raise Exception("no more cards in deck")

    def deal_card(self):
        if self.deck_size > 0:
            return self.cards.pop()
        raise Exception("no more cards in deck")
        
    def add_card(self, card):
        if card in self.cards:
            raise Exception(f"Card: {card} already in deck!")
        self.cards.append(card)

    #shuffles order of cards in list stored by deck object    
    def shuffle_deck(self):
        random.shuffle(self.cards)

