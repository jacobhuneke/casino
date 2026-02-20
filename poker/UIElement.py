import pygame
import pygame.freetype
from pygame.sprite import Sprite
from enum import Enum

def create_surface_with_text(text, font_size, text_rgb, bg_rgb):
    """ Returns surface with text written on """
    font = pygame.freetype.SysFont("Comic Sans MS", font_size)
    surface, _ = font.render(text=text, fgcolor=text_rgb, bgcolor=bg_rgb)
    return surface.convert_alpha()

class UIElement(Sprite):
    def __init__(self, center_position, text, font_size, bg_rgb, text_rgb, screen_action=None, active=None, poker_func=None):
        self.mouse_over = False
        self.center_position = center_position
        self.text = text
        self.font_size = font_size
        self.text_rgb = text_rgb
        self.bg_rgb = bg_rgb
        self.name = ""
        default_image = create_surface_with_text(
            text=text, font_size=font_size, text_rgb=text_rgb, bg_rgb=bg_rgb
        )
        highlighted_image = create_surface_with_text(
            text=text, font_size=font_size * 1.2, text_rgb="#def440", bg_rgb=bg_rgb
        )

        self.images = [default_image, highlighted_image]
        self.rects = [default_image.get_rect(center = center_position),
                      highlighted_image.get_rect(center = center_position)]
        self.screen_action = screen_action
        self.active = active
        self.poker_func = poker_func
        super().__init__()

    @property
    def image(self):
        return self.images[1] if self.mouse_over else self.images[0]

    @property
    def rect(self):
        return self.rects[1] if self.mouse_over else self.rects[0]
    
    #deletes the last character from the name variable (when backspace is typed)
    def del_text(self):
        self.name = self.name[:-1]
        self.default_image = create_surface_with_text(
            text=self.text + self.name, font_size=self.font_size, text_rgb=self.text_rgb, bg_rgb=self.bg_rgb
        )
        self.highlighted_image = create_surface_with_text(
            text=self.text + self.name, font_size=(self.font_size * 1.2), text_rgb="#def440", bg_rgb=self.bg_rgb
        )
        self.images = [self.default_image, self.highlighted_image]
        self.rects = [self.default_image.get_rect(center = self.center_position),
                      self.highlighted_image.get_rect(center = self.center_position)]

    #adds a char to the name variable
    def add_text(self, new_text):
        self.name += new_text
        self.default_image = create_surface_with_text(
            text=(self.text + self.name), font_size=self.font_size, text_rgb=self.text_rgb, bg_rgb=self.bg_rgb
        )
        self.highlighted_image = create_surface_with_text(
            text=(self.text + self.name), font_size=(self.font_size * 1.2), text_rgb="#def440", bg_rgb=self.bg_rgb
        )
        self.images = [self.default_image, self.highlighted_image]
        self.rects = [self.default_image.get_rect(center = self.center_position),
                      self.highlighted_image.get_rect(center = self.center_position)]

    def screen_update(self, mouse_pos, mouse_up):
        if self.rect.collidepoint(mouse_pos):
            self.mouse_over = True
            if mouse_up:
                return self.screen_action
        else:
            self.mouse_over = False

    def poker_func_update(self, mouse_pos, mouse_up):
        if self.rect.collidepoint(mouse_pos):
            self.mouse_over = True
            if mouse_up:
                return self.poker_func
        else:
            self.mouse_over = False

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class GameState(Enum):
    QUIT = -1
    TITLE = 0
    POKER_GAME = 1
    PLAYER_INIT = 2
    NAME = 25

class PokerFuncs(Enum):
    DEAL = 1
    CALL = 2
    BET = 3
    FOLD = 4
    TURN = 5
    END_GAME = 0
    NEW_GAME = 10