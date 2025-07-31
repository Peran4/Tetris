from sys import exit
from time import sleep

from game_screen import GameScreen
from start_screen import StartScreen
from options_screen import OptionsScreen
from paths import *

import pygame

pygame.init()


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((800, 880))
        self.screen.fill((0, 0, 0))

        pygame.display.set_caption("Tetris")

        self.clock = pygame.time.Clock()
        self.running = True

        self.click_sound = pygame.mixer.Sound(click_sound_path)
        self.click_sound.set_volume(1)

        self.music = pygame.mixer.Sound(music_path)
        self.music.set_volume(0.25)
        self.music.play(-1)

        self.current_screen = StartScreen(self)

    def run(self):
        while self.running:
            events = pygame.event.get()

            for event in events:
                if event.type == pygame.QUIT:
                    self.exit_game()

            self.current_screen.handle_events(events)
            self.current_screen.update_screen()
            self.current_screen.draw_screen()

            pygame.display.update()
            self.clock.tick(60)

    def exit_game(self):
        sleep(0.45)
        pygame.quit()
        exit()

    def go_GameScreen(self):
        self.current_screen = GameScreen(self)

    def go_OptionScreen(self):
        self.current_screen = OptionsScreen(self)

    def go_StartScreen(self):
        self.current_screen = StartScreen(self)


if __name__ == "__main__":
    Game().run()
