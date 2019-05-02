import os
import sys
import glob
import time
import math
import pygame
import socket
import threading

from graphics.gui import Button, Label, Colors
from graphics.sprites import Spaceship, Bullet, SuperBullet


def bounceDown(x):
    y = math.exp(-x/1.287)*math.sin(x)
    return y


class Game(object):
    def __init__(self):

        pygame.init()
        self.width = 1152
        self.height = 720
        self.display = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Spaceships!")
        self.clock = pygame.time.Clock()

        self.spaceshipSprites = pygame.sprite.Group()
        self.bulletSprites = pygame.sprite.Group()
        self.allSprites = pygame.sprite.Group()

    def mainMenu(self):
        running = True

        w, h = pygame.display.get_surface().get_size()

        title = Label(w/2, 50, text="Spaceships",
                      fgColor=Colors.title, fontSize=60)
        settingsBtn = Button(w/3, 500, 250, 75, text="Settings", bgColor=Colors.btnBg1,
                             fgColor=Colors.btnFg1, hoverBg=Colors.btnBg2, hoverFg=Colors.btnFg2)
        playBtn = Button(w/3*2, 500, 250, 75, text="Play", bgColor=Colors.btnBg1,
                         fgColor=Colors.btnFg1, hoverBg=Colors.btnBg2, hoverFg=Colors.btnFg2)

        while running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        running = False

            self.display.fill((255, 255, 255))

            title.draw(self.display)
            settingsBtn.draw(self.display)
            playBtn.draw(self.display)

            if settingsBtn.buttonClicked:
                del title
                del settingsBtn
                del playBtn
                running = False
                self.settings()

            if playBtn.buttonClicked:
                del title
                del settingsBtn
                del playBtn
                running = False
                self.gameMode()

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()
        sys.exit()

    def settings(self):
        running = True

        w, h = pygame.display.get_surface().get_size()

        back = Button(w/2, w/2, 400, 120, text="Back", bgColor=Colors.btnBg1,
                      fgColor=Colors.btnFg1, hoverBg=Colors.btnBg2, hoverFg=Colors.btnFg2, fontSize=60)

        while running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        running = False

            self.display.fill((255, 255, 255))

            back.draw(self.display)

            if back.buttonClicked:
                del back
                running = False
                self.mainMenu()

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()
        sys.exit()

    def gameMode(self):
        running = True

        w, h = pygame.display.get_surface().get_size()

        vsAIbtn = Button(w/4, 500, 250, 75, text="vs AI", bgColor=Colors.btnBg1,
                         fgColor=Colors.btnFg1, hoverBg=Colors.btnBg2, hoverFg=Colors.btnFg2)
        multiplayerBtn = Button(w/4*3, 500, 250, 75, text="Multiplayer", bgColor=Colors.btnBg1,
                                fgColor=Colors.btnFg1, hoverBg=Colors.btnBg2, hoverFg=Colors.btnFg2)
        hostBtn = Button(w/4, -75/2, 250, 75, text="Host", bgColor=Colors.btnBg1,
                         fgColor=Colors.btnFg1, hoverBg=Colors.btnBg2, hoverFg=Colors.btnFg2)
        joinBtn = Button(w/4*3, -75/2, 250, 75, text="Join", bgColor=Colors.btnBg1,
                         fgColor=Colors.btnFg1, hoverBg=Colors.btnBg2, hoverFg=Colors.btnFg2)

        backBtn = Button(w/4*2, 500, 250, 75, text="Back", bgColor=Colors.btnBg1,
                         fgColor=Colors.btnFg1, hoverBg=Colors.btnBg2, hoverFg=Colors.btnFg2)

        animate = False
        animateX = -5.5
        animateMod = 0

        while running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        running = False

            self.display.fill((255, 255, 255))

            if animate:
                animateX += 0.1
                animateMod = bounceDown(animateX)

                if animateMod < 0.05 and animateMod > 0:
                    animate = False

            vsAIbtn.move(0, animateMod)
            multiplayerBtn.move(0, animateMod)
            hostBtn.move(0, animateMod)
            joinBtn.move(0, animateMod)

            vsAIbtn.draw(self.display)
            multiplayerBtn.draw(self.display)
            hostBtn.draw(self.display)
            joinBtn.draw(self.display)

            backBtn.draw(self.display)

            if multiplayerBtn.buttonClicked:
                animate = True

            if backBtn.buttonClicked:
                del vsAIbtn
                del multiplayerBtn
                del hostBtn
                del joinBtn
                del backBtn
                running = False
                self.mainMenu()

            if vsAIbtn.buttonClicked:
                del vsAIbtn
                del multiplayerBtn
                del hostBtn
                del joinBtn
                del backBtn
                running = False
                self.vsAI()

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()
        sys.exit()

    def vsAI(self):
        running = True

        godImg = pygame.image.load(os.path.join(
            "assets", "Images", "god.jpg")).convert_alpha()
        godImg = pygame.transform.scale(godImg, (self.width, self.height))

        while running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        running = False

            self.display.fill((255, 255, 255))

            self.display.blit(godImg, (0, 0))

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()
        sys.exit()
