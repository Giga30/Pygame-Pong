import pygame
import constants
import math
import random

class Ball():
    def __init__(self, x, y, speed):
        self.rect = pygame.Rect(0, 0, 10, 10)
        self.rect.center = (x, y)

        self.speedx = speed
        self.speedy = speed
        # Define dx and dy as a normalized diagonal speed
        self.length = math.sqrt(self.speedx**2 + self.speedy**2)
        self.dx = abs(self.speedx) / self.length * self.speedx
        self.dy = abs(self.speedy) / self.length * self.speedy

    def move(self, top_border, right_border, bottom_border, left_border, paddle1, paddle2):
        # Bounce off the walls
        if self.rect.colliderect(top_border):
            self.dy *= -1
        if self.rect.colliderect(right_border):
            self.dx *= -1
        if self.rect.colliderect(bottom_border):
            self.dy *= -1
        if self.rect.colliderect(left_border):
            self.dx *= -1
        if self.rect.colliderect(paddle1):
            self.dx *= -1
        if self.rect.colliderect(paddle2):
            self.dx *= -1
        
        # Move the ball
        self.rect.x += self.dx
        self.rect.y += self.dy

    def draw(self, surface):
        pygame.draw.rect(surface, constants.WHITE, self.rect)


class Paddle():
    def __init__(self, x, y):
        self.rect = pygame.Rect(0, 0, 10, 100)
        self.rect.center = (x, y)

    def move(self, dy, top_border, bottom_border):
        print(self.rect.centery - self.rect.size[1]/2)
        if (self.rect.centery - self.rect.size[1]/2 <= 0 and dy > 0) or (self.rect.centery + self.rect.size[1]/2 >= constants.SCREEN_HEIGHT and dy < 0):
            self.rect.y += dy
        elif self.rect.centery - self.rect.size[1]/2 > 0 and self.rect.centery + self.rect.size[1]/2 < constants.SCREEN_HEIGHT:
            self.rect.y += dy
    
    def draw(self, surface):
        pygame.draw.rect(surface, constants.WHITE, self.rect)
    
    def get_rect(self):
        return self.rect