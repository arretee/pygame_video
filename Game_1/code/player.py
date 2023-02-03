import pygame

from settings import *
from support import import_folder


class Player(pygame.sprite.Sprite):
    def __init__(self, size, pos):
        super().__init__()

        self.screen = pygame.display.get_surface()

        # setup animations
        self.frame_index = 0
        self.animation_speed = 0.15
        self.animation = 'idle_right'
        self.import_animations()

        # Status
        self.status = 'idle'
        self.facing = 'right'


        # Movement
        self.speed = 4
        self.jump_speed = 16
        self.direction = pygame.Vector2()
        self.onGround = False

        # General setup
        self.image = self.animations[self.animation][self.frame_index]
        self.rect = self.image.get_rect(topleft=pos)

    def get_status(self):
        if self.direction.y < 0:
            self.status = 'jump'
        elif self.direction.y > 1:
            self.status = 'fall'
        else:
            if self.direction.x != 0:
                self.status = 'run'
            else:
                self.status = 'idle'


        print(self.status)

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_d]:
            self.direction.x = 1
            self.facing = 'right'
        elif keys[pygame.K_a]:
            self.direction.x = -1
            self.facing = 'left'
        else:
            self.direction.x = 0

        if keys[pygame.K_SPACE]:
            self.jump()

    def import_animations(self):
        self.animations = {
            'fall_left': [], 'fall_right': [], 'idle_left': [], 'idle_right': [],
            'jump_left': [], 'jump_right': [], 'run_left': [], 'run_right': []
        }

        # Load animations
        for key in self.animations.keys():
            path = '../graphics/player/' + key
            self.animations[key] = import_folder(path)

    def animate(self):
        animation = self.animations[self.status + '_' + self.facing]

        # loop over frame index
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0

        self.image = animation[int(self.frame_index)]

    def gravity_update(self):
        self.direction.y += PLAYER_GRAVITY

    def jump(self):
        if self.onGround:
            self.direction.y = -self.jump_speed

    def update(self):
        self.input()

        self.get_status()
        self.gravity_update()

        self.animate()
