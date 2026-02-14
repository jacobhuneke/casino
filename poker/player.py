from poker.deck import *
from poker.rank_hand import PokerRank

class Player():
    def __init__(self, name):
        self.name = name
        self._hand = []
        self.hand_rank = PokerRank.HIGH_CARD
        
    def __repr__(self):
        card_list = " ".join(self._hand)
        return f"Name: {self.name}\nCards: {card_list}"
    
    def get_hand(self):
        card_list = " ".join(self._hand)
        return card_list
    
    def __eq__(self, other):
        if isinstance(other, Player):
            return self.name == other.name and self._hand == other._hand
        return False
    
    def rank_hand(self):
        return self.hand_rank