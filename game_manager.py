import pygame
import constants
import utils
import random

from character import *
from input_handler import *

print()
class GameManager():
    def __init__(self, speed_pad1, speed_pad2, ball_speed, screen):
        self.ball_advantage = 'Left'
        self.pong = Ball(constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2, ball_speed)
        self.paddle1 = Paddle(15, constants.SCREEN_HEIGHT/2)
        self.paddle2 = Paddle(constants.SCREEN_WIDTH-15, constants.SCREEN_HEIGHT/2)
        self.speed_pad1 = speed_pad1
        self.speed_pad2 = speed_pad2
        self.screen = screen
        self.input_handler = InputHandler()
        self.run = True
        self.dashes = []
        self.score1 = 0
        self.score2 = 0
        # Define dashes
        for i in range(0, 8):
            dash = pygame.Rect(0, 0, 10, constants.SCREEN_HEIGHT/16)
            dash.midtop = (constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/8 * i + constants.SCREEN_HEIGHT/16/2)
            self.dashes.append(dash)
        

    def reset_game(self):
        # Random direction for the ball
        rand_x = random.randint(1, 2)
        rand_y = random.randint(1, 2)

        if rand_x == 1:
            self.pong.dx = abs(self.pong.dx)
        elif rand_x == 2:
            self.pong.dx = -abs(self.pong.dx)
        if rand_y == 1:
            self.pong.dy = abs(self.pong.dy)
        elif rand_y == 2:
            self.pong.dy = -abs(self.pong.dy)

        self.pong.rect.center = (constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2)
        self.paddle1.rect.centery = constants.SCREEN_HEIGHT/2
        self.paddle2.rect.centery = constants.SCREEN_HEIGHT/2


    def update(self):
        self.input_handler.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False

        # Define borders
        top_border = pygame.Rect(0, 0, constants.SCREEN_WIDTH, 10)
        top_border.midbottom = (constants.SCREEN_WIDTH/2, 0)

        right_border = pygame.Rect(0, 0, 10, constants.SCREEN_HEIGHT)
        right_border.midleft = (constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT/2)

        bottom_border = pygame.Rect(0, 0, constants.SCREEN_WIDTH, 10)
        bottom_border.midtop = (constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT)

        left_border = pygame.Rect(0, 0, 10, constants.SCREEN_WIDTH)
        left_border.midright = (0, constants.SCREEN_HEIGHT/2)




        moving_up_pad1 = False
        moving_down_pad1 = False

        moving_up_pad2 = False
        moving_down_pad2 = False


        if self.input_handler.is_key_pressed(pygame.K_w):
            moving_up_pad1 = True
        if self.input_handler.is_key_pressed(pygame.K_s):
            moving_down_pad1 = True
        if self.input_handler.is_key_pressed(pygame.K_UP):
            moving_up_pad2 = True
        if self.input_handler.is_key_pressed(pygame.K_DOWN):
            moving_down_pad2 = True
        
        dy1 = 0
        dy2 = 0

        if moving_up_pad1:
            dy1 = -self.speed_pad1
        if moving_down_pad1:
            dy1 = self.speed_pad1
        if moving_up_pad2:
            dy2 = -self.speed_pad2
        if moving_down_pad2:
            dy2 = self.speed_pad2



        self.paddle1.move(dy1)
        self.paddle2.move(dy2)

        collided_wall = self.pong.move(top_border, right_border, bottom_border, left_border, self.paddle1.get_rect(), self.paddle2.get_rect())

        if collided_wall == 'Left':
            self.ball_advantage = 'Right'
            self.score2 += 1
            self.reset_game()
        elif collided_wall == 'Right':
            self.ball_advantage = 'Left'
            self.score1 += 1
            self.reset_game()

        pygame.display.update()

    def draw(self):
        self.screen.fill(constants.BG)

        # Draw dashes
        for dash in self.dashes:
            print(len(self.dashes))
            pygame.draw.rect(self.screen, constants.WHITE, dash)

        utils.draw_text(str(self.score1), 'Arial', 48, constants.WHITE, constants.SCREEN_WIDTH/4, 75, self.screen)
        utils.draw_text(str(self.score2), 'Arial', 48, constants.WHITE, constants.SCREEN_WIDTH/4*3, 75, self.screen)

        self.paddle1.draw(self.screen)
        self.paddle2.draw(self.screen)
        self.pong.draw(self.screen)