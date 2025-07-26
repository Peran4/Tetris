from sys import exit
from time import sleep
from block import Block
import pygame

from start_screen import StartScreen

pygame.init()


def click_play():
    print("aa")


def click_options():
    pass


def exit_game():
    sleep(0.45)
    pygame.quit()
    exit()


screen = pygame.display.set_mode((800, 880))
screen.fill((0, 0, 0))
pygame.display.set_caption("Tetris")
clock = pygame.time.Clock()

main_menu = StartScreen(screen, 1)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game()

    main_menu.start_screen(click_play, click_options, exit_game)

    pygame.display.update()
    clock.tick(60)
