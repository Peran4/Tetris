from button import Button
from paths import *
from cell import Cell
from block import Block
from random import choice
from enums import Shapes
import pygame

pygame.init()


class GameScreen:
    def __init__(self, game):

        self.game = game
        self.screen = self.game.screen

        self.font = pygame.font.SysFont('Ariel', 36)

        self.start_text = self.font.render("To start game press any button",
                                           True, (255, 255, 255))

        self.click_sound = pygame.mixer.Sound(click_sound_path)
        self.click_sound.set_volume(1)

        self.back_button = Button((540, 720), back_button_path, back_button_brighten_path,
                                  self.click_sound, 0.75)

        self.frame = []
        self.game_frame()
        self.next_block = None
        self.get_next_block()

        self.current_block = None

        self.game_start = False
        self.game_pause = False

    def update_screen(self):
        self.screen.fill((0, 0, 0))

        self.back_button.draw(self.screen)
        self.back_button.click_left(self.game.click_back)

        for block in self.frame:
            block.draw(self.screen)

        self.next_block.draw_block(self.screen)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                print("a")
                if not self.game_start:
                    self.game_start = True
                    return

        # key = pygame.key.get_pressed()

        if not self.game_start:
            self.screen.blit(self.start_text, (54, 200))

        # if any(key) and not self.game_start:
        #     self.game_start = True
        #     return

        if self.game_pause:
            print("n")
            return

        if self.current_block is None:
            self.current_block = self.next_block
            self.get_next_block()

    def handle_events(self, events):
        pass

    def game_frame(self):
        for x in range(20):
            self.frame.append(Cell((40 * x, 0), "GRAY", 0.5))
            self.frame.append(Cell((40 * x, 840), "GRAY", 0.5))

        for y in range(1, 21):
            self.frame.append(Cell((0, y * 40), "GRAY", 0.5))
            self.frame.append(Cell((440, y * 40), "GRAY", 0.5))
            self.frame.append(Cell((760, y * 40), "GRAY", 0.5))

    def get_next_block(self):
        shape = choice(list(Shapes)).name
        print(shape)
        if shape == "I":
            self.next_block = Block((600, 160), shape, 0.5)
        else:
            self.next_block = Block((600, 120), shape, 0.5)

    def restore(self):
        self.game_start = False
