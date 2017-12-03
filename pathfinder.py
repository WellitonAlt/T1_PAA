grid = [[0, 0, 0, 0, 0, 1],
        [1, 1, 0, 0, 0, 1],
        [0, 0, 0, 1, 0, 0],
        [0, 1, 1, 0, 0, 1],
        [0, 1, 0, 0, 1, 0],
        [0, 1, 0, 0, 0, 2]]

# A função search(x,y) faz a verficação da célula visitada;
def search(x,y):
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

    # Marcando como visitado
    grid[x][y] = 3;

    # Explorando vizinhos em sentido horário começando pelo da direita
    if ((x < len(grid)-1 and search(x+1, y))
        or (y > 0 and search(x, y-1))
        or (x > 0 and search(x-1, y))
        or (y < len(grid)-1 and search(x, y+1))):
        return True

    return False

search(0,0)