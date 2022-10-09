from enumPeca import tipoPeca

from contants import TabuleiroTamanho


class Peca:
    def __init__(self, tipo, x=None, y=None):
        self.tipo = tipoPeca[tipo]
        self.x = x
        self.y = y

    def morte(self):
        del self

<<<<<<< HEAD
    def tiposIguais(self,peca):
        return self.tipo == peca.tipo
=======
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
>>>>>>> c1a64da95ec36d3be19c555bb63012aecf311dc6
