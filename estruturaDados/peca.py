from enumPeca import tipoPeca


class Peca:
    def __init__(self, tipo, x=None, y=None):
        self.tipo = tipoPeca[tipo]
        self.x = x
        self.y = y

    def morte(self):
        del self

    def tiposIguais(self,peca):
        return self.tipo == peca.tipo
