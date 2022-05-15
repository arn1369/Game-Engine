import pygame
import math


class Ball(pygame.sprite.Sprite):
    def __init__(self,
                 screen: 'Surface',
                 pos: tuple,
                 radius: float,
                 color: tuple,
                 speed: float):
        self.x, self.y = pos[0], pos[1]
        self.img = pygame.draw.circle(screen, color, pos, radius)
        self.rect = self.img.get_rect()
