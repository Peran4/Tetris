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

        self.back_button = Button((540, 720), back_button_path, back_button_brighten_path,
                                  self.game.click_sound, 0.75)

        self.frame = []
        self.game_frame()
        self.next_block = None
        self.get_next_block()

        self.current_block = None

        self.start_flag = False
        self.pause_flag = False

        self.start_time = pygame.time.get_ticks()
        self.current_time = 0

    def update_screen(self):
        self.back_button.click_left(self.game.click_back)

        if self.pause_flag or not self.start_flag:
            return

        if self.current_block is None:
            self.current_block = self.next_block
            self.current_block.change_pos((200, 40))
            self.get_next_block()

        self.current_time = pygame.time.get_ticks()
        if self.current_time - self.start_time >= 1000:
            # self.current_block.move_down()
            self.start_time = self.current_time

    def draw_screen(self):
        self.screen.fill((0, 0, 0))

        self.back_button.draw(self.screen)
        for block in self.frame:
            block.draw(self.screen)

        self.next_block.draw_block(self.screen)

        if not self.start_flag:
            self.screen.blit(self.start_text, (54, 400))

        if self.current_block is not None:
            self.current_block.draw_block(self.screen)

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if not self.start_flag:
                    self.start_flag = True
                    return

                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    self.current_block.move_left()
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    self.current_block.move_right()
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    self.current_block.rotate(1)
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    pass
                if event.key == pygame.K_LSHIFT:
                    pass
                if event.key == pygame.K_p:
                    self.pause_flag = not self.pause_flag

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
        if shape == "I":
            self.next_block = Block((600, 160), shape, 0.5)
        else:
            self.next_block = Block((600, 120), shape, 0.5)

    def restore(self):
        self.start_flag = False
