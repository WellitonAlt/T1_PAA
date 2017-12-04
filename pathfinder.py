import pygame
import heapq
# Inicialização do pygame
pygame.init()

# Tamanho e nome da janela
tela = pygame.display.set_mode([400,400])
tela.fill((255, 255, 255))
pygame.display.set_caption("PathFinding Profundidade")


img_verde = pygame.image.load('Imagens/Verde.jpg')
img_vermelha = pygame.image.load('Imagens/Vermelho.jpg')
img_preta = pygame.image.load('Imagens/Preto.jpg')
img_azul = pygame.image.load('Imagens/Azul.jpg')
img_branco = pygame.image.load('Imagens/Branco.jpg')

class Pilha(object):
    def __init__(self):
        self.dados = []
 
    def empilha(self, elemento): 
    def desempilha(self):
        
# Mapa inicial
grid = [[0, 0, 1, 1, 0, 0, 0, 1, 1, 1],
        [1, 0, 0, 0, 1, 1, 0, 0, 1, 1],
        [1, 1, 0, 0, 0, 1, 0, 1, 0, 1],
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 0, 1, 1, 0, 0, 1, 0],
        [1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 0, 0, 1, 1, 1, 1, 1, 1],
        [1, 1, 0, 0, 1, 0, 0, 0, 1, 1],
        [1, 1, 0, 0, 0, 0, 1, 0, 0, 2]];

#Heap
p = Pilha()

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

def vizinhos(i, j):
    vizinhosList = []
    pesoDir = 100
    pesoBaixo = 100
    if i > 0 and not (grid[i-1][j] == 1) and not (grid[i-1][j] == 3) :
        p.empilha(((i-1),j))
        print("Cima")
        print(i-1)
        print(j)
        
        
    if j > 0 and not (grid[i][j-1] == 1) and not (grid[i][j-1] == 3):
        p.empilha(i,(j-1))
        print("Esq")
        print(i)
        print(j-1)

    if i < 9 and not (grid[i][j+1] == 1) and not (grid[i][j+1] == 3):
        pesoDir = abs(i - (j+1))
        print("Dir")
        print(i)
        print(j+1)
        print("Peso Dir")
        print(abs(i - (j+1)))

    if j < 9 and not (grid[i+1][j] == 1) and not (grid[i+1][j] == 3):
        pesoBaixo = abs((i+1) - (j))
        print("Baixo")
        print(i+1)
        print(j)
        print("Peso Baixo")
        print(abs((i+1) - (j)))
        
    if pesoDir <= pesoBaixo:
        p.empilha(i,(j+1))    
    else:
        p.empilha(i,(j+1))
        heapq.heappush(pos, ((i+1),j))    

# A função procura(i,j) faz a verficação da célula visitada;
def procura(i,j):
 
    if grid[i][j] == 2:       
        return True
      
    # Marcando como visitado e atualiza grid
    grid[i][j] = 3;
    atualizaGrid(i,j)
    pygame.time.delay(150)

    vizinhos(i, j)

    posX, posY = heapq.heappop(pos)
    print("PosX PosY")
    print(posX)
    print(posY)

    print("+++++++++++++++++++++++++++++++++++++++++++++++++++=")
    
    atualizaGrid(posX, posY) 
    #pygame.time.delay(500)
    procura(posX, posY)        
    
    return False

printGridIni()
procura(0,0)
#Sai depois de 200 milisegundos
pygame.time.delay(150)


