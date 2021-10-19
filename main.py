import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font(None, 50)

sky_surface = pygame.image.load('graphics/Sky.png')
ground_surface = pygame.image.load('graphics/ground.png')
text_surface = test_font.render('My Game', False, 'Red')

snail_surface = pygame.image.load('graphics/snail/snail1.png')


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.QUIT()
            exit()
    screen.blit(ground_surface, (0, 300))
    screen.blit(sky_surface, (0, 0))
    screen.blit(text_surface, (300, 50))
    screen.blit(snail_surface, (600, 250))

    pygame.display.update()
    clock.tick(60)
