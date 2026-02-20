import pygame
from poker.UIElement import *
from poker.constants import *
from poker.card_sheet import *
from poker.poker_game import *
from poker.log_event import *
from poker.player_init_screen import names
from poker.player import *

def play_game(screen):
    
    return_btn = UIElement(
        center_position=(1150, 650),
        font_size=20,
        bg_rgb=SCREEN_COLOR,
        text_rgb=TEXT_COLOR,
        text="Return to main menu",
        screen_action=GameState.TITLE,
    )

    CARD_SHEET = pygame.image.load("poker/images/cards-sheet.png").convert_alpha()
    CARD_SHEET = pygame.transform.scale(CARD_SHEET, (CARD_SHEET_WIDTH, CARD_SHEET_HEIGHT))
    clock = pygame.time.Clock()
    title_box = pygame.Rect(DECK_INIT_WIDTH, CARD_BUFFER, 180, 40)
    winner_box = pygame.Rect(SCREEN_WIDTH - DECK_INIT_WIDTH - 360, CARD_BUFFER, 180, 40)
    p1_name_box = pygame.Rect(DECK_INIT_WIDTH, PLAYER_NAME_HEIGHT, 180, 40)
    p2_name_box = pygame.Rect(SCREEN_WIDTH - DECK_INIT_WIDTH - (180 * 2), PLAYER_NAME_HEIGHT, 180, 40)
    p1_cash_box = pygame.Rect(DECK_INIT_WIDTH, PLAYER_CASH_HEIGHT, 180, 40)
    p2_cash_box = pygame.Rect(SCREEN_WIDTH - DECK_INIT_WIDTH - (180 * 2), PLAYER_CASH_HEIGHT, 180, 40)
    play_again_box = pygame.Rect(PLAY_AGAIN_WIDTH, PLAYER_NAME_HEIGHT, 180, 40)

    call_button1 = UIElement(
        center_position=(DECK_INIT_WIDTH + 36, BUTTON_HEIGHT + 30),
        font_size=36,
        bg_rgb=SCREEN_COLOR,
        text_rgb=TEXT_COLOR,
        text="CALL",
        poker_func=PokerFuncs.CALL,
    )
    bet_button1 = UIElement(
        center_position=(DECK_INIT_WIDTH + 156, BUTTON_HEIGHT + 30),
        font_size=36,
        bg_rgb=SCREEN_COLOR,
        text_rgb=TEXT_COLOR,
        text="BET",
        poker_func=PokerFuncs.BET,
    )
    fold_button1 = UIElement(
        center_position=(DECK_INIT_WIDTH + 276, BUTTON_HEIGHT + 30),
        font_size=36,
        bg_rgb=SCREEN_COLOR,
        text_rgb=TEXT_COLOR,
        text="FOLD",
        poker_func=PokerFuncs.FOLD,
    )
    call_button2 = UIElement(
        center_position=(P2_CARD1_WIDTH + 36, BUTTON_HEIGHT + 30),
        font_size=36,
        bg_rgb=SCREEN_COLOR,
        text_rgb=TEXT_COLOR,
        text="CALL",
        poker_func=PokerFuncs.CALL,
    )
    bet_button2 = UIElement(
        center_position=(P2_CARD1_WIDTH + 156, BUTTON_HEIGHT + 30),
        font_size=36,
        bg_rgb=SCREEN_COLOR,
        text_rgb=TEXT_COLOR,
        text="BET",
        poker_func=PokerFuncs.BET,
    )
    fold_button2 = UIElement(
        center_position=(P2_CARD1_WIDTH+ 276, BUTTON_HEIGHT + 30),
        font_size=36,
        bg_rgb=SCREEN_COLOR,
        text_rgb=TEXT_COLOR,
        text="FOLD",
        poker_func=PokerFuncs.FOLD,
    )
    yes_button = UIElement(
        center_position=(PLAY_AGAIN_WIDTH + 200, PLAYER_CASH_HEIGHT + CARD_BUFFER),
        font_size=36,
        bg_rgb=SCREEN_COLOR,
        text_rgb=TEXT_COLOR,
        text="YES",
        poker_func=PokerFuncs.NEW_GAME,
    )
    no_button = UIElement(
        center_position=(PLAY_AGAIN_WIDTH + 300, PLAYER_CASH_HEIGHT + CARD_BUFFER),
        font_size=36,
        bg_rgb=SCREEN_COLOR,
        text_rgb=TEXT_COLOR,
        text="NO",
        screen_action=GameState.QUIT,
    )
    title_font = pygame.font.SysFont("Comic Sans MS", 64)
    player_font = pygame.font.SysFont("Comic Sans MS", 48)
    
    #init poker game with ui names, sets state to deal
    p1 = Player(names["p1"])
    p2 = Player(names["p2"])
    game = PokerGame(p1, p2)
    func_state = PokerFuncs.DEAL
    turn = p1
    flopped = False
    turned = False
    rivered = False
    is_winner = False
    screen_buttons1 = [return_btn, no_button]
    poker_buttons1 = [call_button1, bet_button1, fold_button1, call_button2, bet_button2, fold_button2, yes_button]
    screen_buttons2 = [return_btn]
    poker_buttons2 = [call_button1, bet_button1, fold_button1, call_button2, bet_button2, fold_button2]

    while True:
        mouse_up = False
        match func_state:
            case PokerFuncs.DEAL:
                game.deal_player_cards()
                p1_cards = p1.get_hole()
                p2_cards = p2.get_hole()
                func_state = PokerFuncs.TURN
                log_event("dealt_cards")
            case PokerFuncs.CALL:
                if turn == p1:
                    turn = p2
                    func_state = PokerFuncs.TURN
                elif game.flop == [] and turn == p2:
                    game.deal_flop()
                    p1.score_hand()
                    p2.score_hand()
                    winner = get_winner(p1, p2)
                    turn = p1
                    flopped = True
                    func_state = PokerFuncs.TURN
                    log_event("flopped_cards")
                elif flopped and turned != True and turn == p2:
                    game.deal_turn()
                    p1.score_hand()
                    p2.score_hand()
                    winner = get_winner(p1, p2)
                    turn = p1
                    turned = True
                    func_state = PokerFuncs.TURN
                    log_event("turned_card")
                elif turned and turn == p2 and rivered != True:
                    game.deal_turn()
                    p1.score_hand()
                    p2.score_hand()
                    winner = get_winner(p1, p2)
                    turn = p1
                    rivered = True
                    func_state = PokerFuncs.TURN
                    is_winner = True
                    winner.win_count += 1
                    log_event("rivered_card")
                    log_event(f"{winner.name}_won_with_{winner.hand_rank.value[1]}")
            case PokerFuncs.FOLD:
                if turn == p1:
                    winner = p2
                    log_event("p1_folded")
                elif turn == p2:
                    winner = p1
                    log_event("p2_folded")
                is_winner = True
                winner.win_count += 1
                log_event(f"{winner.name}_won_with_{winner.hand_rank.value[1]}")
                func_state = PokerFuncs.END_GAME
            case PokerFuncs.BET:
                pass
            case PokerFuncs.END_GAME:
                pass
            case PokerFuncs.NEW_GAME:
                p1.reset_player()
                log_event("p1_reset")
                p2.reset_player()
                log_event("p2_reset")
                game.reset_game()
                log_event("game_reset")
                flopped = False
                turned = False
                rivered = False
                is_winner = False
                turn = p1
                func_state = PokerFuncs.DEAL
            case PokerFuncs.TURN:
                pass
        
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
        pygame.draw.rect(screen, SCREEN_COLOR, p1_name_box, 2)
        p1_name_surface = player_font.render(f"{p1.name}: {p1.score_hand().value[1]}", True, TEXT_COLOR)
        screen.blit(p1_name_surface, (p1_name_box.x + 5, p1_name_box.y + 5))
        pygame.draw.rect(screen, SCREEN_COLOR, p1_cash_box, 2)
        p1_cash_surface = player_font.render(f"Cash: ${p1.cash:.2f}", True, TEXT_COLOR)
        screen.blit(p1_cash_surface, (p1_cash_box.x + 5, p1_cash_box.y + 5))
        if turn == p1 or is_winner:
            p1_card1_rect = get_card_rect(p1_cards[0].__repr__())
            p1_card1_pic = CARD_SHEET.subsurface(p1_card1_rect)
            screen.blit(p1_card1_pic, (P1_CARD1_WIDTH, PLAYER_CARD_HEIGHT))
            p1_card2_rect = get_card_rect(p1_cards[1].__repr__())
            p1_card2_pic = CARD_SHEET.subsurface(p1_card2_rect)
            screen.blit(p1_card2_pic, (P1_CARD2_WIDTH, PLAYER_CARD_HEIGHT))
        else:
            screen.blit(deck_pic, (P1_CARD1_WIDTH, PLAYER_CARD_HEIGHT))
            screen.blit(deck_pic, (P1_CARD2_WIDTH, PLAYER_CARD_HEIGHT))

        #init p2 name, cash, cards
        pygame.draw.rect(screen, SCREEN_COLOR, p2_name_box, 2)
        p2_name_surface = player_font.render(f"{p2.name}: {p2.score_hand().value[1]}", True, TEXT_COLOR)
        screen.blit(p2_name_surface, (p2_name_box.x + 5, p2_name_box.y + 5))
        pygame.draw.rect(screen, SCREEN_COLOR, p2_cash_box, 2)
        p2_cash_surface = player_font.render(f"Cash: ${p2.cash:.2f}", True, TEXT_COLOR)
        screen.blit(p2_cash_surface, (p2_cash_box.x + 5, p2_cash_box.y + 5))
        if turn == p2 or is_winner:
            p2_card1_rect = get_card_rect(p2_cards[0].__repr__())
            p2_card1_pic = CARD_SHEET.subsurface(p2_card1_rect)
            screen.blit(p2_card1_pic, (P2_CARD1_WIDTH, PLAYER_CARD_HEIGHT))
            p2_card2_rect = get_card_rect(p2_cards[1].__repr__())
            p2_card2_pic = CARD_SHEET.subsurface(p2_card2_rect)
            screen.blit(p2_card2_pic, (P2_CARD2_WIDTH, PLAYER_CARD_HEIGHT))
        else:
            screen.blit(deck_pic, (P2_CARD1_WIDTH, PLAYER_CARD_HEIGHT))
            screen.blit(deck_pic, (P2_CARD2_WIDTH, PLAYER_CARD_HEIGHT))

        #draw flop cards to screen
        if flopped == True:
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
        if turned == True:
            turn_rect = get_card_rect(game.flop[3].__repr__())
            turn_pic = CARD_SHEET.subsurface(turn_rect)
            screen.blit(turn_pic, (TURN_WIDTH, DECK_INIT_HEIGHT))

        #draw river to screen
        if rivered == True:
            river_rect = get_card_rect(game.flop[4].__repr__())
            river_pic = CARD_SHEET.subsurface(river_rect)
            screen.blit(river_pic, (RIVER_WIDTH, DECK_INIT_HEIGHT))

        #draw winner message to screen, play again button
        if is_winner == True:
            pygame.draw.rect(screen, SCREEN_COLOR, winner_box, 2)
            winner_surface = title_font.render(f"{winner.name} wins!", True, TEXT_COLOR)
            screen.blit(winner_surface, (winner_box.x + 5, winner_box.y + 5))
            pygame.draw.rect(screen, SCREEN_COLOR, play_again_box, 2)
            play_again_surface = player_font.render("Would you like to play again?", True, TEXT_COLOR)
            screen.blit(play_again_surface, (play_again_box.x + 5, play_again_box.y + 5))
        else:
            pygame.draw.rect(screen, SCREEN_COLOR, winner_box, 2)
            winner_surface = title_font.render(f"{turn.name}'s turn", True, TEXT_COLOR)
            screen.blit(winner_surface, (winner_box.x + 5, winner_box.y + 5))

        if is_winner:
            for button in poker_buttons1:
                ui_action = button.poker_func_update(pygame.mouse.get_pos(), mouse_up)
                if ui_action is not None:
                    func_state = ui_action
                button.draw(screen)

            for button in screen_buttons1:
                ui_action = button.screen_update(pygame.mouse.get_pos(), mouse_up)
                if ui_action is not None:
                    return ui_action
                button.draw(screen)
        else:
            for button in poker_buttons2:
                ui_action = button.poker_func_update(pygame.mouse.get_pos(), mouse_up)
                if ui_action is not None:
                    func_state = ui_action
                button.draw(screen)

            for button in screen_buttons2:
                ui_action = button.screen_update(pygame.mouse.get_pos(), mouse_up)
                if ui_action is not None:
                    return ui_action
                button.draw(screen)
        pygame.display.flip()
        clock.tick(60)
