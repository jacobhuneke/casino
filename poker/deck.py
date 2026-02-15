from enum import Enum, auto
import random

#Rank and Suit enums for cards
class Rank(Enum) :
    TWO = 2, "Two"
    THREE = 3, "Three"
    FOUR = 4, "Four"
    FIVE = 5, "Five"
    SIX = 6, "Six"
    SEVEN = 7, "Seven"
    EIGHT = 8, "Eight"
    NINE = 9, "Nine"
    TEN = 10, "Ten"
    JACK = 11, "Jack"
    QUEEN = 12, "Queen"
    KING = 13, "King"
    ACE = 14, "Ace"

class Suit(Enum) :
    DIAMONDS = 1, "Diamonds"
    CLUBS = 2, "Clubs"
    HEARTS = 3, "Hearts"
    SPADES = 4, "Spades"

#card class, saves one rank and one suit enum
class Card():
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        return f"{self.rank.value[1]} of {self.suit.value[1]}"
    
    def __eq__(self, other):
        if isinstance(other, Card):
            return self.rank == other.rank and self.suit == other.suit
        return False
    
    def get_rank(self):
        return self.rank.value
    
    def get_suit(self):
        return self.suit.value
    
#creates a deck with cards in order
ORDERED_DECK = [Card(r, s) for s in Suit for r in Rank]

#Deck class creates an ordered deck and saves it to a cards variable
#helper functions to get the number of cards in the deck,
#to remove a specific card from the deck,
#To pop the top card off the deck (deal a card)
#To add cards back into the deck
#and to shuffle the deck. These all work on the cards variable of the deck
class Deck():
    def __init__(self):
        ORDERED_DECK = [Card(r, s) for s in Suit for r in Rank]
        self.cards = ORDERED_DECK

    def __repr__(self):
        deck_string = ""
        for card in self.cards:
            deck_string += card.__repr__() + ", "
        string = deck_string.removesuffix(", ")
        return string
    
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
        if self.deck_size() > 0:
            return self.cards.pop()
        raise Exception("no more cards in deck")
        
    def add_card(self, card):
        if card in self.cards:
            raise Exception(f"Card: {card} already in deck!")
        self.cards.append(card)

    #shuffles order of cards in list stored by deck object    
    def shuffle_deck(self):
        random.shuffle(self.cards)

