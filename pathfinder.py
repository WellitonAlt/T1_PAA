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

# Mapa inicial
grid = [[0, 0, 1, 1, 0, 0, 0, 1, 1, 1],
        [1, 0, 0, 0, 1, 1, 0, 0, 1, 1],
        [1, 1, 1, 0, 0, 1, 0, 1, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 0, 1, 1, 0, 0, 1, 0],
        [1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 0, 0, 1, 1, 1, 0, 1, 1],
        [1, 1, 0, 0, 1, 0, 0, 0, 1, 1],
        [1, 1, 0, 0, 0, 0, 1, 0, 0, 2]];

# Imprime o mapa inicial
def printGridIni():
    for i in range(0, 10):
        for j in range(0, 10):
            if grid[i][j] == 0: #Se vazio imprime branco
                pygame.draw.rect(tela, (255,255,255) ,(j*40,i*40,40,40)) 
            elif grid[i][j] == 1: #Se parede imprime azul
                pygame.draw.rect(tela, (0,0,255) ,(j*40,i*40,40,40))
            elif grid[i][j] == 2: #Se final imprime vermelho
                pygame.draw.rect(tela, (255,0,0) ,(j*40,i*40,40,40))
    #Inicio imprime preto
    pygame.draw.rect(tela, (0,0,0) ,(0,0,40,40))
    pygame.display.update()

# Atualiza as cores do grid
def atualizaGrid(i ,j):
    #imprime verde
    pygame.draw.rect(tela, (0,255,0) ,(j*40,i*40,40,40))
    pygame.display.flip()

<<<<<<< HEAD
# A função procura(i,j) faz a verficação da célula visitada;
def procura(i,j):
    if i > 9 or j > 9:
=======
# A função search(x,y) faz a verficação da célula visitada;
def search(x,y):
    grid[x][y] = 3
    if grid[x][y] == 1:
        print("Parede em: %d,%d" % (x, y))
>>>>>>> b5ed783dcf0558dbdf1df3414f47b44f25d0eff5
        return False
   
    if grid[i][j] == 1:        
        return False
<<<<<<< HEAD
    elif grid[i][j] == 2:       
        ctrl = True
        return True
        
    elif grid[i][j] == 3:
        return False       
      
    # Marcando como visitado e atualiza grid
    grid[i][j] = 3;
    atualizaGrid(i,j)
    pygame.time.delay(150)
=======

    print("Visitando %d,%d" % (x, y))
    printGrid(x,y)
    grid[x][y] = 3;
    pygame.time.wait(100)
    # Marcando como visitado
>>>>>>> b5ed783dcf0558dbdf1df3414f47b44f25d0eff5

    # Explorando vizinhos em sentido horário começando pelo da direita
    if ((i < len(grid)-1 and procura(i+1, j))
        or (i > 0 and procura(i-1, j))
        or (j > 0 and procura(i, j-1))
        or (j < len(grid)-1 and procura(i, j+1))):
        return True
       
    return False

<<<<<<< HEAD
printGridIni()
procura(0,0)
#Sai depois de 200 milisegundos
pygame.time.delay(150)
pygame.quit()

=======

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
>>>>>>> b5ed783dcf0558dbdf1df3414f47b44f25d0eff5
