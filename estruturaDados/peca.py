from typing import Tuple
from enumPeca import tipoPeca

from contants import TabuleiroTamanho


class Peca:
    def __init__(self, tipo, x=None, y=None):
        self.tipo = tipoPeca[tipo]
        self.x = x
        self.y = y

    def morte(self):
        del self

    def tiposIguais(self,peca):
        return self.tipo == peca.tipo

    def estaNaPosicao(self,tupla:Tuple):
        return self.x == tupla(0) and self.y == tupla(1)

    def estaEmUmaDasPosicoes(self,lista:list[Tuple]):
        for posicao in lista:
            if(self.estaNaPosicao(posicao) == True):
                return True
        return False

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
