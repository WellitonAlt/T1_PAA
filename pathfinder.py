import pygame
import time


# Inicialização do pygame
pygame.init()

# Tamanho e nome da janela
tela = pygame.display.set_mode([400,400])
tela.fill((255, 255, 255))
pygame.display.set_caption("PathFinding")

img_verde = pygame.image.load('Imagens/Verde.jpg')
img_vermelha = pygame.image.load('Imagens/Vermelho.jpg')
img_preta = pygame.image.load('Imagens/Preto.jpg')
img_azul = pygame.image.load('Imagens/Azul.jpg')
img_branco = pygame.image.load('Imagens/Branco.jpg')

grid = [[0, 0, 0, 0, 0, 1],
        [1, 1, 0, 0, 0, 1],
        [0, 0, 0, 1, 0, 0],
        [0, 1, 1, 0, 0, 1],
        [0, 1, 0, 0, 1, 0],
        [0, 1, 0, 0, 0, 2]]


# A função search(x,y) faz a verficação da célula visitada;
def search(x,y):
    grid[x][y] = 3
    if grid[x][y] == 1:
        print("Parede em: %d,%d" % (x, y))
        return False
    elif grid[x][y] == 2:
        print("Encontrou célula final em: %d,%d" % (x, y))
        return True
    elif grid[x][y] == 3:
        print("Visitado em: %d,%d" % (x, y))
        return False

    print("Visitando %d,%d" % (x, y))
    printGrid(x,y)
    grid[x][y] = 3;
    pygame.time.wait(100)
    # Marcando como visitado

    # Explorando vizinhos em sentido horário começando pelo da direita
    if ((x < len(grid)-1 and search(x+1, y))
        or (y > 0 and search(x, y-1))
        or (x > 0 and search(x-1, y))
        or (y < len(grid)-1 and search(x, y+1))):
        return True

    return False


def printGridIni():
    for i in range(0, 6):
        for j in range(0, 6):
            if grid[i][j] == 0:
                tela.blit(img_branco, (i * 40, j * 40))
            elif grid[i][j] == 1:
                tela.blit(img_azul, (i * 40, j * 40))
            elif grid[i][j] == 2:
                tela.blit(img_vermelha, (i * 40, j * 40))
            elif grid[i][j] == 3:
                tela.blit(img_preta, (i * 40, j * 40))

    tela.blit(img_preta, (0,0))
    pygame.display.update()



def printGrid(i ,j):
    if grid[i][j] == 0:
        tela.blit(img_branco, (i * 40, j * 40))
    elif grid[i][j] == 1:
        tela.blit(img_azul, (i * 40, j * 40))
    elif grid[i][j] == 2:
        tela.blit(img_vermelha, (i * 40, j * 40))
    elif grid[i][j] == 3:
        tela.blit(img_preta, (i * 40, j * 40))
    pygame.display.update()



printGridIni()
search(0,0)



input("Tecle algo para sair")