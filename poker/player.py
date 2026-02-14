from poker.deck import *

class Player():
    def __init__(self, name):
        self.name = name
        self._hand = []
        
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