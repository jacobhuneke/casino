from poker.player import *
from poker.deck import *
from poker.poker_rank import PokerRank

#Poker Game class, gets a game going essentially.
#Stores a deck, a list of players, and the flop (the cards dealt for all to see in this texas hold em style game)
class PokerGame():
    def __init__(self, p1, p2):
        self.deck = Deck()
        self.deck.shuffle_deck()
        self.deck.shuffle_deck()
        self.players = [p1, p2]
        self.flop = []
        
#deals all players in order two cards from the deck. This is their hole
    def deal_player_cards(self):
        try:    
            for player in self.players:
                card = self.deck.deal_card()
                player.add_card(card)

            for player in self.players:
                card = self.deck.deal_card()
                player.add_card(card)
        except Exception as e:
            print(e)

#deals the flop (three cards) and stores it in the flop variable
#by poker rules, burns one card first
    def deal_flop(self):
        flop = []
        self.deck.deal_card()#burn one
        flop.append(self.deck.deal_card())#turn three
        flop.append(self.deck.deal_card())
        flop.append(self.deck.deal_card())
        self.flop = flop
        self.set_flop()

#deals one card for the turn, and the river. Burns a card before dealing one as with the flop
    def deal_turn(self):
        self.deck.deal_card()#burn one turn one
        self.flop.append(self.deck.deal_card())
        self.set_flop()
    
#want the player objects to be able to see the game's flop
    def set_flop(self):
        for player in self.players:
            player.flop = self.flop.copy()

    
    def get_flop(self):
        return self.flop
    
    def __repr__(self):
        string = "Welcome to the Poker Game!\n"
        string += "Players are: "
        for player in self.players:
            string += player.name + " and "
        string = string.removesuffix(" and ")
        string += "\nFlop is: "
        for f in self.flop:
            string += f.__repr__() + ", "
        string = string.removesuffix(", ")
        return string


