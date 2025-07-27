import pygame
from enums import Color

pygame.init()


class Cell:
    def __init__(self, pos: tuple, color_name, scale=1):
        self.pos = pos
        self.path = Color[color_name].value
        self.scale = scale

        self.image = pygame.image.load(self.path)

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
        self.path = Color["WHITE"].value

        self.image = pygame.image.load(self.path)
        self.image = pygame.transform.scale(self.image, (int(self.width * self.scale),
                                                         int(self.height * self.scale)))

    def move_down(self):
        self.update_pos((self.pos[0], self.pos[1] - int(80 * self.scale)))
