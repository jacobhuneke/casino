from poker.deck import *
from poker.poker_rank import *
from itertools import combinations
from collections import Counter

#Player class stores the player's name, the two cards they hold in their hand (hole), and the poker rank of their hand
#Helper methods to compare players, getters for the hole aand the rank, add cards to the hole
class Player():
    def __init__(self, name):
        self.name = name
        self._hole = []
        self.hand_rank = PokerRank.HIGH_CARD
        self.flop = []
        
    def __repr__(self):
        card_list = "" 
        for card in self._hole:
            card_list += card.__repr__() + ", "
        list = card_list.removesuffix(", ")
        return f"\nName: {self.name}\nCards: {list}\nHand Rank: {self.hand_rank.value[1]}"
    
    def get_hole(self):
        return self._hole
    
    def __eq__(self, other):
        if isinstance(other, Player):
            return self.name == other.name and self._hole == other._hole
        return False
    
    def get_hand_rank(self):
        return self.hand_rank

    def add_card(self, card):               #Max cards a player is dealt is two
        if len(self._hole) < 2:
            if isinstance(card, Card):
                self._hole.append(card)
            else:
                raise Exception("card is not a card")
        else:
            raise Exception("has max cards in hole")
    
    def score_hand(self):
        player_cards = self.get_hole()
        flop_combinations = list(combinations(self.flop, 3))
        card_combinations = list(map(lambda x: x + tuple(player_cards), flop_combinations))
        best_rank = self.hand_rank.value

        for combo in card_combinations:
            score = score_combo(combo)
            print(score)
            if score < best_rank:
                continue
            elif score > best_rank:
                best_rank = score
            else:
                pass
                #compare rank
        self.hand_rank = best_rank
        return self.hand_rank.value
    
    def compare_rank(self, combo):
        pass


#combo is five cards. The prior function will go through every combination of five cards, score them, and save the highest ranking hand
#when score_combo is called, the cards are checked to meet the reqs for each of the PokerRank enum values, high to low. 
#When one is met, it is returned
def score_combo(combo):
    card1 = combo[0]
    card2 = combo[1]
    card3 = combo[2]
    card4 = combo[3]
    card5 = combo[4]
    #determine flushes
    suits = [card1.suit.value[0], card2.suit.value[0], card3.suit.value[0], card4.suit.value[0], card5.suit.value[0]]
    suit = suits[0]
    i = 0    
    is_flush = True
    while is_flush and i <= 4:
        if suits[i] != suit:
            is_flush = False
        i += 1
    
    #determine straight, and duplicate nums (pair-3-4 of a kind)
    nums = [card1.rank.value[0], card2.rank.value[0], card3.rank.value[0], card4.rank.value[0], card5.rank.value[0]]
    nums.sort(reverse=True)
    num_counter = Counter()
    for num in nums:
        num_counter[num] += 1

    is_low_straight = False
    is_top_straight = False    
    is_straight = True
    #check low straight(A2345)
    if nums[0] == 14 and nums[1] == 5  and nums[2] == 4 and nums[3] == 3 and nums[4] == 2:
        is_low_straight = True
    #check other straights
    j = 1
    curr = nums[0]
    #is straight if each number is one less than the previous one, breaks if one is more than one less
    while is_straight and j <= 4:
        if nums[j] != curr - 1:
            is_straight = False
        j += 1
        curr = nums[j - 1]
    
    #if straight and the top num is an ace, then it is AKQJ10, and the top straight (need for royal flush)
    if is_straight and nums[0] == 14:
        is_top_straight = True

    #is a straight if its a low straight or normal
    if is_low_straight or is_straight:
        is_straight = True
    else:
        is_straight = False
    #poker rank conditions
    #checks for the highest first then the rest, returns based on highest
    if is_flush and is_top_straight:
        return PokerRank.ROYAL_FLUSH
    elif is_flush and is_straight:
        return PokerRank.STRAIGHT_FLUSH
    elif is_flush:
        return PokerRank.FLUSH
    elif is_straight:
        return PokerRank.STRAIGHT
    else:
        return PokerRank.HIGH_CARD
