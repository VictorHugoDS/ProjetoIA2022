from copyreg import constructor
from time import sleep

from peca import Peca
from contants import TabuleiroTamanho, PontosDeVitoria
from utils import DevLog

tipoPeca = {"mercenario": "merc", "soldado": "sold", "vazio": None, "rei": "king"}


def iniciaTabuleiro():
    matriz = []

    for i in range(TabuleiroTamanho):
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
        self.posicaoRei = (5, 5)

        for peca in pecas:
            for posicao in peca["posicoes"]:
                x = posicao[0]
                y = posicao[1]
                self.matrix[x][y] = Peca(peca["tipo"], x, y)
                if peca["tipo"] == "king":
                    self.posicaoRei = (x, y)
        DevLog("[Tabuleiro] Tabuleiro inicializado com sucesso!")
        DevLog()

    def pegarPosicaoRei(self):
        return self.posicaoRei

    def moverPeca(self, peca, x, y):
        if peca.tipo == "king":
            self.posicaoRei = (x, y)

        self.matrix[peca.x][peca.y] = Peca("vazio", peca.x, peca.y)
        self.matrix[x][y] = peca
        peca.mover(x, y)

    def checarMovimento(self, x, y):
        tabuleiro = self.matrix
        if x < 0 or x > TabuleiroTamanho or y < 0 or y > TabuleiroTamanho:
            return False
        if tabuleiro[x][y].tipo == None:
            return True

        return False

    # retorna uma lista de tuplas com as posições possíveis
    def checarMovimentosPossiveis(self, peca):
        copiaPeca = peca
        movimentosPossiveis = []

        # (x,y)
        esquerda_futuro = (copiaPeca.x - 1, copiaPeca.y)
        direita_futuro = (copiaPeca.x + 1, copiaPeca.y)
        cima_futuro = (copiaPeca.x, copiaPeca.y + 1)
        baixo_futuro = (copiaPeca.x, copiaPeca.y - 1)

        movimentosFuturos = [esquerda_futuro, direita_futuro, cima_futuro, baixo_futuro]

        DevLog(
            "[Tabuleiro] Checando movimentos possíveis para a peça:",
        )
        DevLog(
            copiaPeca.x,
            copiaPeca.y,
            copiaPeca.tipo,
        )
        DevLog()

        # testa movimentos
        for movimento in movimentosFuturos:
            x_internal = movimento[0]
            y_internal = movimento[1]
            DevLog("[Tabuleiro] Checando movimento: ", x_internal, y_internal)

            if self.checarMovimento(x_internal, y_internal):
                DevLog("[Tabuleiro] Movimento possível: ", x_internal, y_internal)
                movimentosPossiveis.append((x_internal, y_internal))

        return movimentosPossiveis

    def pecasMercenarios(self):
        pecas = []
        for linha in self.matrix:
            for peca in linha:
                if peca.tipo == "merc":
                    pecas.append(peca)
        return pecas

    def pecasSoldados(self):
        pecas = []
        for linha in self.matrix:
            for peca in linha:
                if peca.tipo == "sold" or peca.tipo == "king":
                    pecas.append(peca)
        return pecas

    def pecasProximasAUmaPeca(self, peca: Peca):

        x = peca.x
        y = peca.y
        pecas = {}
        posicaoInvestigada = [None, x, y]
        pecavazia = Peca("vazio", x, y)

        # encontra peça superior
        while posicaoInvestigada[0] == None:
            if y == 0 or posicaoInvestigada[2] == 0:
                posicaoInvestigada[0] = pecavazia
            else:
                if self.matrix[x][y - 1].tiposIguais(pecavazia) == False:
                    posicaoInvestigada[0] = self.matrix[x][y - 1]
            posicaoInvestigada[2] += -1

        pecas["superior"] = posicaoInvestigada[0]
        posicaoInvestigada = [None, x, y]

        # encontra peça inferior
        while posicaoInvestigada[0] == None:
            if y == 10 or posicaoInvestigada[2] == 10:
                posicaoInvestigada[0] = pecavazia
            else:
                if self.matrix[x][y + 1].tiposIguais(pecavazia) == False:
                    posicaoInvestigada[0] = self.matrix[x][y + 1]
            posicaoInvestigada[2] += 1

        pecas["inferior"] = posicaoInvestigada[0]
        posicaoInvestigada = [None, x, y]

        # encontra peça a esquerda
        while posicaoInvestigada[0] == None:
            if x == 0 or posicaoInvestigada[1] == 0:
                posicaoInvestigada[0] = pecavazia
            else:
                if self.matrix[x - 1][y].tiposIguais(pecavazia) == False:
                    posicaoInvestigada[0] = self.matrix[x - 1][y]
            posicaoInvestigada[1] += -1

        pecas["esquerda"] = posicaoInvestigada[0]
        posicaoInvestigada = [None, x, y]

        # encontra peça a direita
        while posicaoInvestigada[0] == None:
            if x == 10 or posicaoInvestigada[1] == 10:
                posicaoInvestigada[0] = pecavazia
            else:
                if self.matrix[x + 1][y].tiposIguais(pecavazia) == False:
                    posicaoInvestigada[0] = self.matrix[x + 1][y]
            posicaoInvestigada[1] += 1

        pecas["direita"] = posicaoInvestigada[0]
        return pecas

    def printInTerminal(self):
        self.printInWeb()
        for linha in self.matrix:
            for peca in linha:
                tipo = peca.tipo
                x = peca.x
                y = peca.y

                if tipo == None:
                    print(" ", end=" ")
                    DevLog("----", end=" ")
                else:
                    DevLog(tipo, end=" ")

            DevLog()
        DevLog()
        DevLog("[Tabuleiro] Tabuleiro impresso no terminal com sucesso!")

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
