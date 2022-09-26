import string
from  enumPeca import tipoPeca
from  peca import Peca

def iniciaTabuleiro():
    matriz = []
    for i in range(11):
        linhaDePecas = [Peca('vazio'),Peca('vazio'),Peca('vazio'),Peca('vazio'),Peca('vazio'),Peca('vazio'),Peca('vazio'),Peca('vazio'),Peca('vazio'),Peca('vazio'),Peca('vazio')]
        matriz.append(linhaDePecas)
    return matriz

# positivo vertical, negativo horizontal
def preencheLugares(matriz,direcao:int,peca,x,y):
    if (direcao >0):
        for i in range(direcao):
            matriz[x+i-1,y]=Peca(peca)
    if (direcao <0):
        for i in range(direcao):
            matriz[x,y+i-1]=Peca(peca)


class Tabuleiro:

    def __init__(self):
        matriz = iniciaTabuleiro()
        self.matriz = matriz
        #Posiciona peças
        preencheLugares(matriz,5,'mercenario',3,0)
        preencheLugares(matriz,5,'mercenario',3,10)
        preencheLugares(matriz,-5,'mercenario',3,10)
        preencheLugares(matriz,-5,'mercenario',0,10)

