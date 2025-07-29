from button import Button
from paths import *
from cells import Cell
from block import Block
from random import choice
from enums import Shapes
from math import cos, sin, pi
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

        self.frame_cells = []
        self.__create_game_frame()
        self.next_block = None
        self.__get_next_block()

        self.current_block = None
        self.locked_cells = []

        self.start_flag = False
        self.pause_flag = False
        self.press_down = False
        self.can_move_down_flag = False
        self.shade_stopped = False

        self.start_time = 0
        self.current_time = 0

    def update_screen(self):
        self.back_button.click_left(self.game.click_back)

        if self.pause_flag or not self.start_flag:
            return

        if self.current_block is None:
            self.current_block = self.next_block
            new_pos = (200, 40)
            if self.next_block.color == "YELLOW" or self.next_block.color == "CYAN":
                new_pos = (200, 80)

            self.current_block.change_pos_center(new_pos)
            self.__get_next_block()
            self.start_time = pygame.time.get_ticks()

        self.throw_shade()

        self.current_time = pygame.time.get_ticks()
        if self.current_time - self.start_time >= 500:
            self.__move_block_down()
            self.start_time = self.current_time

    def draw_screen(self):
        self.screen.fill((0, 0, 0))

        self.back_button.draw(self.screen)
        for block in self.frame_cells:
            block.draw(self.screen)
        for block in self.locked_cells:
            block.draw(self.screen)

        self.next_block.draw_block(self.screen)

        if not self.start_flag:
            self.screen.blit(self.start_text, (54, 400))

        if self.current_block is not None:
            if self.shade_stopped:
                self.current_block.draw_shade(self.screen)
            self.current_block.draw_block(self.screen)

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if not self.start_flag:
                    self.start_flag = True
                    return

                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    self.__move_block_left()
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    self.__move_block_right()
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    self.__rotate_block()
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    pass
                if event.key == pygame.K_LSHIFT:
                    pass
                if event.key == pygame.K_p:
                    self.pause_flag = not self.pause_flag

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    pass

    def __create_game_frame(self):
        for x in range(20):
            self.frame_cells.append(Cell((40 * x, 0), "GRAY", 0.5))
            self.frame_cells.append(Cell((40 * x, 840), "GRAY", 0.5))

        for y in range(1, 21):
            self.frame_cells.append(Cell((0, y * 40), "GRAY", 0.5))
            self.frame_cells.append(Cell((440, y * 40), "GRAY", 0.5))
            self.frame_cells.append(Cell((760, y * 40), "GRAY", 0.5))

    def __get_next_block(self):
        shape = choice(list(Shapes)).name
        if shape == "I":
            self.next_block = Block((600, 160), shape, 0.5)
        else:
            self.next_block = Block((600, 120), shape, 0.5)

    def __move_block_down(self):
        new_positions = []
        for cell in self.current_block.cells:
            new_positions.append((cell.pos[0], cell.pos[1] + 40))

        all_locked_blocks = []
        all_locked_blocks.extend(self.frame_cells)
        all_locked_blocks.extend(self.locked_cells)

        for block in all_locked_blocks:
            for cell in new_positions:
                if cell == block.pos:
                    if not self.can_move_down_flag:
                        self.__shatter_block()
                    else:
                        self.can_move_down_flag = False
                    return

        self.can_move_down_flag = True
        self.current_block.change_all_pos(new_positions)

    def __move_block_left(self):
        new_positions = []
        for cell in self.current_block.cells:
            new_positions.append((cell.pos[0] - 40, cell.pos[1]))

        if self.__check_overlap(new_positions):
            return

        self.current_block.change_all_pos(new_positions)
        self.current_block.change_shade_pos(new_positions)

    def __move_block_right(self):
        new_positions = []
        for cell in self.current_block.cells:
            new_positions.append((cell.pos[0] + 40, cell.pos[1]))

        if self.__check_overlap(new_positions):
            return

        self.current_block.change_all_pos(new_positions)
        self.current_block.change_shade_pos(new_positions)

    def __rotate_block(self):
        new_positions = []

        beta = pi / 2
        center_pos = self.current_block.center_pos
        for cell in self.current_block.cells:
            x = cell.pos[0] - center_pos[0]
            y = cell.pos[1] - center_pos[1]

            new_x = round(x * cos(beta) - y * sin(beta))
            new_y = round(x * sin(beta) + y * cos(beta))

            new_x += center_pos[0]
            new_y += center_pos[1]

            new_positions.append((new_x, new_y))

        if self.__check_overlap(new_positions):
            return

        self.current_block.change_all_pos(new_positions)
        self.current_block.change_shade_pos(new_positions)

    def __check_overlap(self, cells_pos):
        all_locked_cells = []
        all_locked_cells.extend(self.frame_cells)
        all_locked_cells.extend(self.locked_cells)

        for locked_cell in all_locked_cells:
            for cell_pos in cells_pos:
                if cell_pos == locked_cell.pos:
                    return True
        return False

    def throw_shade(self):
        for x in range(5):
            new_positions = []
            self.shade_stopped = False
            for cell in self.current_block.shade_cells:
                new_positions.append((cell.pos[0], cell.pos[1] + 40))

            if self.__check_overlap(new_positions):
                self.shade_stopped = True
                return

            self.current_block.change_shade_pos(new_positions)

    def __fall_block(self):
        pass

    def __shatter_block(self):
        self.locked_cells.extend(self.current_block.cells)
        self.current_block = None

    def __destroy_line(self):
        pass
