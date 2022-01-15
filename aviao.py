import pygame
import os


class Aviao:
    AVIAO = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'aviao.png')))
    VELOCIDADE = 20

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def moverEsq(self):
        self.x -= self.VELOCIDADE

    def moverDir(self):
        self.x += self.VELOCIDADE

    def desenhar(self, tela):
        tela.blit(self.AVIAO, (self.x, self.y))

    def get_mask(self):
        return pygame.mask.from_surface(self.AVIAO)
