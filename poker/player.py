from poker.deck import *
from poker.poker_rank import *
from itertools import combinations
from collections import Counter

#Player class stores the player's name, the two cards they hold in their hand (hole), and the poker rank of their hand
#Helper methods to compare players, getters for the hole and the rank, add cards to the hole
class Player():
    def __init__(self, name):
        self.name = name
        self._hole = []
        self.hand_rank = PokerRank.HIGH_CARD
        self.flop = []
        self.best_hand = []
        self.is_tie = False
        
    def __repr__(self):
        card_list = "" 
        for card in self._hole:
            card_list += card.__repr__() + ", "
        list = card_list.removesuffix(", ")
        return f"\nName: {self.name}\nCards: {list}\nHand Rank: {self.hand_rank.value[1]}"
    
    def get_hole(self):
        cards = self._hole.copy()
        return cards
    
    def __eq__(self, other):
        if isinstance(other, Player):
            return self.name == other.name and self._hole == other._hole
        return False
    
    def get_best_hand(self):
        return self.best_hand
    
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
        
    def set_flop(self, flop):
        self.flop = flop.copy()
    
    
    def score_hand(self):
        player_cards = self.get_hole()
        player_cards.extend(self.flop)
        flop_combinations = list(combinations(player_cards, 5))
        best_rank = self.hand_rank
        self.best_hand = flop_combinations[0]

        for combo in flop_combinations:
            score = score_combo(combo)
            if score.value[0] < best_rank.value[0]:
                continue
            elif score.value[0] > best_rank.value[0]:
                best_rank = score
                self.best_hand = combo
            else:
                combo2 = compare_tie(self.best_hand, combo, best_rank, self)
                if combo2 != None:
                    self.best_hand = combo
        self.hand_rank = best_rank
        return self.hand_rank
    

#TODO compare straights with aces needs to be fixed
def compare_tie(combo1, combo2, hand_rank, player):
    sum1 = 0
    sum2 = 0
    for card in combo1:
        sum1 += card.rank.value[0]
    for card in combo2:
        sum2 += card.rank.value[0]
    num_count = get_num_counts_for_combo(combo1)
    num_count2 = get_num_counts_for_combo(combo2)
    keys1 = list(num_count.keys())
    keys2 = list(num_count2.keys())

    one_is_low_straight = False
    two_is_low_straight = False
    if sum1 == 28:
        one_is_low_straight = True
    if sum2 == 28:
        two_is_low_straight = True

    match hand_rank:
        case PokerRank.ROYAL_FLUSH:
            player.is_tie = True
        case PokerRank.STRAIGHT_FLUSH:
            if sum1 > sum2 and one_is_low_straight != True:
                return combo1
            elif sum1 > sum2 and one_is_low_straight == True:
                return combo2
            elif sum1 < sum2 and two_is_low_straight != True:
                return combo2
            elif sum1 < sum2 and two_is_low_straight == True:
                return combo1
            else:
                player.is_tie = True
        case PokerRank.FOUR_OF_A_KIND:
            if keys1[0] > keys2[0]:
                return combo1
            elif keys1[0] < keys2[0]:
                return combo2
            else: 
                if keys1[1] > keys2[1]:
                    return combo1
                elif keys1[1] < keys2[1]:
                    return combo2
                else:
                    player.is_tie = True
        case PokerRank.FULL_HOUSE:
            if keys1[0] > keys2[0]:
                return combo1
            elif keys1[0] < keys2[0]:
                return combo2
            else:
                if keys1[1] > keys2[1]:
                    return combo1
                elif keys1[1] < keys2[1]:
                    return combo2
                else:
                    player.is_tie = True
        case PokerRank.FLUSH:
            if sum1 > sum2:
                return combo1
            elif sum1 < sum2:
                return combo2
            else:
                player.is_tie = True
        case PokerRank.STRAIGHT:
            if sum1 > sum2 and one_is_low_straight != True:
                return combo1
            elif sum1 > sum2 and one_is_low_straight == True:
                return combo2
            elif sum1 < sum2 and two_is_low_straight != True:
                return combo2
            elif sum1 < sum2 and two_is_low_straight == True:
                return combo1
            else:
                player.is_tie = True
        case PokerRank.THREE_OF_A_KIND:
            if keys1[0] > keys2[0]:
                return combo1
            elif keys1[0] < keys2[0]:
                return combo2
            else:
                if keys1[1] > keys2[1]:
                    return combo1
                elif keys1[1] < keys2[1]:
                    return combo2
                else:
                    player.is_tie = True
        case PokerRank.TWO_PAIR:
            if keys1[0] > keys2[0]:
                return combo1
            elif keys1[0] < keys2[0]:
                return combo2
            else:
                if keys1[1] > keys2[1]:
                    return combo1
                elif keys1[1] < keys2[1]:
                    return combo2
                else:
                    if keys1[2] > keys2[2]:
                        return combo1
                    elif keys1[2] < keys2[2]:
                        return combo2
                    else:
                        player.is_tie = True
        case PokerRank.ONE_PAIR:
            if keys1[0] > keys2[0]:
                return combo1
            elif keys1[0] < keys2[0]:
                return combo2
            else:
                if keys1[1] > keys2[1]:
                    return combo1
                elif keys1[1] < keys2[1]:
                    return combo2
                else:
                    if keys1[2] > keys2[2]:
                        return combo1
                    elif keys1[2] < keys2[2]:
                        return combo2
                    else:
                        if keys1[3] > keys2[3]:
                            return combo1
                        elif keys1[3] < keys2[3]:
                            return combo2
                        else:
                            player.is_tie = True
        case PokerRank.HIGH_CARD:
            if keys1[0] > keys2[0]:
                return combo1
            elif keys1[0] < keys2[0]:
                return combo2
            else:
                if keys1[1] > keys2[1]:
                    return combo1
                elif keys1[1] < keys2[1]:
                    return combo2
                else:
                    if keys1[2] > keys2[2]:
                        return combo1
                    elif keys1[2] < keys2[2]:
                        return combo2
                    else:
                        if keys1[3] > keys2[3]:
                            return combo1
                        elif keys1[3] < keys2[3]:
                            return combo2
                        else:
                            if keys1[4] > keys2[4]:
                                return combo1
                            elif keys1[4] < keys2[4]:
                                return combo2
                            else:
                                player.is_tie = True
    return None

def get_num_counts_for_combo(combo):
    card1 = combo[0]
    card2 = combo[1]
    card3 = combo[2]
    card4 = combo[3]
    card5 = combo[4]
    nums = [card1.rank.value[0], card2.rank.value[0], card3.rank.value[0], card4.rank.value[0], card5.rank.value[0]]
    nums.sort(reverse=True)
    num_counter = Counter(nums)
    return num_counter



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
    num_counter = Counter(nums)
    sorted_freq = sorted(num_counter.values(), reverse=True)  #cleanup w/ helper

    is_low_straight = False
    is_top_straight = False   
    is_straight = True
    #check high straight(A2345)
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
    #top straight is AKQJT
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
    elif sorted_freq[0] == 4:
        return PokerRank.FOUR_OF_A_KIND
    elif sorted_freq[0] == 3 and sorted_freq[1] == 2:
        return PokerRank.FULL_HOUSE
    elif is_flush:
        return PokerRank.FLUSH
    elif is_straight:
        return PokerRank.STRAIGHT
    elif sorted_freq[0] == 3:
        return PokerRank.THREE_OF_A_KIND
    elif sorted_freq[0] == 2 and sorted_freq[1] == 2:
        return PokerRank.TWO_PAIR
    elif sorted_freq[0] == 2:
        return PokerRank.ONE_PAIR
    else:
        return PokerRank.HIGH_CARD
    
def get_tie_winner_players(p1, p2):
    p1_hand = p1.get_best_hand()
    p2_hand = p2.get_best_hand()
    hand_rank = p1.get_hand_rank()
    best_hand = compare_tie(p1_hand, p2_hand, hand_rank, p1)
    print("Best Hand", best_hand)
    if best_hand == None:
        p1.is_tie = True
        p2.is_tie = True
        return p1
    else:
        if p1_hand == best_hand:
            return p1
        else:
            return p2

def get_winner(p1, p2):
    p3 = Player("Tie")
    if p1.hand_rank.value[0] > p2.hand_rank.value[0]:
        return p1
    elif p1.hand_rank.value[0] < p2.hand_rank.value[0]:
        return p2
    else:
        winner = get_tie_winner_players(p1, p2)
        return winner if winner != None else p3