import pygame
from os import walk


def import_folder(path):
    pygame.init()

    surfaces = []

    for _, __, file_names in walk(path):
        for img in file_names:
            full_path = path + '/' + img
            image = pygame.image.load(full_path).convert_alpha()
            surfaces.append(image)

    return surfaces
