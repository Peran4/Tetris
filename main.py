from sys import exit
from time import sleep
from start_screen import StartScreen
from enums import GameState

import pygame

pygame.init()


def click_play():
    global game_state
    game_state = GameState.GAME


def click_options():
    print(game_state.value)


def exit_game():
    sleep(0.45)
    pygame.quit()
    exit()


screen = pygame.display.set_mode((800, 880))
screen.fill((0, 0, 0))
pygame.display.set_caption("Tetris")
clock = pygame.time.Clock()

main_menu = StartScreen(screen, 1)
game_state = GameState.MAIN_MENU

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game()

    main_menu.start_screen(click_play, click_options, exit_game)

    pygame.display.update()
    clock.tick(60)
