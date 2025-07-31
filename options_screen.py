from button import Button
from cells import Cell
from paths import *
from slider import Slider

import pygame

pygame.init()


class OptionsScreen:
    def __init__(self, game):
        self.game = game
        self.screen = self.game.screen

        self.frame = []
        self.__create_frame()

        self.back_button = Button((290, 720), back_button_path, back_button_brighten_path,
                                  self.game.click_sound, 1)

        self.font = pygame.font.SysFont('Ariel', 36)
        self.w_up = self.font.render("W / UP ARROW - ROTATE",
                                     True, (255, 255, 255))

        self.s_down = self.font.render("S / DOWN ARROW - SPEED UP",
                                       True, (255, 255, 255))

        self.a_left = self.font.render("A / LEFT ARROW - MOVE LEFT",
                                       True, (255, 255, 255))

        self.d_right = self.font.render("D / RIGHT ARROW - MOVE RIGHT",
                                        True, (255, 255, 255))

        self.left_shift = self.font.render("LEFT SHIFT - FALL BLOCK",
                                           True, (255, 255, 255))

        self.music_text = self.font.render("MUSIC VOLUME:",
                                           True, (255, 255, 255))

        self.sfx_text = self.font.render("SFX VOLUME:",
                                         True, (255, 255, 255))

        self.music_slider = Slider(255, 400, 350, 30, 0.5, 0, 0.5)

        self.sfx_slider = Slider(255, 500, 350, 30, 0.5, 0, 2)

    def update_screen(self):
        self.back_button.click_left(self.game.go_StartScreen)

        self.music_slider.move_slider()
        self.game.music.set_volume(self.music_slider.get_value())

        self.sfx_slider.move_slider()
        self.game.click_sound.set_volume(self.sfx_slider.get_value())

    def handle_events(self, events):
        pass

    def draw_screen(self):
        self.screen.fill((0, 0, 0))
        self.back_button.draw(self.screen)

        for block in self.frame:
            block.draw(self.screen)

        self.screen.blit(self.w_up, (80, 80))
        self.screen.blit(self.s_down, (80, 130))
        self.screen.blit(self.a_left, (80, 180))
        self.screen.blit(self.d_right, (80, 230))
        self.screen.blit(self.left_shift, (80, 280))
        self.screen.blit(self.music_text, (80, 350))
        self.screen.blit(self.sfx_text, (80, 450))

        self.music_slider.slider_render(self.screen)
        self.sfx_slider.slider_render(self.screen)

    def __create_frame(self):
        for x in range(20):
            self.frame.append(Cell((40 * x, 0), "GRAY", 0.5))
            self.frame.append(Cell((40 * x, 840), "GRAY", 0.5))

        for y in range(1, 21):
            self.frame.append(Cell((0, y * 40), "GRAY", 0.5))
            self.frame.append(Cell((760, y * 40), "GRAY", 0.5))

    def __background_blocks(self):
        pass
