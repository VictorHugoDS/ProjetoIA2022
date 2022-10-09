from enumPeca import tipoPeca


class Peca:
    def __init__(self, tipo, x: int, y: int):
        self.tipo = tipoPeca[tipo]
        self.x = x
        self.y = y

    def morte(self):
        del self
