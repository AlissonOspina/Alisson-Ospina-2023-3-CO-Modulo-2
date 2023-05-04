import pygame

from dino_runner.utils.constants import FONT_STYLE, SCREEN_HEIGHT, SCREEN_WIDTH

class Menssage:
    POSITION_X = SCREEN_WIDTH 
    POSITION_Y = SCREEN_HEIGHT 

    def __init__(self, screen): 
        screen.fill((225, 225, 225))
        self.font = pygame.font.Font(FONT_STYLE, 28)
        
             
    def write_messages(self, message, POSITION_X, POSITION_Y, screen):
        self.text = self.font.render(message, True, (0, 0, 0))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (POSITION_X, POSITION_Y)
        screen.blit(self.text, self.text_rect)

    def draw(self, screen):
        screen.blit(self.text, self.text_rect)

    
