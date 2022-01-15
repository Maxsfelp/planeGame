import pygame
import os


class Nuvem:
    NUVEM = [
        pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'cloud.png'))),
        pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'cloudBig.png')))
    ]

    def __init__(self, x, tamanho, velocidade):
        self.x = x
        self.y = 0
        self.tamanho = tamanho
        self.passou = False
        self.velocidade = velocidade

    def mover(self):
        self.y += self.velocidade

    def desenhar(self, tela):
        tela.blit(self.NUVEM[self.tamanho], (self.x, self.y))

    def colidir(self, aviao):
        aviao_mask = aviao.get_mask()
        nuvem_mask = pygame.mask.from_surface(self.NUVEM[self.tamanho])

        distancia = (self.x - aviao.x, self.y - round(aviao.y))

        toque = aviao_mask.overlap(nuvem_mask, distancia)

        if toque:
            return True
        else:
            return False
