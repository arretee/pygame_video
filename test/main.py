import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

surf = pygame.image.load('ship.png')
rect = surf.get_rect(topleft=(100, 100))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        rect.x -= 10
    if keys[pygame.K_RIGHT]:
        rect.x += 10

    if keys[pygame.K_UP]:
        rect.y -= 10
    if keys[pygame.K_DOWN]:
        rect.y += 10



    pygame.display.update()

    screen.fill('black')

    screen.blit(surf, rect)
    pygame.draw.line(screen, 'red', (0, 0), (1280, 720), 10)
    pygame.draw.circle(screen, 'red', (600, 300), 100, 10)

    clock.tick(30)
