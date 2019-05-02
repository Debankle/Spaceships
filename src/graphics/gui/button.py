import os
import math
import time
import pygame
import threading
from pygame.locals import *

pygame.font.init()


class Button(object):
    def __init__(self, x, y, width, height, text="", bgColor=(0, 0, 0), fgColor=(255, 255, 255), **kwargs):

        self._x = x
        self._y = y
        self._width = width
        self._height = height

        self._text = text
        self._bgColor = bgColor
        self._fgColor = fgColor

        self._fontSize = kwargs.get("fontSize", 30)
        self._fontName = kwargs.get("fontName", "Times New Roman.ttf")
        self._hoverBg = kwargs.get("hoverBg", (255, 255, 255))
        self._hoverFg = kwargs.get("hoverFg", (0, 0, 0))
        self._hidden = kwargs.get("hidden", False)

        self._buttonClicked = False

        self._fontPath = os.path.join("assets", "Fonts", self._fontName)
        self._font = pygame.font.Font(self._fontPath, self._fontSize)

    def _update(self):
        self._rect = pygame.Rect(self._x - self._width/2, self._y - self._height/2, self._width, self._height)
        
        self._buttonSurface = pygame.Surface((self._rect.width, self._rect.height))
        self._buttonSurfaceRect = self._rect
        self._buttonSurface.fill(self._bgColor)

        self._label = self._font.render(self._text, 1, self._fgColor)
        self._labelRect = self._label.get_rect()
        self._labelRect.centerx = self._buttonSurfaceRect.width/2
        self._labelRect.centery = self._buttonSurfaceRect.height/2

        if self._buttonSurfaceRect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                self._buttonClicked = True
            self._buttonSurface.fill(self._hoverBg)
            self._label = self._font.render(self._text, 1, self._hoverFg)
        else:
            self._buttonSurface.fill(self._bgColor)
            self._label = self._font.render(self._text, 1, self._fgColor)

    def move(self, xMod, yMod):
        self._x += xMod
        self._y += yMod

    def draw(self, display):
        if not self._hidden:
            self._update()

            self._buttonSurface.blit(self._label, self._labelRect)
            display.blit(self._buttonSurface, self._buttonSurfaceRect)


    def buttonClicked(self):
        return self._buttonClicked

    def xPos(self):
        return self._x

    def yPos(self):
        return self._y

    buttonClicked = property(fget=buttonClicked)
    x = property(fget=xPos)
    y = property(fget=yPos)