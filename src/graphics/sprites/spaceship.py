import math
import pygame


class Spaceship(pygame.sprite.Sprite):
    def __init__(self, pos, image):
        super().__init__()

        self.pos = pygame.math.Vector2(pos)

        self.image = image
        self.original_image = image
        self.rect = self.image.get_rect(center=self.pos)

    def update(self):
        self.rotate()
        self.rect = self.image.get_rect(center=self.pos)

    def rotate(self):
        mouse_pos = pygame.mouse.get_pos()
        relX, relY = mouse_pos[0] - self.pos[0], mouse_pos[1] - self.pos[1]
        rad_angle = -math.atan2(relY, relX)
        deg_angle = math.degrees(rad_angle) - 90
        self.image = pygame.transform.rotate(self.original_image, deg_angle)

    def move(self, xMod, yMod):
        self.pos.x += xMod
        self.pos.y += yMod