from sys import exit
from time import sleep
import pygame

import start_screen

pygame.init()


def click_play():
    print("aa")


def click_options():
    print("vv")


def exit_game():
    sleep(0.45)
    pygame.quit()
    exit()


screen = pygame.display.set_mode((800, 880))
screen.fill((0, 0, 0))
pygame.display.set_caption("Tetris")
clock = pygame.time.Clock()

click_sound = start_screen.get_click_sound()
play_button, options_button, exit_button = start_screen.create_buttons(click_sound, 1)
frame = start_screen.create_frame()
text = start_screen.create_text()
background_blocks = start_screen.create_bg_blocks()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game()

    play_button.draw(screen)
    play_button.click_left(click_play)

    options_button.draw(screen)
    options_button.click_left(click_options)

    exit_button.draw(screen)
    exit_button.click_left(exit_game)

    for block in frame:
        block.draw(screen)

    for block in text:
        block.draw(screen)

    for block in background_blocks:
        block.draw(screen)

    pygame.display.update()
    clock.tick(60)
