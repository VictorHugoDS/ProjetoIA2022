# Define qual o melhor movimento para soldado

from tabuleiro import Tabuleiro
from peca import Peca

# tipos de movimentos

# Comer um mercenário -> 4
# Permitir Rei chegar ao objetivo -> 10
# Proteger o Rei -> 6
# Proteger o Rei Comendo uma Peça -> 12
# Colocar-se em perigo -> -2
# Abrir Caminho para o Rei -> 3
from contants import RamificacoesMaximas

turnoPosiveis = "mercenario" | "soldado"


def melhorMovimentoSoldado(tabuleiro: Tabuleiro, soldado: Peca):
    # Peca, x,y,peso
    return (Peca, 0, 0, 10)


def melhorMovimento(tabuleiro: Tabuleiro, turno: turnoPosiveis):
    isSoldadoTurno = turno == "soldado"
    pecasDoTime

    if isSoldadoTurno:
        pecasDoTime = tabuleiro.pecasMercenarios()
    else:
        pecasDoTime = tabuleiro.pecasSoldados()

    pesosMovimentos = []
    for peca in pecasDoTime:
        pesoMovimento = melhorMovimentoSoldado(tabuleiro, peca)
        pesosMovimentos.append(pesoMovimento)

    pesosMovimentos.sort(key=lambda x: x[3], reverse=True)
    return pesosMovimentos[0]
    # tuple[Type[Peca], Literal[0], Literal[0], Literal[10]]


def melhorMovimentoRamificado(
    tabuleiro: Tabuleiro, turno: turnoPosiveis, profundidade: int
):
    if profundidade == 0:
        return melhorMovimento(tabuleiro, turno)

    isSoldadoTurno = turno == "soldado"

    tabuleiroSimulado = tabuleiro.copia()

    pesosMovimentosSoldado = 0
    pesosMovimentosMercenario = 0

    # profundida par
    if profundidade % 2 != 0:
        profundidade += 1

    for i in range(profundidade):
        melhorMovdPecas = melhorMovimento(tabuleiroSimulado, turno)
        tabuleiroSimulado.moverPeca(
            melhorMovdPecas[0], melhorMovdPecas[1], melhorMovdPecas[2]
        )
        if turno == "mercenario":
            pesosMovimentosMercenario += melhorMovdPecas[3]
            turno = "soldado"
        else:
            pesosMovimentosSoldado += melhorMovdPecas[3]
            turno = "mercenario"

    if isSoldadoTurno:
        return pesosMovimentosSoldado
    else:
        return pesosMovimentosMercenario


""" 
    pesosMovimentos = []
    for peca in pecasDoTime:
        pesoMovimento = melhorMovimentoSoldado(tabuleiro, peca)
        pesosMovimentos.append(pesoMovimento)

    pesosMovimentos.sort(key=lambda x: x[3], reverse=True)
    return pesosMovimentos[0] """
