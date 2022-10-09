from copyreg import constructor
from time import sleep

from peca import Peca

tipoPeca = {"mercenario": "merc", "soldado": "sold", "vazio": None, "rei": "king"}


def iniciaTabuleiro():
    matriz = []

    for i in range(11):
        defaultValues = [
            Peca("vazio", 0, 0),
            Peca("vazio", 0, 0),
            Peca("vazio", 0, 0),
            Peca("vazio", 0, 0),
            Peca("vazio", 0, 0),
            Peca("vazio", 0, 0),
            Peca("vazio", 0, 0),
            Peca("vazio", 0, 0),
            Peca("vazio", 0, 0),
            Peca("vazio", 0, 0),
            Peca("vazio", 0, 0),
        ]
        linhaDePecas = defaultValues
        matriz.append(linhaDePecas)

    return matriz


def objetoInicializacao():
    return [
        {
            "tipo": "mercenario",
            "posicoes": [
                (0, 3),
                (0, 4),
                (0, 5),
                (0, 6),
                (0, 7),
                (1, 5),
                (3, 0),
                (4, 0),
                (5, 0),
                (6, 0),
                (7, 0),
                (5, 1),
                (10, 3),
                (10, 4),
                (10, 5),
                (10, 6),
                (10, 7),
                (9, 5),
                (10, 3),
                (10, 4),
                (10, 5),
                (10, 6),
                (10, 7),
                (9, 5),
                (3, 10),
                (4, 10),
                (5, 10),
                (6, 10),
                (7, 10),
                (5, 9),
                (0, 3),
            ],
        },
        {
            "tipo": "soldado",
            "posicoes": [
                (5, 4),
                (5, 6),
                (5, 7),
                (5, 3),
                (4, 4),
                (4, 6),
                (6, 4),
                (6, 6),
                (7, 5),
                (6, 5),
                (4, 5),
                (3, 5),
            ],
        },
        {
            "tipo": "rei",
            "posicoes": [
                (5, 5),
            ],
        },
    ]


class Tabuleiro:
    def __init__(self):
        self.matrix = iniciaTabuleiro()
        pecas = objetoInicializacao()

        for peca in pecas:
            for posicao in peca["posicoes"]:
                x = posicao[0]
                y = posicao[1]
                self.matrix[x][y] = Peca(peca["tipo"], x, y)
                if(x==6 and y==6):
                    print("/////////////////////////////")
                    print(self.pecasProximasAUmaPeca(Peca(peca["tipo"], x, y)))
                    print("/////////////////////////////")
        print("[Tabuleiro] Tabuleiro inicializado com sucesso!")
        print()

    def pecasProximasAUmaPeca(self,peca:Peca):
        
        x = peca.x
        y = peca.y
        pecas = {}
        posicaoInvestigada = [None,x,y]
        pecavazia = Peca('vazio', x, y)

        #encontra peça superior
        while(posicaoInvestigada[0]==None):
            if(y==0 or posicaoInvestigada[2]==0):
                posicaoInvestigada[0] = pecavazia
            else:
                if(self.matrix[x][y-1].tiposIguais(pecavazia) == False):
                    posicaoInvestigada[0] = self.matrix[x][y-1]
            posicaoInvestigada[2] += -1
        
        pecas['superior']=posicaoInvestigada[0]
        posicaoInvestigada = [None,x,y]


        #encontra peça inferior
        while(posicaoInvestigada[0]==None):
            if(y==10 or posicaoInvestigada[2]==10):
                posicaoInvestigada[0] = pecavazia
            else:
                if(self.matrix[x][y+1].tiposIguais(pecavazia) == False):
                    posicaoInvestigada[0] = self.matrix[x][y+1]
            posicaoInvestigada[2] += 1

        pecas['inferior']=posicaoInvestigada[0]
        posicaoInvestigada = [None,x,y]

        #encontra peça a esquerda
        while(posicaoInvestigada[0]==None):
            if(x==0 or posicaoInvestigada[1]==0):
                posicaoInvestigada[0] = pecavazia
            else:
                if(self.matrix[x-1][y].tiposIguais(pecavazia) == False):
                    posicaoInvestigada[0] = self.matrix[x-1][y]
            posicaoInvestigada[1] += -1

        pecas['esquerda']=posicaoInvestigada[0]
        posicaoInvestigada = [None,x,y]

        #encontra peça a direita
        while(posicaoInvestigada[0]==None):
            if(x==10 or posicaoInvestigada[1]==10):
                posicaoInvestigada[0] = pecavazia
            else:
                if(self.matrix[x+1][y].tiposIguais(pecavazia) == False):
                    posicaoInvestigada[0] = self.matrix[x+1][y]
            posicaoInvestigada[1] += 1

        pecas['direita']=posicaoInvestigada[0]
        return pecas


    def printInTerminal(self):
        self.printInWeb()
        for linha in self.matrix:
            for peca in linha:
                tipo = peca.tipo
                if tipo == None:
                    print("----", end=" ")
                else:
                    print(tipo, end=" ")
            print()
        print()
        print("[Tabuleiro] Tabuleiro impresso no terminal com sucesso!")

    def printInWeb(self):
        html = ""
        # add html header
        html += "<!DOCTYPE html>"
        html += "<html>"
        html += "<head>"
        html += "<title>Tabuleiro</title>"
        html += "</head>"
        html += "<body>"

        # add html body
        html += "<table>"
        for linha in self.matrix:
            html += "<tr>"
            for peca in linha:
                tipo = peca.tipo
                if tipo == None:
                    html += "<td>xxx</td>"
                else:
                    if tipo == "merc":
                        html += "<td>💰</td>"
                    elif tipo == "sold":
                        html += "<td>🪖</td>"
                    elif tipo == "king":
                        html += "<td>👑</td>"
            html += "</tr>"
        html += "</table>"
        html += "</body>"

        # save html
        with open("tabuleiro.html", "w") as f:
            f.write(html)
