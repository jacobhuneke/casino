import pygame
from poker.UIElement import *
from poker.constants import *
from poker.card_sheet import *
from poker.poker_game import *
from poker.log_event import *
from poker.player_init_screen import names
from poker.player import *

winners = {"winner" : "", "debt": ""}
def play_game(screen):
    #button to take you back to the home screen
    return_btn = UIElement(
        center_position=(1150, 650),
        font_size=20,
        bg_rgb=SCREEN_COLOR,
        text_rgb=TEXT_COLOR,
        text="Return to main menu",
        screen_action=GameState.TITLE,
    )

    #imports card sheet, initialize local variables and text boxes
    CARD_SHEET = pygame.image.load("poker/images/cards-sheet.png").convert_alpha()
    CARD_SHEET = pygame.transform.scale(CARD_SHEET, (CARD_SHEET_WIDTH, CARD_SHEET_HEIGHT))
    clock = pygame.time.Clock()
    title_box = pygame.Rect(DECK_INIT_WIDTH, CARD_BUFFER, 180, 40)
    winner_box = pygame.Rect(SCREEN_WIDTH - DECK_INIT_WIDTH - 360, CARD_BUFFER, 180, 40)
    p1_name_box = pygame.Rect(DECK_INIT_WIDTH, PLAYER_NAME_HEIGHT, 180, 40)
    p2_name_box = pygame.Rect(SCREEN_WIDTH - DECK_INIT_WIDTH - (180 * 2), PLAYER_NAME_HEIGHT, 180, 40)
    p1_cash_box = pygame.Rect(DECK_INIT_WIDTH, PLAYER_CASH_HEIGHT, 180, 40)
    p2_cash_box = pygame.Rect(SCREEN_WIDTH - DECK_INIT_WIDTH - (180 * 2), PLAYER_CASH_HEIGHT, 180, 40)
    play_again_box = pygame.Rect(PLAY_AGAIN_WIDTH, PLAYER_CASH_HEIGHT, 180, 40)
    pot_box = pygame.Rect(PLAY_AGAIN_WIDTH + 150, PLAYER_CASH_HEIGHT, 180, 40)

    #initializes buttons for player functions, and buttons to alter the screen if quit or back to home page
    call_button1 = UIElement(
        center_position=(P1_BTN1_WIDTH, BUTTON_HEIGHT),
        font_size=36,
        bg_rgb=SCREEN_COLOR,
        text_rgb=TEXT_COLOR,
        text="CALL",
        poker_func=PokerFuncs.CALL,
    )
    bet_button1 = UIElement(
        center_position=(P1_BTN2_WIDTH, BUTTON_HEIGHT),
        font_size=36,
        bg_rgb=SCREEN_COLOR,
        text_rgb=TEXT_COLOR,
        text="BET",
        poker_func=PokerFuncs.BET,
    )
    fold_button1 = UIElement(
        center_position=(P1_BTN3_WIDTH, BUTTON_HEIGHT),
        font_size=36,
        bg_rgb=SCREEN_COLOR,
        text_rgb=TEXT_COLOR,
        text="FOLD",
        poker_func=PokerFuncs.FOLD,
    )
    call_button2 = UIElement(
        center_position=(P2_BTN1_WIDTH, BUTTON_HEIGHT),
        font_size=36,
        bg_rgb=SCREEN_COLOR,
        text_rgb=TEXT_COLOR,
        text="CALL",
        poker_func=PokerFuncs.CALL,
    )
    bet_button2 = UIElement(
        center_position=(P2_BTN2_WIDTH, BUTTON_HEIGHT),
        font_size=36,
        bg_rgb=SCREEN_COLOR,
        text_rgb=TEXT_COLOR,
        text="BET",
        poker_func=PokerFuncs.BET,
    )
    fold_button2 = UIElement(
        center_position=(P2_BTN3_WIDTH, BUTTON_HEIGHT),
        font_size=36,
        bg_rgb=SCREEN_COLOR,
        text_rgb=TEXT_COLOR,
        text="FOLD",
        poker_func=PokerFuncs.FOLD,
    )
    half_pot_btn1 = UIElement(
        center_position=(P1_BTN1_WIDTH, BUTTON_HEIGHT),
        font_size=36,
        bg_rgb=SCREEN_COLOR,
        text_rgb=TEXT_COLOR,
        text="Half Pot",
        poker_func=PokerFuncs.HALF_POT,
    )
    pot_btn1 = UIElement(
        center_position=(P1_BTN2_WIDTH, BUTTON_HEIGHT),
        font_size=36,
        bg_rgb=SCREEN_COLOR,
        text_rgb=TEXT_COLOR,
        text="Pot",
        poker_func=PokerFuncs.POT,
    )
    two_pot_btn1 = UIElement(
        center_position=(P1_BTN3_WIDTH, BUTTON_HEIGHT),
        font_size=36,
        bg_rgb=SCREEN_COLOR,
        text_rgb=TEXT_COLOR,
        text="Two Pot",
        poker_func=PokerFuncs.TWO_POT,
    )
    half_pot_btn2 = UIElement(
        center_position=(P2_BTN1_WIDTH, BUTTON_HEIGHT),
        font_size=36,
        bg_rgb=SCREEN_COLOR,
        text_rgb=TEXT_COLOR,
        text="Half Pot",
        poker_func=PokerFuncs.HALF_POT,
    )
    pot_btn2 = UIElement(
        center_position=(P2_BTN2_WIDTH, BUTTON_HEIGHT),
        font_size=36,
        bg_rgb=SCREEN_COLOR,
        text_rgb=TEXT_COLOR,
        text="Pot",
        poker_func=PokerFuncs.POT,
    )
    two_pot_btn2 = UIElement(
        center_position=(P2_BTN3_WIDTH, BUTTON_HEIGHT),
        font_size=36,
        bg_rgb=SCREEN_COLOR,
        text_rgb=TEXT_COLOR,
        text="Two Pot",
        poker_func=PokerFuncs.TWO_POT,
    )
    yes_button = UIElement(
        center_position=(PLAY_AGAIN_WIDTH + 200, PLAYER_CASH_HEIGHT + CARD_BUFFER + 75),
        font_size=36,
        bg_rgb=SCREEN_COLOR,
        text_rgb=TEXT_COLOR,
        text="YES",
        poker_func=PokerFuncs.NEW_GAME,
    )
    no_button = UIElement(
        center_position=(PLAY_AGAIN_WIDTH + 300, PLAYER_CASH_HEIGHT + CARD_BUFFER + 75),
        font_size=36,
        bg_rgb=SCREEN_COLOR,
        text_rgb=TEXT_COLOR,
        text="NO",
        screen_action=GameState.QUIT,
    )

    #defines title and player font
    title_font = pygame.font.SysFont("Comic Sans MS", 64)
    player_font = pygame.font.SysFont("Comic Sans MS", 48)
    
    #init poker game with ui names, sets state to deal
    p1 = Player(names["p1"])
    p2 = Player(names["p2"])
    game = PokerGame(p1, p2)
    #subtract ante value from each player at beginning of the game
    p1.cash -= ANTE
    p2.cash -= ANTE 
    pot_amount = ANTE * 2
    #sets state to deal so when loop begins cards are dealt, and on p1's turn
    func_state = PokerFuncs.DEAL
    turn = p1
    #sets boolean values to false
    flopped = False
    turned = False
    rivered = False
    is_winner = False
    is_bet = False
    matched_bet = True
    current_bet = 0.0
    end_game = False
    #creates different lists with all the UI buttons. Win screen buttons come up when a player wins
    #the func buttons come up on each player's turn
    win_screen_buttons = [return_btn, no_button]
    p1_func_buttons = [call_button1, bet_button1, fold_button1]
    p2_func_buttons = [call_button2, bet_button2, fold_button2]
    p1_bet_buttons = [half_pot_btn1, pot_btn1, two_pot_btn1]
    p2_bet_buttons = [half_pot_btn2, pot_btn2, two_pot_btn2]
    win_func_buttons = [yes_button]
    screen_buttons = [return_btn]

    #main game screen loop
    while True:
        mouse_up = False
        #checks func state and acts accordingly
        match func_state:
            #deals player cards
            case PokerFuncs.DEAL:
                game.deal_player_cards()
                p1_cards = p1.get_hole()
                p2_cards = p2.get_hole()
                func_state = PokerFuncs.TURN
                log_event("dealt_cards")
            #call means player wants to see another card. if p1 calls this the turn changes to p2
            #if it is the first time to call, three cards are dealt. the second and third time one card are dealt
            #boolean values are used to track which card should be dealt
            #after the fifth card there is a winner. 
            case PokerFuncs.CALL:
                if matched_bet != True:
                    turn.cash -= current_bet
                    pot_amount += current_bet
                    current_bet = 0.0
                    matched_bet = True
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
                elif turned and rivered and turn == p2:
                    is_winner = True
                    winner.win_count += 1
                    winner.cash += pot_amount
                    winners["winner"] = winner.name
                    log_event("rivered_card")
                    log_event(f"{winner.name}_won${pot_amount:.2f}_with_{winner.hand_rank.value[1]} and cards {winner.best_hand}")
                    func_state = PokerFuncs.END_GAME if p1.cash <= 0.0 or p2.cash <= 0.0 else PokerFuncs.TURN
                #if either player folds, the other player wins. They obtain the pot
            case PokerFuncs.FOLD:
                if turn == p1:
                    winner = p2
                    p2.cash += pot_amount
                    log_event("p1_folded")
                elif turn == p2:
                    winner = p1
                    p1.cash += pot_amount
                    log_event("p2_folded")
                is_winner = True
                winners["winner"] = winner.name
                winner.win_count += 1
                log_event(f"{winner.name}_won_${pot_amount:.2f}_with_{winner.hand_rank.value[1]} and cards {winner.best_hand}")
                func_state = PokerFuncs.END_GAME if p1.cash <= 0.0 or p2.cash <= 0.0 else PokerFuncs.TURN
                #if a player bets the amount is added to the pot, subtracted from their pile, and the turn changes to the next player
                #the next player must match or raise the amount bet
            case PokerFuncs.BET:
                is_bet = True
                func_state = PokerFuncs.TURN
            case PokerFuncs.HALF_POT:
                is_bet = False
                matched_bet = False
                current_bet = round(pot_amount / 2, 2)
                pot_amount += current_bet
                turn.cash -= current_bet
                log_event(f"{turn.name} bet {current_bet}")
                if turn == p1:
                    turn = p2
                else:
                    turn = p1
                func_state = PokerFuncs.TURN
            case PokerFuncs.POT:
                is_bet = False
                matched_bet = False
                current_bet = pot_amount
                pot_amount += current_bet
                turn.cash -= current_bet
                log_event(f"{turn.name} bet {current_bet}")
                if turn == p1:
                    turn = p2
                else:
                    turn = p1
                func_state = PokerFuncs.TURN
            case PokerFuncs.TWO_POT:
                is_bet = False
                matched_bet = False
                current_bet = pot_amount * 2
                pot_amount += current_bet
                turn.cash -= current_bet
                log_event(f"{turn.name} bet {current_bet}")
                if turn == p1:
                    turn = p2
                else:
                    turn = p1
                func_state = PokerFuncs.TURN
            case PokerFuncs.END_GAME:
                log_event("someone is broke, in end game")
                if winners["winner"] == p1:
                    debtor = p2
                else:
                    debtor = p1
                winners["debt"] = debtor.cash * -1
                end_game = True
                func_state = PokerFuncs.TURN
            #new game resets the players and board
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
                pot_amount = ANTE * 2
                p1.cash -= ANTE
                p2.cash -= ANTE
                turn = p1
                func_state = PokerFuncs.DEAL
                #turn is an idle state. It goes to this after a button is used to wait for the next UI
            case PokerFuncs.TURN:
                pass
        if end_game == True:
            return GameState.WIN
        
        #looks for mouse input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                log_event("quit_game")
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True
        #sets background color
        screen.fill(SCREEN_COLOR)

        #init deck image
        deck_rect = get_deck_img()
        deck_pic = CARD_SHEET.subsurface(deck_rect)
        screen.blit(deck_pic, (DECK_INIT_WIDTH, DECK_INIT_HEIGHT))

        #init title message
        pygame.draw.rect(screen, SCREEN_COLOR, title_box, 2)
        title_surface = title_font.render(f"POKER GAME", True, TEXT_COLOR)
        screen.blit(title_surface, (title_box.x + 5, title_box.y + 5))

        #init pot amount
        if is_winner != True:
            pygame.draw.rect(screen, SCREEN_COLOR, pot_box, 2)
            pot_surface = player_font.render(f"Pot: ${pot_amount:.2f}", True, TEXT_COLOR)
            screen.blit(pot_surface, (pot_box.x + 5, pot_box.y + 5))
        #init p1 name, cash, and cards. Can only be seen by p1. p2 sees deck image in card place, and cannot see the hand of the player
        pygame.draw.rect(screen, SCREEN_COLOR, p1_name_box, 2)
        pygame.draw.rect(screen, SCREEN_COLOR, p1_cash_box, 2)
        p1_cash_surface = player_font.render(f"Cash: ${p1.cash:.2f}", True, TEXT_COLOR)
        screen.blit(p1_cash_surface, (p1_cash_box.x + 5, p1_cash_box.y + 5))
        if turn == p1 or is_winner:
            p1_name_surface = player_font.render(f"{p1.name}: {p1.score_hand().value[1]}", True, TEXT_COLOR)
            screen.blit(p1_name_surface, (p1_name_box.x + 5, p1_name_box.y + 5))
            p1_card1_rect = get_card_rect(p1_cards[0].__repr__())
            p1_card1_pic = CARD_SHEET.subsurface(p1_card1_rect)
            screen.blit(p1_card1_pic, (P1_CARD1_WIDTH, PLAYER_CARD_HEIGHT))
            p1_card2_rect = get_card_rect(p1_cards[1].__repr__())
            p1_card2_pic = CARD_SHEET.subsurface(p1_card2_rect)
            screen.blit(p1_card2_pic, (P1_CARD2_WIDTH, PLAYER_CARD_HEIGHT))
        else:
            p1_name_surface = player_font.render(f"{p1.name}", True, TEXT_COLOR)
            screen.blit(p1_name_surface, (p1_name_box.x + 5, p1_name_box.y + 5))
            screen.blit(deck_pic, (P1_CARD1_WIDTH, PLAYER_CARD_HEIGHT))
            screen.blit(deck_pic, (P1_CARD2_WIDTH, PLAYER_CARD_HEIGHT))

        #init p2 name, cash, cards. can only be seen by p2. p1 sees deck image on their turn
        pygame.draw.rect(screen, SCREEN_COLOR, p2_name_box, 2)
        pygame.draw.rect(screen, SCREEN_COLOR, p2_cash_box, 2)
        p2_cash_surface = player_font.render(f"Cash: ${p2.cash:.2f}", True, TEXT_COLOR)
        screen.blit(p2_cash_surface, (p2_cash_box.x + 5, p2_cash_box.y + 5))
        if turn == p2 or is_winner:
            p2_name_surface = player_font.render(f"{p2.name}: {p2.score_hand().value[1]}", True, TEXT_COLOR)
            screen.blit(p2_name_surface, (p2_name_box.x + 5, p2_name_box.y + 5))
            p2_card1_rect = get_card_rect(p2_cards[0].__repr__())
            p2_card1_pic = CARD_SHEET.subsurface(p2_card1_rect)
            screen.blit(p2_card1_pic, (P2_CARD1_WIDTH, PLAYER_CARD_HEIGHT))
            p2_card2_rect = get_card_rect(p2_cards[1].__repr__())
            p2_card2_pic = CARD_SHEET.subsurface(p2_card2_rect)
            screen.blit(p2_card2_pic, (P2_CARD2_WIDTH, PLAYER_CARD_HEIGHT))
        else:
            p2_name_surface = player_font.render(f"{p2.name}", True, TEXT_COLOR)
            screen.blit(p2_name_surface, (p2_name_box.x + 5, p2_name_box.y + 5))
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
            #says who's turn it is
            pygame.draw.rect(screen, SCREEN_COLOR, winner_box, 2)
            winner_surface = title_font.render(f"{turn.name}'s turn", True, TEXT_COLOR)
            screen.blit(winner_surface, (winner_box.x + 5, winner_box.y + 5))

        #if there is a winner, puts buttons for new game on screen
        if is_winner:
            for button in win_func_buttons:
                ui_action = button.poker_func_update(pygame.mouse.get_pos(), mouse_up)
                if ui_action is not None:
                    func_state = ui_action
                button.draw(screen)

            for button in win_screen_buttons:
                ui_action = button.screen_update(pygame.mouse.get_pos(), mouse_up)
                if ui_action is not None:
                    return ui_action
                button.draw(screen)
        else:
            #if there is no winner yet, draws buttons for the player whose turn it is
            if turn == p1:
                if is_bet == False:
                    for button in p1_func_buttons:
                        ui_action = button.poker_func_update(pygame.mouse.get_pos(), mouse_up)
                        if ui_action is not None:
                            func_state = ui_action
                        button.draw(screen)
                    for button in screen_buttons:
                        ui_action = button.screen_update(pygame.mouse.get_pos(), mouse_up)
                        if ui_action is not None:
                            return ui_action
                        button.draw(screen)
                else:
                    for button in p1_bet_buttons:
                        ui_action = button.poker_func_update(pygame.mouse.get_pos(), mouse_up)
                        if ui_action is not None:
                            func_state = ui_action
                        button.draw(screen)
                    for button in screen_buttons:
                        ui_action = button.screen_update(pygame.mouse.get_pos(), mouse_up)
                        if ui_action is not None:
                            return ui_action
                        button.draw(screen)
            if turn == p2:
                if is_bet == False:
                    for button in p2_func_buttons:
                        ui_action = button.poker_func_update(pygame.mouse.get_pos(), mouse_up)
                        if ui_action is not None:
                            func_state = ui_action
                        button.draw(screen)

                    for button in screen_buttons:
                        ui_action = button.screen_update(pygame.mouse.get_pos(), mouse_up)
                        if ui_action is not None:
                            return ui_action
                        button.draw(screen)
                else:
                    for button in p2_bet_buttons:
                        ui_action = button.poker_func_update(pygame.mouse.get_pos(), mouse_up)
                        if ui_action is not None:
                            func_state = ui_action
                        button.draw(screen)

                    for button in screen_buttons:
                        ui_action = button.screen_update(pygame.mouse.get_pos(), mouse_up)
                        if ui_action is not None:
                            return ui_action
                        button.draw(screen)
        pygame.display.flip()
        clock.tick(60)
