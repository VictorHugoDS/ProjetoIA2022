import string
from enumPeca import tipoPeca


class Peca:
    def __init__(self, tipo: string):
        self.tipo = tipoPeca[tipo]

    def morte(self):
        del self
