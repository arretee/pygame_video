import pygame

from settings import *
from tile import Tile
from player import Player


class Level:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.get_surface()

        # Groups
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()

        self.setup()

    def setup(self):
        # Map
        for line_num, line_data in enumerate(map1):
            y = line_num * TILE_SIZE

            for row, value in enumerate(line_data):
                x = row * TILE_SIZE

                if value == 1:
                    tile = Tile((x, y), 'gray', TILE_SIZE)
                    self.tiles.add(tile)

        # Player
        player = Player((20, 50), (100, 100))
        self.player.add(player)

    def horizontal_collision(self):
        player = self.player.sprite

        player.rect.x += player.direction.x * player.speed

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player):
                if player.direction.x > 0:
                    player.rect.right = sprite.rect.left

                elif player.direction.x < 0:
                    player.rect.left = sprite.rect.right



    def vertical_collision(self):
        player = self.player.sprite

        player.rect.y += player.direction.y
        player.onGround = False

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.onGround = True
                    player.direction.y = 0

                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0



    def run(self):
        self.tiles.draw(self.screen)

        # Player
        self.player.update()

        self.horizontal_collision()
        self.vertical_collision()

        self.player.draw(self.screen)
