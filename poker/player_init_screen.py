import pygame
from poker.UIElement import *
from poker.constants import *
from poker.log_event import *

names = {"p1" : "", "p2" : "",}
def player_init_screen(screen):
    info_text1 = "Click the button to type your name."
    info_text2 = "The enter button will save it!"
    info_box1 = pygame.Rect(SCREEN_CENTERX - 300, CARD_BUFFER, 180, 40)
    info_box2 = pygame.Rect(SCREEN_CENTERX - 250, CARD_BUFFER + 60, 180, 40)
    info_font = pygame.font.SysFont("Comic Sans MS", 48)
    p1_btn = UIElement(
        center_position=(SCREEN_CENTERX, SCREEN_CENTERY - 150),
        font_size=50,
        bg_rgb=SCREEN_COLOR,
        text_rgb=TEXT_COLOR,
        text="Enter Player 1's Name: ",
        action=None,
        active = False
    )
    p2_btn = UIElement(
        center_position=(SCREEN_CENTERX, SCREEN_CENTERY),
        font_size=50,
        bg_rgb=SCREEN_COLOR,
        text_rgb=TEXT_COLOR,
        text="Enter Player 2's Name: ",
        action=None,
        active = False
    )
    start_btn = UIElement(
        center_position=(SCREEN_CENTERX, SCREEN_CENTERY + 150),
        font_size=50,
        bg_rgb=SCREEN_COLOR,
        text_rgb=TEXT_COLOR,
        text="Start Game",
        action=GameState.POKER_GAME
    )
    buttons = [p1_btn, p2_btn, start_btn]
    clock = pygame.time.Clock()

    while True:
        mouse_up = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                log_event("quit_game")
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True
                if p1_btn.rect.collidepoint(event.pos):
                    p1_btn.name = ""
                    p1_btn.active = True
                elif p2_btn.rect.collidepoint(event.pos):
                    p2_btn.name = ""
                    p2_btn.active = True
                else:
                    p1_btn.active = False
                    p2_btn.active = False
            if event.type == pygame.KEYDOWN and p1_btn.active:
                    if event.key == pygame.K_BACKSPACE:
                        curr = names["p1"]
                        bkspc = curr[:-1]
                        names["p1"] = bkspc
                        p1_btn.del_text()
                    elif event.key == pygame.K_RETURN:
                        print("Input submitted:", names["p1"])
                        p1_btn.active = False
                        #p1_name = ""  # Reset after submission
                    else:
                        names["p1"] += event.unicode
                        p1_btn.add_text(event.unicode)
            elif event.type == pygame.KEYDOWN and p2_btn.active:
                if event.key == pygame.K_BACKSPACE:
                    curr = names["p2"]
                    bkspc = curr[:-1]
                    names["p2"] = bkspc
                    p2_btn.del_text()
                elif event.key == pygame.K_RETURN:
                    p2_btn.active = False
                    print("Input submitted:", names["p2"])
                    #p2_name = ""  # Reset after submission
                else:  
                    names["p2"] += event.unicode
                    p2_btn.add_text(event.unicode)

        screen.fill(SCREEN_COLOR)
        #init info message
        pygame.draw.rect(screen, SCREEN_COLOR, info_box1, 2)
        info_surface1 = info_font.render(info_text1, True, TEXT_COLOR)
        screen.blit(info_surface1, (info_box1.x + 5, info_box1.y + 5))
        pygame.draw.rect(screen, SCREEN_COLOR, info_box2, 2)
        info_surface2 = info_font.render(info_text2, True, TEXT_COLOR)
        screen.blit(info_surface2, (info_box2.x + 5, info_box2.y + 5))

        for button in buttons:
            ui_action = button.update(pygame.mouse.get_pos(), mouse_up)
            if ui_action is not None:
                return ui_action
            button.draw(screen)

        pygame.display.flip()
        clock.tick(60)