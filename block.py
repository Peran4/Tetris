import pygame
from block_colors import Color

pygame.init()


class Block:
    def __init__(self, pos: tuple, color_name, scale=1):
        self.pos = pos
        self.path = Color[color_name].value
        self.scale = scale

        self.image = pygame.image.load(self.path)

        self.width = self.image.get_width()
        self.height = self.image.get_height()
        # print(f"width: {self.width}\nheight: {self.height}")

        self.image = pygame.transform.scale(self.image, (int(self.width * self.scale),
                                                         int(self.height * self.scale)))

        self.rect = self.image.get_rect()
        self.rect.topleft = pos

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def change_to_white(self):
        self.path = Color["WHITE"].value

        self.image = pygame.image.load(self.path)
        self.image = pygame.transform.scale(self.image, (int(self.width * self.scale),
                                                         int(self.height * self.scale)))

    def move_down(self):
        pass