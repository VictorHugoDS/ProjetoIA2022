TabuleiroTamanho = 11
PosicoesVitoria = [
    (0, 0),
    (0, TabuleiroTamanho - 1),
    (TabuleiroTamanho - 1, 0),
    (TabuleiroTamanho - 1, TabuleiroTamanho - 1),
]

RamificacoesMaximas = 5

PosicoesIniciais = [
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

PosicoesProximasTrono = [(5, 4), (5, 7), (4, 5), (6, 5)]
