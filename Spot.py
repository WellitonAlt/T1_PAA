class Spot(object):
    def __init__(self, x, y, noWall):
        """
        :param x: coordenada x
        :param y: coordenada y
        :param noWall: é alcançável ou não
        """

        self.noWall = noWall
        self.x = x
        self.y = y
        self.parent = None

        # Valores para palpite educado
        self.f = 0
        self.g = 0
        self.h = 0