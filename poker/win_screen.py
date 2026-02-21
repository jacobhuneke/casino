import pygame
from poker.UIElement import *
from poker.constants import *
from poker.log_event import *
from poker.play_game_screen import winners

def win_screen(screen):
    start_btn = UIElement(
        center_position=(SCREEN_CENTERX, SCREEN_CENTERY),
        font_size=50,
        bg_rgb=SCREEN_COLOR,
        text_rgb=TEXT_COLOR,
        text="Start a new game",
        screen_action=GameState.PLAYER_INIT,
    )
    quit_btn = UIElement(
        center_position=(SCREEN_CENTERX, SCREEN_CENTERY + 150),
        font_size=50,
        bg_rgb=SCREEN_COLOR,
        text_rgb=TEXT_COLOR,
        text="No thanks",
        screen_action=GameState.QUIT,
    )
    win_message_box = pygame.Rect(SCREEN_CENTERX - 400, SCREEN_CENTERY - 150, 180, 40)
    money_owed_box = pygame.Rect(SCREEN_CENTERX - 300, SCREEN_CENTERY - 100, 180, 40)
    font = pygame.font.SysFont("Comic Sans MS", 48)
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

        pygame.draw.rect(screen, SCREEN_COLOR, win_message_box, 2)
        win_surface = font.render(f"{winners["winner"]} won cause the other guy ran outta money,", True, TEXT_COLOR)
        screen.blit(win_surface, (win_message_box.x + 5, win_message_box.y + 5))

        pygame.draw.rect(screen, SCREEN_COLOR, money_owed_box, 2)
        money_owed_surface = font.render(f"who owes ${winners["debt"]:.2f} to the winner", True, TEXT_COLOR)
        screen.blit(money_owed_surface, (money_owed_box.x + 5, money_owed_box.y + 5))

        for button in buttons:
            ui_action = button.screen_update(pygame.mouse.get_pos(), mouse_up)
            if ui_action is not None:
                return ui_action
            button.draw(screen)

        pygame.display.flip()