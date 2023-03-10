import pygame


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, color, size):
        super().__init__()

        self.image = pygame.Surface((size, size))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=pos)

