from tabuleiro import Tabuleiro
from bestMoveSoldier import melhorMovimento
import os

tab = Tabuleiro()

gameLoop = True

# voce quer jogar como?
print("Bem vindo ao jogo!")
player = input("Voce quer jogar como Soldado(S) ou Mercenario(M)?:\n")
# posiveis M, S

if player == "S" or player == "s":
    player = "sold"
elif player == "M" or player == "m":
    player = "merc"
else:
    print("Opcao invalida")
    gameLoop = False

if player == "merc":
    print("Voce esta jogando como Mercenario\n")
else:
    player = "sold"
    print("Voce esta jogando como Soldado\n")


while gameLoop:
    os.system("clear")
    tab.printInTerminal()
    tab.printInWeb()

    # captar x, y
    positionSelected = input("Digite a posição da peça a ser movida (x, y):\n")
    if positionSelected:
        # split por ,
        positionSelected = positionSelected.split(",")
        # transformar em int
        positionSelected = [int(positionSelected[0]), int(positionSelected[1])]

        peca = tab.matrix[positionSelected[0]][positionSelected[1]]

        if peca.tipo == None:
            print("Nao ha peça nessa posição!\n")
            delay = input('Pressione "Enter" para continuar...')
            continue
        elif peca.tipo == "king" and player == "sold":
            print("Voce escolheu o Rei!\n")
        elif peca.tipo != player:
            print(peca.tipo, player)
            print("Essa peça não é sua!\n")
            delay = input('Pressione "Enter" para continuar...')
            continue

        print(peca.tipo)

        # movimentos possiveis
        movimentosPossiveis = tab.checarMovimentosPossiveis(peca)
        print(movimentosPossiveis)

        if len(movimentosPossiveis) == 0:
            print("Não há movimentos possíveis para essa peça!\n")
            delay = input('Pressione "Enter" para continuar...')
            continue

        print("Os movimentos possíveis para essa peça são:\n")
        for i in range(len(movimentosPossiveis)):
            print("Movimento", i, ":", movimentosPossiveis[i])

        # captar movimento
        movimento = input("Digite o movimento que deseja fazer (numero):\n")
        movimento = int(movimento)

        if movimento >= len(movimentosPossiveis):
            print("Movimento inválido!\n")
            delay = input('Pressione "Enter" para continuar...')
            continue

        tab.moverPeca(
            peca, movimentosPossiveis[movimento][0], movimentosPossiveis[movimento][1]
        )

    # MOVIMENTO INIMIGO
    nomeRealTurno = player
    if player == "sold":
        nomeRealTurno = "soldado"
    else:
        nomeRealTurno = "mercenario"

    melhorMovInimigo = melhorMovimento(tab, nomeRealTurno)
    print("peca", melhorMovInimigo[1])

    print("opa", melhorMovInimigo[0]["x"], melhorMovInimigo[0]["y"])
    tab.moverPeca(
        melhorMovInimigo[1],
        melhorMovInimigo[0]["x"],
        melhorMovInimigo[0]["y"],
    )

    delay = input('Pressione "Enter" para continuar...')
