from button import Button
from paths import *
from block import Block
import pygame

pygame.init()


def create_text():
    TETRIS = []
    for x in range(5):
        TETRIS.append(Block((110 + 20 * x, 80), "BLUE", 0.25))
        TETRIS.append(Block((330 + 20 * x, 80), "PURPLE", 0.25))

    for x in range(7):
        TETRIS.append(Block((150, 80 + 20 * x), "BLUE", 0.25))
        TETRIS.append(Block((230, 80 + 20 * x), "RED", 0.25))
        TETRIS.append(Block((370, 80 + 20 * x), "PURPLE", 0.25))
        TETRIS.append(Block((450, 80 + 20 * x), "ORANGE", 0.25))
        TETRIS.append(Block((550, 80 + 20 * x), "CYAN", 0.25))

    for x in range(3):
        TETRIS.append(Block((250 + 20 * x, 80), "RED", 0.25))
        TETRIS.append(Block((250 + 20 * x, 140), "RED", 0.25))
        TETRIS.append(Block((250 + 20 * x, 200), "RED", 0.25))
        TETRIS.append(Block((470 + 20 * x, 160 + 20 * x), "ORANGE", 0.25))
        TETRIS.append(Block((610 + 20 * x, 80), "YELLOW", 0.25))
        TETRIS.append(Block((610 + 20 * x, 140), "YELLOW", 0.25))
        TETRIS.append(Block((610 + 20 * x, 200), "YELLOW", 0.25))

    for x in range(2):
        TETRIS.append(Block((470 + 20 * x, 80), "ORANGE", 0.25))
        TETRIS.append(Block((470 + 20 * x, 140), "ORANGE", 0.25))
        TETRIS.append(Block((510, 100 + 20 * x), "ORANGE", 0.25))
        TETRIS.append(Block((670, 160 + 20 * x), "YELLOW", 0.25))
        TETRIS.append(Block((590, 100 + 20 * x), "YELLOW", 0.25))

    TETRIS.append(Block((590, 180), "YELLOW", 0.25))
    TETRIS.append(Block((670, 100), "YELLOW", 0.25))

    return TETRIS


def crate_frame():
    frame = []

    for x in range(20):
        top_row = Block((40 * x, 0), "GRAY", 0.5)
        bottom_row = Block((40 * x, 840), "GRAY", 0.5)
        frame.append(top_row)
        frame.append(bottom_row)

    for y in range(1, 21):
        left_column = Block((0, y * 40), "GRAY", 0.5)
        right_column = Block((760, y * 40), "GRAY", 0.5)
        frame.append(left_column)
        frame.append(right_column)

    return frame


def get_click_sound():
    click_sound = pygame.mixer.Sound(click_sound_path)
    click_sound.set_volume(1)
    return click_sound


def create_buttons(sound, scale):
    play_button = Button((290, 400), play_button_path, play_button_brighten_path, sound, scale)
    options_button = Button((290, 500), options_button_path, options_button_brighten_path, sound, scale)
    exit_button = Button((290, 600), exit_button_path, exit_button_brighten_path, sound, scale)
    return play_button, options_button, exit_button
