import pygame

# Inicialização do pygame
pygame.init()

# Tamanho e nome da janela
tela = pygame.display.set_mode([400,400])
tela.fill((255, 255, 255))
pygame.display.set_caption("PathFinding")

matriz = ([[ 0,  1,  0,  1],
           [ 1,  0,  1,  0],
           [ 0,  1,  0,  1],
           [ 1,  0,  1,  0]])

quad = pygame.Surface((40, 40))
for i in range(0, 4):
    for j in range(0, 4):        
        if matriz[i][j] == 0:
            quad.fill((255, 0, 0))
        else:
            quad.fill((0, 255, 0))
        tela.blit(quad, (i*40, j*40))

        
pygame.display.update()
