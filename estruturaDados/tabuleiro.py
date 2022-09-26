tipoPeca = {
    'mercenario': 'merc',
    'soldado': 'sold',
    'vazio': None,
    'rei': 'king'
}

class Peca:
    def __init__(self,tipo):
        self.tipo = tipoPeca[tipo]
    def morte(self):
        del self

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
                    (0,3),
                    (0,4),
                    (0,5),
                    (0,6),
                    (0,7),
                    (1,5),
                    (3,0),
                    (4,0),
                    (5,0),
                    (6,0),
                    (7,0),
                    (5,1),
                    (10,3),
                    (10,4),
                    (10,5),
                    (10,6),
                    (10,7),
                    (9,5),
                    (10,3),
                    (10,4),
                    (10,5),
                    (10,6),
                    (10,7),
                    (9,5),
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
        self.matrix = iniciaTabuleiro()
        pecas = objetoInicializacao()

        for peca in pecas:  
            tipo = peca['tipo']
            posicoes = peca['posicoes']
            for posicao in posicoes:
                x = posicao[0]
                y = posicao[1]
                self.matrix[x][y] = Peca(tipo)
        
    def printInWeb(self):
        html = ''
        for linha in self.matrix:
            html += '<tr>'
            for peca in linha:
                tipo = peca.tipo
                if tipo == None:
                    html += '<td></td>'
                else:
                    html += '<td>'+tipo+'</td>'
            html += '</tr>'

        html_grid = '<table>'+html+'</table>'


        # save html
        with open('tabuleiro.html','w') as f:
            f.write(html_grid)
        