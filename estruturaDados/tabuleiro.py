import string
from  enumPeca import tipoPeca
from  peca import Peca

def iniciaTabuleiro():
    matriz = []
    
    defaultValues = [Peca('vazio'),Peca('vazio'),Peca('vazio'),Peca('vazio'),Peca('vazio'),Peca('vazio'),Peca('vazio'),Peca('vazio'),Peca('vazio'),Peca('vazio'),Peca('vazio')]
    
    for i in range(11):
        linhaDePecas = defaultValues
        matriz.append(linhaDePecas)

    return matriz

def objetoInicializacao():
    return(
        [
            {
                'tipo': 'mercenario',
                'posicoes': [
                    (0,0),
                ]
            },
            {
                'tipo': 'soldado',
                'posicoes': [
                    (0,1),
                ]
            },
            {
                'tipo': 'rei',
                'posicoes': [
                    (0,1),
                ]
            }
        ]
    )

class Tabuleiro:

    def __init__(self):
        matriz = iniciaTabuleiro()
        self.matriz = matriz

        pecas = objetoInicializacao()

        for peca in pecas:  
            tipo = peca['tipo']
            posicoes = peca['posicao']
            for posicao in posicoes:
                x = posicao[0]
                y = posicao[1]
                self.matriz[x][y] = Peca(tipo)
        

