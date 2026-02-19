import pygame
from poker.UIElement import *
from poker.constants import *
from poker.card_sheet import *
from poker.poker_game import *
from poker.log_event import *
from poker.player_init_screen import names

def play_game(screen):
    return_btn = UIElement(
        center_position=(1150, 650),
        font_size=20,
        bg_rgb=SCREEN_COLOR,
        text_rgb=TEXT_COLOR,
        text="Return to main menu",
        action=GameState.TITLE,
    )
    CARD_SHEET = pygame.image.load("poker/images/cards-sheet.png").convert_alpha()
    CARD_SHEET = pygame.transform.scale(CARD_SHEET, (CARD_SHEET_WIDTH, CARD_SHEET_HEIGHT))
    title_box = pygame.Rect(DECK_INIT_WIDTH, CARD_BUFFER, 180, 40)
    winner_box = pygame.Rect(SCREEN_WIDTH - DECK_INIT_WIDTH - 360, CARD_BUFFER, 180, 40)
    p1_box = pygame.Rect(DECK_INIT_WIDTH, PLAYER_NAME_HEIGHT, 180, 40)
    p2_box = pygame.Rect(SCREEN_WIDTH - DECK_INIT_WIDTH - (180 * 2), PLAYER_NAME_HEIGHT, 180, 40)
    call_button1 = UIElement(
        center_position=(DECK_INIT_WIDTH + 36, BUTTON_HEIGHT + 30),
        font_size=36,
        bg_rgb=SCREEN_COLOR,
        text_rgb=TEXT_COLOR,
        text="CALL",
        action=GameState.CALL,
    )
    bet_button1 = UIElement(
        center_position=(DECK_INIT_WIDTH + 156, BUTTON_HEIGHT + 30),
        font_size=36,
        bg_rgb=SCREEN_COLOR,
        text_rgb=TEXT_COLOR,
        text="BET",
        action=GameState.BET,
    )
    fold_button1 = UIElement(
        center_position=(DECK_INIT_WIDTH + 276, BUTTON_HEIGHT + 30),
        font_size=36,
        bg_rgb=SCREEN_COLOR,
        text_rgb=TEXT_COLOR,
        text="FOLD",
        action=GameState.FOLD,
    )
    call_button2 = UIElement(
        center_position=(P2_CARD1_WIDTH + 36, BUTTON_HEIGHT + 30),
        font_size=36,
        bg_rgb=SCREEN_COLOR,
        text_rgb=TEXT_COLOR,
        text="CALL",
        action=GameState.CALL,
    )
    bet_button2 = UIElement(
        center_position=(P2_CARD1_WIDTH + 156, BUTTON_HEIGHT + 30),
        font_size=36,
        bg_rgb=SCREEN_COLOR,
        text_rgb=TEXT_COLOR,
        text="BET",
        action=GameState.BET,
    )
    fold_button2 = UIElement(
        center_position=(P2_CARD1_WIDTH+ 276, BUTTON_HEIGHT + 30),
        font_size=36,
        bg_rgb=SCREEN_COLOR,
        text_rgb=TEXT_COLOR,
        text="FOLD",
        action=GameState.FOLD,
    )

    title_font = pygame.font.SysFont("Comic Sans MS", 64)
    title_font.set_underline(True)
    player_font = pygame.font.SysFont("Comic Sans MS", 48)
    p1 = Player(names["p1"])
    p2 = Player(names["p2"])
    game = PokerGame(p1, p2)
    game.deal_player_cards()
    p1_cards = p1.get_hole()
    p2_cards = p2.get_hole()
    print(p1_cards, p2_cards)
    game.deal_flop()
    game.deal_turn()
    game.deal_turn()
    p1.score_hand()
    p2.score_hand()
    print(p1)
    print(p2)
    winner = get_winner(p1, p2)

    buttons = [return_btn, call_button1, bet_button1, fold_button1, call_button2, bet_button2, fold_button2]

    while True:
        mouse_up = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                log_event("quit_game")
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True

        screen.fill(SCREEN_COLOR)

        #init deck image
        deck_rect = get_deck_img()
        deck_pic = CARD_SHEET.subsurface(deck_rect)
        screen.blit(deck_pic, (DECK_INIT_WIDTH, DECK_INIT_HEIGHT))

        #init title message
        pygame.draw.rect(screen, SCREEN_COLOR, title_box, 2)
        title_surface = title_font.render(f"POKER GAME", True, TEXT_COLOR)
        screen.blit(title_surface, (title_box.x + 5, title_box.y + 5))

        #init p1 message, cards
        pygame.draw.rect(screen, SCREEN_COLOR, p1_box, 2)
        p1_surface = player_font.render(f"{p1.name}: {p1.score_hand().value[1]}", True, TEXT_COLOR)
        screen.blit(p1_surface, (p1_box.x + 5, p1_box.y + 5))
        p1_card1_rect = get_card_rect(p1_cards[0].__repr__())
        p1_card1_pic = CARD_SHEET.subsurface(p1_card1_rect)
        screen.blit(p1_card1_pic, (P1_CARD1_WIDTH, PLAYER_CARD_HEIGHT))
        p1_card2_rect = get_card_rect(p1_cards[1].__repr__())
        p1_card2_pic = CARD_SHEET.subsurface(p1_card2_rect)
        screen.blit(p1_card2_pic, (P1_CARD2_WIDTH, PLAYER_CARD_HEIGHT))

        #init p2 name, cards
        pygame.draw.rect(screen, SCREEN_COLOR, p2_box, 2)
        p2_surface = player_font.render(f"{p2.name}: {p2.score_hand().value[1]}", True, TEXT_COLOR)
        screen.blit(p2_surface, (p2_box.x + 5, p2_box.y + 5))
        p2_card1_rect = get_card_rect(p2_cards[0].__repr__())
        p2_card1_pic = CARD_SHEET.subsurface(p2_card1_rect)
        screen.blit(p2_card1_pic, (P2_CARD1_WIDTH, PLAYER_CARD_HEIGHT))
        p2_card2_rect = get_card_rect(p2_cards[1].__repr__())
        p2_card2_pic = CARD_SHEET.subsurface(p2_card2_rect)
        screen.blit(p2_card2_pic, (P2_CARD2_WIDTH, PLAYER_CARD_HEIGHT))

        #draw flop cards to screen
        flop1_rect = get_card_rect(game.flop[0].__repr__())
        flop1_pic = CARD_SHEET.subsurface(flop1_rect)
        screen.blit(flop1_pic, (FLOP1_WIDTH, DECK_INIT_HEIGHT))
        flop2_rect = get_card_rect(game.flop[1].__repr__())
        flop2_pic = CARD_SHEET.subsurface(flop2_rect)
        screen.blit(flop2_pic, (FLOP2_WIDTH, DECK_INIT_HEIGHT))
        flop3_rect = get_card_rect(game.flop[2].__repr__())
        flop3_pic = CARD_SHEET.subsurface(flop3_rect)
        screen.blit(flop3_pic, (FLOP3_WIDTH, DECK_INIT_HEIGHT))
        
        #draw turn to screen
        turn_rect = get_card_rect(game.flop[3].__repr__())
        turn_pic = CARD_SHEET.subsurface(turn_rect)
        screen.blit(turn_pic, (TURN_WIDTH, DECK_INIT_HEIGHT))

        #draw river to screen
        river_rect = get_card_rect(game.flop[4].__repr__())
        river_pic = CARD_SHEET.subsurface(river_rect)
        screen.blit(river_pic, (RIVER_WIDTH, DECK_INIT_HEIGHT))

        #draw winner message to screen
        pygame.draw.rect(screen, SCREEN_COLOR, winner_box, 2)
        winner_surface = title_font.render(f"{winner.name} wins!", True, TEXT_COLOR)
        screen.blit(winner_surface, (winner_box.x + 5, winner_box.y + 5))
        
        for button in buttons:
            ui_action = button.update(pygame.mouse.get_pos(), mouse_up)
            if ui_action is not None:
                return ui_action
            button.draw(screen)

        pygame.display.flip()

