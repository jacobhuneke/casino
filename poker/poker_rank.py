from enum import Enum

class PokerRank(Enum):
    ROYAL_FLUSH = 10, "Royal Flush", 
    STRAIGHT_FLUSH = 9, "Straight Flush",
    FOUR_OF_A_KIND = 8, "Four of a Kind",
    FULL_HOUSE = 7, "Full House",
    FLUSH = 6, "Flush",
    STRAIGHT = 5, "Straight",
    THREE_OF_A_KIND = 4, "Three of a Kind",
    TWO_PAIR = 3, "Two Pair",
    ONE_PAIR = 2, "One Pair",
    HIGH_CARD = 1, "High Card",
