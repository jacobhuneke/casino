from poker.card_sheet import *
from poker.poker_game import *
import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    running = True
    #is_start = True
    #active = False
    CARD_SHEET = pygame.image.load("poker/images/cards-sheet.png").convert_alpha()
    CARD_SHEET = pygame.transform.scale(CARD_SHEET, (CARD_SHEET_WIDTH, CARD_SHEET_HEIGHT))
    title_box = pygame.Rect(DECK_INIT_WIDTH, CARD_BUFFER, 180, 40)
    p1_box = pygame.Rect(DECK_INIT_WIDTH, PLAYER_NAME_HEIGHT, 180, 40)
    p2_box = pygame.Rect(SCREEN_WIDTH - DECK_INIT_WIDTH - (180 * 2), PLAYER_NAME_HEIGHT, 180, 40)
    title_font = pygame.font.SysFont("Comic Sans MS", 64)
    title_font.set_underline(True)
    player_font = pygame.font.SysFont("Comic Sans MS", 48)
    #text_value = ""
    king_of_hearts_rect = get_card_rect("Ace of Clubs")
    king_of_hearts_pic = CARD_SHEET.subsurface(king_of_hearts_rect)
    screen.blit(king_of_hearts_pic, (650, 350))

    p1 = Player("Jake")
    p2 = Player("Lainey")
    game = PokerGame(p1, p2)
    game.deal_player_cards()
    p1_cards = p1.get_hole()
    p2_cards = p2.get_hole()
    print(p1_cards, p2_cards)
    game.deal_flop()
    game.deal_turn()
    game.deal_turn()

    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
        screen.fill(SCREEN_COLOR)
        # RENDER YOUR GAME HERE
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
        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(60)

    pygame.quit()
main()

    #king_of_hearts_rect = get_card_rect("A of Clubs")
    #king_of_hearts_pic = CARD_SHEET.subsurface(king_of_hearts_rect)
    #screen.blit(king_of_hearts_pic, (650, 350)) 
#p1 = Player("Jake")
    #p2 = Player("Lainey")
    #game = PokerGame(p1, p2)
    #ante up
    #game.deal_player_cards()
    #bets?
    #game.deal_flop()
    
    #print(f"Jake's cards are: {p1.get_hole()}")
    #print(f"Lainey's cards are: {p2.get_hole()}\n")

   
    #game.deal_turn()
    #print(f"The cards on the board are: {game.flop}")
    
    
    #print(f"Jake has a {p1.score_hand().value[1]}, {p1.best_hand}")
    #print(f"Lainey has a {p2.score_hand().value[1]}, {p2.best_hand}\n")
    #game.deal_turn()
    #print(f"The cards on the board are: {game.flop}")
    #print(f"Jake has a {p1.score_hand().value[1]}, {p1.best_hand}")
    #print(f"Lainey has a {p2.score_hand().value[1]}, {p2.best_hand}\n")
    #game.deal_turn()
    #print(f"The cards on the board are: {game.flop}")
    #print(f"Jake has a {p1.score_hand().value[1]}, {p1.best_hand}")
    #print(f"Lainey has a {p2.score_hand().value[1]}, {p2.best_hand}")

#    winner = get_winner(p1, p2)
 #   if winner != None:
  #      print(f"The winner is: {winner.name}, with a {winner.hand_rank.value[1]}")
   
   # else:
    #    print(f"There was a Tie! Both players win")