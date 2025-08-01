import pygame
from enums import Color

pygame.init()


class Cell:
    def __init__(self, pos: tuple, color_name, scale=1):
        self.pos = pos
        self.paths = Color[color_name].value
        self.scale = scale

        self.image = pygame.image.load(self.paths[0])

        self.width = self.image.get_width()
        self.height = self.image.get_height()

        self.image = pygame.transform.scale(self.image, (int(self.width * self.scale),
                                                         int(self.height * self.scale)))

        self.rect = self.image.get_rect()
        self.rect.topleft = pos

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def update_pos(self, new_pos: tuple):
        self.pos = new_pos
        self.rect.topleft = self.pos

    def change_to_white(self):
        self.paths = Color["WHITE"].value

        self.image = pygame.image.load(self.paths[0])
        self.image = pygame.transform.scale(self.image, (int(self.width * self.scale),
                                                         int(self.height * self.scale)))


class ShadeCell:
    def __init__(self, pos: tuple, color_name, scale=1):
        self.pos = pos
        self.paths = Color[color_name].value

        self.shade_image = pygame.image.load(self.paths[1])

        width = self.shade_image.get_width()
        height = self.shade_image.get_height()

        self.shade_image = pygame.transform.scale(self.shade_image, (int(width * scale),
                                                                     int(height * scale)))

        self.shade_rect = self.shade_image.get_rect()
        self.shade_rect.topleft = pos

    def draw(self, screen):
        screen.blit(self.shade_image, (self.shade_rect.x, self.shade_rect.y))

    def update_pos(self, new_pos: tuple):
        self.pos = new_pos
        self.shade_rect.topleft = self.pos
