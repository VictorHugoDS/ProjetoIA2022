from copyreg import constructor


class Peca:
    def __init__(self, tipo, x: int, y: int):
        self.tipo = tipoPeca[tipo]
        self.x = x
        self.y = y

    def morte(self):
        del self


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
        self.printInTerminal()

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
