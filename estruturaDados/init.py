from tabuleiro import Tabuleiro

tab = Tabuleiro()

tab.printInTerminal()

primeiraPeca = tab.pecasSoldados()[1]

print(tab.checarMovimentosPossiveis(primeiraPeca))

print(tab.pegarPosicaoRei())
