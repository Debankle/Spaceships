import os
import math
import pygame


class SuperBullet(pygame.sprite.Sprite):
    def __init__(self, pos, target):
        super().__init__()

        self.pos = pygame.math.Vector2(pos)
        self.target = pygame.math.Vector2(target)
        relX, relY = pos[0] - target[0], pos[1] - target[1]
        self.vector = -pygame.math.Vector2(relX/math.sqrt(relX**2 + relY**2), relY/math.sqrt(relX**2 + relY**2))
        self.pos.x += 25 * self.vector[0]
        self.pos.y += 25 * self.vector[1]
        self.speed = 10
        
        rad_angle = math.atan2(relY, relX)
        deg_angle = -math.degrees(rad_angle) + 90

        self.image = pygame.image.load(os.path.join("assets", "Images", "Bullets", "bullet.png")).convert_alpha()

        self.image = pygame.transform.rotate(self.image, deg_angle)
        self.rect = self.image.get_rect(center=self.pos)

    def update(self):
        self.pos.x += self.speed * self.vector[0]
        self.pos.y += self.speed * self.vector[1]
        self.rect = self.image.get_rect(center=self.pos)

        