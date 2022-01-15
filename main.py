import pygame
import os
import random
from aviao import Aviao
from nuvem import Nuvem

TELA_LARGURA = 500
TELA_ALTURA = 700
IMAGEM_BACKGROUND = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bg.png')))

pygame.font.init()
FONTE_PONTOS = pygame.font.SysFont('arial', 50)


def desenhar_tela(tela, avioes, nuvens, pontos):
    tela.blit(IMAGEM_BACKGROUND, (0, 0))
    for aviao in avioes:
        aviao.desenhar(tela)
    for nuvem in nuvens:
        nuvem.desenhar(tela)

    texto = FONTE_PONTOS.render(f"Pontuação: {pontos}", 1, (255, 255, 255))
    tela.blit(texto, (TELA_LARGURA - 10 - texto.get_width(), 10))

    pygame.display.update()


def main():
    planes = [Aviao(round((TELA_LARGURA - 60) / 2), round(TELA_ALTURA / 1.5))]
    tela = pygame.display.set_mode((TELA_LARGURA, TELA_ALTURA))
    pontos = 0
    velocidadeNuvem = 5
    nuvens = [Nuvem(10, 0, velocidadeNuvem)]
    relogio = pygame.time.Clock()

    rodando = True
    while rodando:
        relogio.tick(30)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
                pygame.quit()
                quit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    for plane in planes:
                        plane.moverEsq()
                if evento.key == pygame.K_RIGHT:
                    for plane in planes:
                        plane.moverDir()

        adicionar_nuvem = False
        remove_nuvem = []
        for nuvem in nuvens:
            for i, plane in enumerate(planes):
                if nuvem.colidir(plane):
                    planes.pop(i)
                    rodando = False
                if not nuvem.passou and plane.y < nuvem.y:
                    nuvem.passou = True
                    adicionar_nuvem = True
                    velocidadeNuvem += 1
            nuvem.mover()
            if nuvem.x + nuvem.NUVEM[nuvem.tamanho].get_width() < 20:
                remove_nuvem.append(nuvem)

        if adicionar_nuvem:
            pontos += 1
            tamanho = random.randint(0, 1)
            pos = random.randrange(0, TELA_LARGURA - nuvem.NUVEM[1].get_width())
            if velocidadeNuvem > 20:
                velocidadeNuvem = 20
            nuvens.append(Nuvem(pos, tamanho, velocidadeNuvem))
        for nuvem in remove_nuvem:
            nuvens.remove(nuvem)

        desenhar_tela(tela, planes, nuvens, pontos)


if __name__ == '__main__':
    main()