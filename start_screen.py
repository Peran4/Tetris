from button import Button
from paths import *
from cell import Cell
from block import Block
import pygame

pygame.init()


class StartScreen:
    def __init__(self, game):
        self.game = game
        self.screen = self.game.screen

        self.play_button = None
        self.options_button = None
        self.exit_button = None
        self.TETRIS = []
        self.frame = []
        self.bg_blocks = []

        self.click_sound = pygame.mixer.Sound(click_sound_path)
        self.click_sound.set_volume(1)

        self.create_buttons()
        self.create_frame()
        self.create_text()
        self.create_bg_blocks()

    def update_screen(self):
        self.screen.fill((0, 0, 0))

        self.play_button.draw(self.screen)

        self.play_button.click_left(self.game.click_play)

        self.options_button.draw(self.screen)
        self.options_button.click_left(self.game.click_options)

        self.exit_button.draw(self.screen)
        self.exit_button.click_left(self.game.exit_game)

        for block in self.frame:
            block.draw(self.screen)

        for block in self.TETRIS:
            block.draw(self.screen)

        for block in self.bg_blocks:
            block.draw(self.screen)

    def handle_events(self, events):
        pass

    def create_text(self):
        for x in range(5):
            self.TETRIS.append(Cell((110 + 20 * x, 80), "BLUE", 0.25))
            self.TETRIS.append(Cell((330 + 20 * x, 80), "PURPLE", 0.25))

        for x in range(7):
            self.TETRIS.append(Cell((150, 80 + 20 * x), "BLUE", 0.25))
            self.TETRIS.append(Cell((230, 80 + 20 * x), "RED", 0.25))
            self.TETRIS.append(Cell((370, 80 + 20 * x), "PURPLE", 0.25))
            self.TETRIS.append(Cell((450, 80 + 20 * x), "ORANGE", 0.25))
            self.TETRIS.append(Cell((550, 80 + 20 * x), "CYAN", 0.25))

        for x in range(3):
            self.TETRIS.append(Cell((250 + 20 * x, 80), "RED", 0.25))
            self.TETRIS.append(Cell((250 + 20 * x, 140), "RED", 0.25))
            self.TETRIS.append(Cell((250 + 20 * x, 200), "RED", 0.25))
            self.TETRIS.append(Cell((470 + 20 * x, 160 + 20 * x), "ORANGE", 0.25))
            self.TETRIS.append(Cell((610 + 20 * x, 80), "YELLOW", 0.25))
            self.TETRIS.append(Cell((610 + 20 * x, 140), "YELLOW", 0.25))
            self.TETRIS.append(Cell((610 + 20 * x, 200), "YELLOW", 0.25))

        for x in range(2):
            self.TETRIS.append(Cell((470 + 20 * x, 80), "ORANGE", 0.25))
            self.TETRIS.append(Cell((470 + 20 * x, 140), "ORANGE", 0.25))
            self.TETRIS.append(Cell((510, 100 + 20 * x), "ORANGE", 0.25))
            self.TETRIS.append(Cell((670, 160 + 20 * x), "YELLOW", 0.25))
            self.TETRIS.append(Cell((590, 100 + 20 * x), "YELLOW", 0.25))

        self.TETRIS.append(Cell((590, 180), "YELLOW", 0.25))
        self.TETRIS.append(Cell((670, 100), "YELLOW", 0.25))

    def create_frame(self):
        for x in range(20):
            self.frame.append(Cell((40 * x, 0), "GRAY", 0.5))
            self.frame.append(Cell((40 * x, 840), "GRAY", 0.5))

        for y in range(1, 21):
            self.frame.append(Cell((0, y * 40), "GRAY", 0.5))
            self.frame.append(Cell((760, y * 40), "GRAY", 0.5))

    def create_bg_blocks(self):
        self.bg_blocks.extend(Block((80, 800), "T", 0.5, 2).shatter())
        self.bg_blocks.extend(Block((80, 720), "Z", 0.5, 1).shatter())

    def create_buttons(self):
        self.play_button = Button((290, 400), play_button_path, play_button_brighten_path,
                                  self.click_sound)
        self.options_button = Button((290, 500), options_button_path, options_button_brighten_path,
                                     self.click_sound)
        self.exit_button = Button((290, 600), exit_button_path, exit_button_brighten_path,
                                  self.click_sound)


