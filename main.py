from sys import exit
from time import sleep

from game_screen import GameScreen
from start_screen import StartScreen

import pygame

pygame.init()


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((800, 880))
        self.screen.fill((0, 0, 0))

        pygame.display.set_caption("Tetris")

        self.clock = pygame.time.Clock()
        self.running = True

        self.current_screen = StartScreen(self)

    def run(self):
        while self.running:
            events = pygame.event.get()

            for event in events:
                if event.type == pygame.QUIT:
                    self.exit_game()

            self.current_screen.handle_events(events)
            self.current_screen.update_screen()

            pygame.display.update()
            self.clock.tick(60)

    def exit_game(self):
        sleep(0.45)
        pygame.quit()
        exit()

    def click_play(self):
        self.current_screen = GameScreen(self)

    def click_options(self):
        pass

    def click_back(self):
        self.current_screen = StartScreen(self)


if __name__ == "__main__":
    Game().run()

# game_state = GameState.MAIN_MENU
#
# main_menu = StartScreen()
# tgame = GameScreen(screen)
#
# run = True
# while run:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             exit_game()
#
#     if game_state == GameState.MAIN_MENU:
#         main_menu.update_screen(click_play, click_options, exit_game)
#     elif game_state == GameState.OPTIONS:
#         pass
#     elif game_state == GameState.GAME:
#         tgame.upadate_screen(click_back)
#
#     pygame.display.update()
#     clock.tick(60)
