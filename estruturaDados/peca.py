from enumPeca import tipoPeca

from contants import TabuleiroTamanho


class Peca:
    def __init__(self, tipo, x: int, y: int):
        self.tipo = tipoPeca[tipo]
        self.x = x
        self.y = y

    def morte(self):
        del self

    def alterarPosicao(self, x, y):
        self.x = x
        self.y = y

    def subir(self):
        self.y += 1

    def descer(self):
        self.y -= 1

    def esquerda(self):
        self.x -= 1

    def direita(self):
        self.x += 1
