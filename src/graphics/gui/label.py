import os
import math
import pygame
from pygame.locals import *

pygame.font.init()


class Label(object):
    def __init__(self, x, y, text=None, fgColor=None, fontName=None, fontSize=None):

        self._x = x
        self._y = y

        if fontSize == None:
            self._fontSize = 30
        else:
            self._fontSize = fontSize

        if fontName == None:
            self._fontName = "Times New Roman.ttf"
        else:
            self._fontName = fontName

        if text == None:
            self._text = ""
        else:
            self._text = text

        if fgColor == None:
            self._fgColor = (0, 0, 0)
        else:
            self._fgColor = fgColor

        self._fontPath = os.path.join("assets", "Fonts", self._fontName)

        self._update()

    def _update(self):
        self._font = pygame.font.Font(self._fontPath, self._fontSize)
        self._label = self._font.render(self._text, 1, self._fgColor)
        self._rect = self._label.get_rect(center=(self._x, self._y))

    def draw(self, display):
        self._update()
        display.blit(self._label, self._rect)
