import pygame
import constants
from game_manager import *
pygame.init()

screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))

clock = pygame.time.Clock()

# Simplify text implementation for later use
# text_font = pygame.font.SysFont('Arial', 12, bold=False, italic=False)
# def draw_text(text, font, text_col, x, y):
#     img = font.render(text, True, text_col)
#     screen.blit(img, (x, y))


game_manager = GameManager(5, 5, screen)
while game_manager.run:
    game_manager.update()
    game_manager.draw()
    
    clock.tick(constants.FPS)

    



    




