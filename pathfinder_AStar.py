import pygame
import heapq
# Inicialização do pygame
pygame.init()

# Tamanho e nome da janela
tela = pygame.display.set_mode([400,400])
tela.fill((255, 255, 255))
pygame.display.set_caption("PathFinding Profundidade")

class Pilha(object):
    def __init__(self):
        self.dados = []
 
    def empilha(self, elemento):
        self.dados.append(elemento)
 
    def desempilha(self):
        if not self.vazia():
            return self.dados.pop(-1)
 
    def vazia(self):
        return len(self.dados) == 0

    def topo(self):
        return self.dados[0]
    

        
# Mapa inicial
grid = [[0, 0, 1, 1, 0, 0, 0, 1, 1, 1],
        [1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
        [1, 1, 1, 0, 0, 1, 0, 1, 0, 1],
        [0, 0, 1, 0, 0, 0, 0, 0, 1, 1],
        [1, 0, 1, 1, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 1, 0, 0, 0, 1, 1],
        [1, 1, 0, 0, 0, 0, 1, 0, 0, 2]];

#Pilha
p = Pilha() #pilha Dir
pEsq = Pilha()
pCima = Pilha()

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

#Encontra os vizinhos
def vizinhos(i, j):
    vizinhosList = []
    pesoDir = 100
    pesoBaixo = 100

    #Empilha na pilha da Esquerda              
    if j > 0 and not (grid[i][j-1] == 1) and not (grid[i][j-1] == 3):
        pEsq.empilha((i,(j-1)))       

    #Empilha na pilha de Cima
    if i > 0 and not (grid[i-1][j] == 1) and not (grid[i-1][j] == 3):
         pCima.empilha(((i-1),j))
         
    if j < 9  and not (grid[i][j+1] == 1) and not (grid[i][j+1] == 3):
        pesoDir = abs(i - (j+1))
       
    if i < 9 and not (grid[i+1][j] == 1) and not (grid[i+1][j] == 3):
        pesoBaixo = abs((i+1) - (j))

    #Dependendo do peso empilha primeiro o caminho da esquerda depois o
        #da direito ou ao contrario
    if pesoDir <= pesoBaixo and not (pesoDir == 100):
            p.empilha((i,(j+1)))   
    else:
        if not (pesoBaixo == 100):
            if not (grid[i+1][j] == 1):
                p.empilha(((i+1),j))
   

# A função procura(i,j) faz a verficação da célula visitada;
def procura(i,j):
 
    if grid[i][j] == 2:       
        return True
      
    # Marcando como visitado e atualiza grid
    grid[i][j] = 3;
    atualizaGrid(i,j)
    pygame.time.delay(100)

    #Procura os vizinhos
    vizinhos(i, j)
    if (p.vazia()): #Se não existir mais caminho para baixo ou direita
        pesoCima = 100
        pesoEsq = 100
        if not(pEsq.vazia()):
            posXe, posYe = pEsq.desempilha()
            pesoEsq = abs(posXe - posYe)
        if not(pCima.vazia()):
            posXc, posYc = pCima.desempilha()
            pesoCima = abs(posXc - posYc) + 2 #aumenta o peso do
                                              #caminho de cima para equilibrar
        #Escolhe a melhor opcao de caminhos para cima ou para esquersa
        if pesoEsq <= pesoCima:
            posX = posXe
            posY = posYe            
        else:            
            posX = posXc
            posY = posYc          
    else:      
        posX, posY = p.desempilha()
        
    procura(posX, posY)
    return False

printGridIni()
procura(0,0)
#Sai depois de 200 milisegundos
pygame.time.delay(150)


