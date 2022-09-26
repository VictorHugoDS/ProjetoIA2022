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
def objetoInicializacao():
    return(
        [
            {
                'tipo': 'mercenario',
                'posicao': [{}]
            }
        ]
    )




class Tabuleiro:

    def __init__(self):
        matriz = iniciaTabuleiro()
        self.matriz = matriz
        #Posiciona peças
        


