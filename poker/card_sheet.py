import pygame
from poker.deck import *
from poker.constants import *

def build_card_map():
    card_map = {}
    col = 0
    row = 1
    for card in ORDERED_DECK:
        if card.get_rank() == 14:
            continue
        else: 
            card_name = card.__repr__()
            card_map[card_name] = (col, row)
            col += 1
        if card.get_rank() == 13:
            col = 0
            row += 1
    return card_map

CARD_MAP = build_card_map()


def get_card_rect(card_name):
    col, row = CARD_MAP[card_name]
    rect = pygame.Rect(col * CARD_WIDTH, row * CARD_HEIGHT, CARD_WIDTH, CARD_HEIGHT)
    return rect

def get_deck_img():
    rect = pygame.Rect(2 * CARD_WIDTH, 0, CARD_WIDTH, CARD_HEIGHT)
    return rect

