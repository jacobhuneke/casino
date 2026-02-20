import pygame
from poker.UIElement import *
from poker.constants import *
from poker.log_event import *

def title_screen(screen):
    start_btn = UIElement(
        center_position=(SCREEN_CENTERX, SCREEN_CENTERY),
        font_size=50,
        bg_rgb=SCREEN_COLOR,
        text_rgb=TEXT_COLOR,
        text="Start 2 Player Poker Game",
        screen_action=GameState.PLAYER_INIT,
    )
    quit_btn = UIElement(
        center_position=(SCREEN_CENTERX, SCREEN_CENTERY + 150),
        font_size=50,
        bg_rgb=SCREEN_COLOR,
        text_rgb=TEXT_COLOR,
        text="Quit",
        screen_action=GameState.QUIT,
    )

    buttons = [start_btn, quit_btn]

    while True:
        mouse_up = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                log_event("quit_game")
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True
        screen.fill(SCREEN_COLOR)

        for button in buttons:
            ui_action = button.screen_update(pygame.mouse.get_pos(), mouse_up)
            if ui_action is not None:
                return ui_action
            button.draw(screen)

        pygame.display.flip()