from copyreg import constructor


tipoPeca = {"mercenario": "merc", "soldado": "sold", "vazio": None, "rei": "king"}


class Peca:
    def __init__(self, tipo):
        self.tipo = tipoPeca[tipo]

    def morte(self):
        del self


def iniciaTabuleiro():
    matriz = []

    for i in range(11):
        defaultValues = [
            Peca("vazio"),
            Peca("vazio"),
            Peca("vazio"),
            Peca("vazio"),
            Peca("vazio"),
            Peca("vazio"),
            Peca("vazio"),
            Peca("vazio"),
            Peca("vazio"),
            Peca("vazio"),
            Peca("vazio"),
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
            ],
        },
        {
            "tipo": "soldado",
            "posicoes": [
                (0, 1),
            ],
        },
        {
            "tipo": "rei",
            "posicoes": [
                (0, 1),
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
                self.matrix[x][y] = Peca(peca["tipo"])
        self.printInTerminal()

    def printInTerminal(self):
        self.printInWeb()
        for linha in self.matrix:
            for peca in linha:
                tipo = peca.tipo
                if tipo == None:
                    print("x", end=" ")
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
                    html += "<td>x</td>"
                else:
                    if tipo == "merc":
                        html += "<td style='background-color: red;'>merc</td>"
                    elif tipo == "sold":
                        html += "<td style='background-color: green;'>sold</td>"
                    elif tipo == "king":
                        html += "<td style='background-color: blue;'>king</td>"
            html += "</tr>"
        html += "</table>"
        html += "</body>"

        # save html
        with open("tabuleiro.html", "w") as f:
            f.write(html)
