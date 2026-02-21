from poker.card_sheet import *
from poker.poker_game import *
from poker.log_event import *
from poker.UIElement import *
from poker.play_game_screen import *
from poker.title_screen import *
from poker.player_init_screen import *
from poker.win_screen import *
import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_state = GameState.TITLE
    clock = pygame.time.Clock()

    CARD_SHEET = pygame.image.load("poker/images/cards-sheet.png").convert_alpha()
    CARD_SHEET = pygame.transform.scale(CARD_SHEET, (CARD_SHEET_WIDTH, CARD_SHEET_HEIGHT))

    while True:
        # poll for events
        if game_state == GameState.TITLE:
            log_event("title_screen")
            game_state = title_screen(screen)
        if game_state == GameState.PLAYER_INIT:
            log_event("player_init_screen")
            game_state = player_init_screen(screen)
        if game_state == GameState.POKER_GAME:
            log_event("play_game_screen")
            game_state = play_game(screen)
        if game_state == GameState.WIN:
            log_event("win_screen")
            game_state = win_screen(screen)
        if game_state == GameState.QUIT:
            pygame.quit()
            log_event("quit_game")
            return

        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                log_event("quit_game")
                pygame.quit()         
            
        screen.fill(SCREEN_COLOR)
        # flip() the display to put your work on screen
        pygame.display.flip()
        clock.tick(60)

pygame.quit()
main()
