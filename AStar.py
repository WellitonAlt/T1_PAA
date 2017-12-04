import heapq
import pygame

from Spot import Spot

# Inicialização do pygame
pygame.init()

# Tamanho e nome da janela
tela = pygame.display.set_mode([400,400])
tela.fill((255, 255, 255))
pygame.display.set_caption("PathFinding AStar")

class AStar(object):
    def __init__(self):
        self.opened = []
        heapq.heapify(self.opened)
        self.closed = set()
        self.spots = []
        self.grid_height = 6
        self.grid_width = 6     
       

    def init_grid(self):
        walls = ((0, 5), (1, 0), (1, 1), (1, 5), (2, 3),
                (3, 1), (3, 2), (3, 5), (4, 1), (4, 4), (5, 1))

                   
        for x in range(self.grid_width):
            for y in range(self.grid_height):
                if (x, y) in walls:
                    noWall = False
                    pygame.draw.rect(tela, (0,0,255) ,(x*40,y*40,40))                    
                else:
                    noWall = True
                    pygame.draw.rect(tela, (255,255,255) ,(j*40,i*40,40,40))               
                self.spots.append(Spot(x, y, noWall))

        pygame.display.update()
        self.start = self.get_spot(0,0)
        self.end = self.get_spot(5,5)


    def get_heuristic(self,spot):
        """
        Calcula o valor h para cada spot: distância entre esse spot
        e o fim do caminho, multiplicando por 10.
        :param spot:
        :return:  valor h
        """
        return 10 * (abs(spot.x - self.end.x) + abs(spot.y - self.end.y))


    def get_spot(self, x, y):
        """
        Retorna o spot da lista de spots

        :param x: coordenada x
        :param y: coordenada y
        :return: spot
        """
        return self.spots[x * self.grid_height + y]

    def get_neighbours(self, spot):
        """
        Retorna os vizinhos do spot passado como parâmetro. A verificação é feita em sentido horário
        a partir do spot mais à direita.

        :param spot: spot referência para a verificação de vizinhos
        :return: lista de vizinhos do spot parâmetro
        """

        spots = []
        if spots.x < self.grid_width - 1:
            spots.append(self.get_spot(spot.x + 1, spot.y))
        if spot.y > 0:
            spots.append(self.get_spot(spot.x, spot.y - 1))
        if spot.x > 0:
            spots.append(self.get_spot(spot.x - 1, spot.y))
        if spot.y < self.grid_height - 1:
            spots.append(self.get_spot(spot.x, spot.y + 1))

        return spots

    def display_path(self):
        """
        Método para exibir caminho encontrado
        :return: DEFINIR
        """
        spot = self.end
        while spot.parent is not self.start:
            spot = spot.parent
            print("Path: cell: %d,%d" % (spot.x, spot.y))


    def update_spot(self, adj, spot):
        """
        Atualizar spot vizinho

        :param adj: Spot vizinho ao spot atual
        :param spot: Spot sendo processado no momento
        """
        adj.g = spot.g + 10
        adj.h = self.get_heuristic(adj)
        adj.parent = spot

        # Função característica da heurística A*
        # f(x) = g(x) + h(x)
        adj.f = adj.g + adj.h
      
                   

    def main(self):        
        # Adiciona spot inicial à heap
        heapq.heappush(self.opened, (self.start.f, self.start))
        while len(self.opened):

            # Retira spot da heap
            f, spot = heapq.heappop(self.opened)

            # Se for o spot final, mostra o caminho
            if spot is self.end:
                self.display_path()
                break

            # Verifica vizinhos
            neighbours = self.get_neighbours(spot)
            for neighbour in neighbours:
                if neighbour.noWall and neighbour not in self.closed:
                    if (neighbour.f, neighbour) in self.opened:
                        # Caso o spot vizinho esteja no open set, checar es o caminho atual é melhor
                        # que o encontrado anteriormente para esse vizinho
                        if neighbour.g > spot.g + 10:
                            self.update_spot(neighbour, spot)
                    else:
                        self.update_spot(neighbour, spot)
                        # Adiciona vizinho ao open set
                        heapq.heappush(self.opened, (neighbour.f, neighbour))
