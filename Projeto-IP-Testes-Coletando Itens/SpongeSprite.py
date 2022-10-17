import pygame
from pygame.locals import *


class Sponge(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('sprites/bob_1.png'))
        self.sprites.append(pygame.image.load('sprites/bob_2.png'))
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image, (40, 40))

        self.rect = self.image.get_rect()
        self.x_bob = 100
        self.y_bob = 100
        self.rect.topleft = self.x_bob,self.y_bob
        self.animar = False
    def posicao(self):
        self.animar = True
        if pygame.key.get_pressed()[K_a]:
            self.x_bob -= 3
            if self.x_bob <= 0:
                self.x_bob = 0
            self.rect.topleft = self.x_bob, self.y_bob
        if pygame.key.get_pressed()[K_d]:
            self.x_bob +=3
            if self.x_bob >= 600:
                self.x_bob = 600
            self.rect.topleft = self.x_bob,self.y_bob
        if pygame.key.get_pressed()[K_w]:
            self.y_bob -= 3
            if self.y_bob <= 0:
                self.y_bob = 0
            self.rect.topleft = self.x_bob,self.y_bob
        if pygame.key.get_pressed()[K_s]:
            self.y_bob += 3
            if self.y_bob >= 440:
                self.y_bob = 440
            self.rect.topleft = self.x_bob,self.y_bob
    def update(self):
        if self.animar == True:
            self.atual += 0.05
            if self.atual >= len(self.sprites):
                self.atual = 0
                self.animar = False
            self.image = self.sprites[int(self.atual)]
            self.image = pygame.transform.scale(self.image, (40, 40))