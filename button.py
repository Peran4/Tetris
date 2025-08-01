import pygame

pygame.init()


class Button:
    def __init__(self, pos: tuple, image_path, brighten_image_path, sound=None, scale=1):
        self.image = pygame.image.load(image_path)
        self.brighten_image = pygame.image.load(brighten_image_path)

        self.width = self.image.get_width()
        self.height = self.image.get_height()

        self.image = pygame.transform.scale(self.image, (int(self.width * scale), int(self.height * scale)))
        self.brighten_image = pygame.transform.scale(self.brighten_image, (int(self.width * scale),
                                                                           int(self.height * scale)))

        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        self.sound = sound

        self.can_click: bool = True
        self.can_display: bool = True
        self.clicked: bool = False

    def draw(self, screen):
        mouse_pos = pygame.mouse.get_pos()
        if self.can_display:
            if self.rect.collidepoint(mouse_pos) and self.can_click:
                screen.blit(self.brighten_image, (self.rect.x, self.rect.y))
            else:
                screen.blit(self.image, (self.rect.x, self.rect.y))

    def click_left(self, action):
        if self.can_click and self.can_display:
            mouse_pos = pygame.mouse.get_pos()

            if self.rect.collidepoint(mouse_pos) and pygame.mouse.get_pressed()[0] and not self.clicked:
                self.clicked = True

            if pygame.mouse.get_pressed()[0] == 0 and self.clicked:
                self.clicked = False
                if self.sound is not None:
                    self.sound.play()
                action()

    def change_display_flag(self, display: bool):
        self.can_display = display

    def change_action_flag(self, flag: bool):
        self.can_click = flag
