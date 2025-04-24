import pygame
import constants
from game_manager import *
import cProfile


def main():
    pygame.init()

    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))

    clock = pygame.time.Clock()

    game_manager = GameManager(5, 5, 2.5, screen)
    while game_manager.run:
        game_manager.update()
        game_manager.draw()
        
        clock.tick(constants.FPS)
cProfile.run('main()')
    



    




