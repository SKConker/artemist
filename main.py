import pygame , sys
import keyboard

import spritesheet
from pygame.locals import*

pygame.init()

# game window
display_surface = pygame.display.set_mode((600, 500))
window_dim_width = 600
window_dim_height = 500
pygame.display.set_caption("Some Shooter")
icon = pygame.image.load('bow-and-arrow.png')
pygame.display.set_icon(icon)

x = 20
y = 420
width = 50
height = 60
velocity = 5



# Setting up the background

layer_0 = pygame.image.load('Layer_0.png')
layer_1 = pygame.image.load('Layer_1.png')
layer_2 = pygame.image.load('Layer_2.png')
layer_3 = pygame.image.load('Layer_3.png')
layer_4 = pygame.image.load('Layer_4.png')
layer_5 = pygame.image.load('Layer_5.png')
layer_6 = pygame.image.load('Layer_6.png')
layer_7 = pygame.image.load('Layer_7_Lights.png')
layer_8 = pygame.image.load('Layer_8.png')
layer_9 = pygame.image.load('Layer_9.png')
layer_10 = pygame.image.load('Layer_10.png')
layer_11 = pygame.image.load('Layer_11.png')

Background = [layer_0, layer_2, layer_3, layer_4, layer_5, layer_6, layer_7, layer_8, layer_9, layer_10, layer_11]

background_1 = 0
background_2 = 0


def background():
    for i in range(0, 11):
        background_image = Background[i]
        display_surface.blit(background_image, (background_1, background_2))

# setting up sprites
sprite_sheet_image = pygame.image.load('sprite_sheet.png').convert_alpha()
sprite_sheet = spritesheet.SpriteSheet(sprite_sheet_image)

BLACK = (0, 0, 0)

# Getting a specific frame from the sprite_sheet
# Creating animation list

animation_idle_list = []
animation_running_list = []
animation_shooting_list = []
animation_roll_list = []
animation_double_jump_list = []
animation_death_list = []
animation_fall_list = []

animation_steps = [4, 8, 7, 7, 4, 8, 2]
last_update = pygame.time.get_ticks()
animation_cooldown = 150
frame = 0

for i in range(len(animation_steps)):
    for x in range(animation_steps[0]):
        animation_idle_list.append(sprite_sheet.get_image_idle(x, 64, 64, 1, BLACK))

for x in range(8):
    animation_running_list.append(sprite_sheet.get_image_running(x, 64, 64, 1, BLACK))

for x in range(animation_steps[2]):
    animation_shooting_list.append(sprite_sheet.get_image_shoot(x, 64, 64, 1, BLACK))




isJump = False
jumpcount = 10
running = True

# main game loop

while running:

    # filling background
    display_surface.fill((0, 128, 128))
    background()

    pygame.display.update()

    # update animation
    current_time = pygame.time.get_ticks()
    if current_time - last_update >= animation_cooldown:
        frame += 1
        last_update = current_time
        if frame >= len(animation_idle_list):
            frame = 0

    display_surface.blit((animation_idle_list[frame]), (x, y))


    # updating animation
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > velocity:
        x -= velocity

    if keys[pygame.K_RIGHT] and x < window_dim_width - width - velocity:
        x += velocity

    if not(isJump):

        if keys[pygame.K_UP] and y > velocity:
            y -= velocity

        if keys[pygame.K_DOWN] and y < window_dim_height - height - velocity:
            y += velocity

        if keys[pygame.K_SPACE]:
            isJump = True

    else:

        if jumpcount >= -10:
            neg = 1
            if jumpcount < 0:
                neg = -1
            y -= (jumpcount ** 2) * 0.5 * neg
            jumpcount -= 1

        else:
            isJump = False
            jumpcount = 10


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
