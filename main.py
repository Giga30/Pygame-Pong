import pygame
import constants
from character import *
pygame.init()

screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))

clock = pygame.time.Clock()

# Define borders
top_border = pygame.Rect(0, 0, constants.SCREEN_WIDTH, 10)
top_border.midbottom = (constants.SCREEN_WIDTH/2, 0)

right_border = pygame.Rect(0, 0, 10, constants.SCREEN_HEIGHT)
right_border.midleft = (constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT/2)

bottom_border = pygame.Rect(0, 0, constants.SCREEN_WIDTH, 10)
bottom_border.midtop = (constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT)

left_border = pygame.Rect(0, 0, 10, constants.SCREEN_WIDTH)
left_border.midright = (0, constants.SCREEN_HEIGHT/2)

# Make the dashes in the middle
mid_dashes = []

moving_up_pad1 = False
moving_down_pad1 = False

moving_up_pad2 = False
moving_down_pad2 = False

speed_pad1 = 5
speed_pad2 = 5

for i in range(0, 8):
    dash = pygame.Rect(0, 0, 10, constants.SCREEN_HEIGHT/16)
    dash.midtop = (constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/8 * i + constants.SCREEN_HEIGHT/16/2)
    mid_dashes.append(dash)

pong = Ball(100, constants.SCREEN_HEIGHT/2, 2.5)
paddle1 = Paddle(15, constants.SCREEN_HEIGHT/2)
paddle2 = Paddle(constants.SCREEN_WIDTH-15, constants.SCREEN_HEIGHT/2)

run = True
while run:
    clock.tick(constants.FPS)
    screen.fill(constants.BG)
    keys = pygame.key.get_pressed()

    dy1 = 0
    dy2 = 0

    if moving_up_pad1:
        dy1 = -speed_pad1
    if moving_down_pad1:
        dy1 = speed_pad1
    if moving_up_pad2:
        dy2 = -speed_pad2
    if moving_down_pad2:
        dy2 = speed_pad2

    paddle1.move(dy1)
    paddle2.move(dy2)
    paddle1.draw(screen)
    paddle2.draw(screen)
    pong.move(top_border, right_border, bottom_border, left_border, paddle1.get_rect(), paddle2.get_rect())
    pong.draw(screen)
    # Draw the dashes
    for i in mid_dashes:
        pygame.draw.rect(screen, constants.WHITE, i)

    pygame.display.update()


    if keys[pygame.K_w]:
        moving_up_pad1 = True
        moving_down_pad1 = False

    if keys[pygame.K_s]:
        moving_down_pad1 = True
        moving_up_pad1 = False

    if keys[pygame.K_UP]:
        moving_up_pad2 = True
        moving_down_pad2 = False

    if keys[pygame.K_DOWN]:
        moving_down_pad2 = True
        moving_up_pad2 = False

    if keys[pygame.K_s] and keys[pygame.K_w]:
        moving_up_pad1 = False
        moving_down_pad1 = False

    if keys[pygame.K_UP] and keys[pygame.K_DOWN]:
        moving_up_pad2 = False
        moving_down_pad2 = False


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w :
                moving_up_pad1 = False
            if event.key == pygame.K_s:
                moving_down_pad1 = False
            if event.key == pygame.K_UP:
                moving_up_pad2 = False
            if event.key == pygame.K_DOWN:
                moving_down_pad2 = False