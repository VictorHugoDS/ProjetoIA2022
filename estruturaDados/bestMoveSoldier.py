# Define qual o melhor movimento para soldado

from tabuleiro import Tabuleiro
from peca import Peca
from contants import PosicoesProximasTrono, PontosDeVitoria
from enumPeca import tipoPeca
import random

# tipos de movimentos

# Comer um mercenário -> 3
eat = 3

# Permitir Rei chegar ao objetivo -> 6
goToWin = 6

# Proteger o Rei entrando na frente de um mercenário -> 5
defKing = 5

#random -> 0
yoggSaron = 0


turnoPosiveis = "mercenario" | "soldado"



def verificaSePodeComer(tabuleiro: Tabuleiro, soldado: Peca, mercenario: Peca):
    pecasProximas = tabuleiro.pecasProximasAUmaPeca(mercenario)
    for key in pecasProximas:
        if mercenario.estaEmUmaDasPosicoes(PosicoesProximasTrono):
            return True
        if pecasProximas[key].tiposIguais(soldado) and pecasProximas[key] != soldado:
            return True

    return False


def protejamORei(vetorPecasProximasKing, tabuleiro:Tabuleiro, rei, soldado, xRei, yRei):
    for peca in vetorPecasProximasKing:
        if peca.tipo == tipoPeca["mercenario"]:
            for valores in tabuleiro.casasDeAlinhamento(rei, soldado):
                resultado = tabuleiro.verificarSeEntre2casas(
                    xRei, yRei, peca.x, peca.y, valores(0), valores(1)
                )
                if resultado and tabuleiro.podeMovimentar(soldado,valores(0), valores(1)):
                    alteraMelhorResultado(defKing,'Defender Rei', valores(0), valores(1))
                    break


def comerUmaPeca(vetorPecas, soldado):
    if melhorResultado["peso"] > eat:
        return 0

    for peca in vetorPecas:
        if peca.tipo == tipoPeca["soldado"] and verificaSePodeComer(peca):
            melhorResultado["peso"] = eat
            melhorResultado["estrategia"] = 'Comer Mercenário'
            if peca.x == soldado.x:
                melhorResultado["x"] = soldado.x
                if soldado.y > peca.y:
                    melhorResultado["y"] = peca.y - 1
                else:
                    melhorResultado["y"] = peca.y + 1
            else:
                melhorResultado["y"] = soldado.y
                if soldado.x > peca.x:
                    melhorResultado["x"] = peca.x - 1
                else:
                    melhorResultado["x"] = peca.x + 1


def alteraMelhorResultado(peso,estrategia, x, y):
    if melhorResultado["peso"] < peso:
        melhorResultado["peso"] = peso
        melhorResultado["estrategia"] = estrategia
        melhorResultado["x"] = x
        melhorResultado["y"] = y

def moveAleatorio(soldado,pecaLimite,direcao):
    x= None
    y= None
    match direcao:
        case 'esquerda':
            x = pecaLimite.x
            diff = soldado.y - pecaLimite.y
            y = soldado.y - random.randint(1,abs(diff))
        case 'direita':
            x = pecaLimite.x
            diff = soldado.y - pecaLimite.y
            y = soldado.y + random.randint(1,abs(diff))
        case 'superior':
            y = pecaLimite.y
            diff = soldado.x - pecaLimite.x
            y = soldado.x - random.randint(1,abs(diff))
        case 'inferior':
            y = pecaLimite.y
            diff = soldado.x - pecaLimite.x
            y = soldado.x + random.randint(1,abs(diff))
    alteraMelhorResultado(yoggSaron,'jogar em uma posição aleatória',x,y)
    
    

def movimentoRandow(soldado: Peca,tabuleiro: Tabuleiro,vetorPecas):
    podeMover = {
        'esquerda':True,
        'direita':True,
        'superior':True,
        'inferior':True,
    }

    posicoes = ['superior','inferior','esquerda','direita']
    i=0
    for peca in vetorPecas:
        if(tabuleiro.verificarAdjacencias(soldado,peca)):
            podeMover[posicoes[i]]=False
        i+=1

    listaDePossibilidades = []
    for key in podeMover:
        if(podeMover[key]==True):
            listaDePossibilidades.append(key)
    direcaoEscolhida = listaDePossibilidades[random.randint(0,len(listaDePossibilidades))]

    pecaEscolhida = None
    i=0
    for peca in vetorPecas:
        if(posicoes[i]==direcaoEscolhida):
            pecaEscolhida=peca
            break

    moveAleatorio(soldado,pecaEscolhida,direcaoEscolhida)



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


# todo lembrar de ajustes retornos para formato esperado
def melhorMovimentoSoldado(tabuleiro: Tabuleiro, soldado: Peca):
    xRei = tabuleiro.posicaoRei(0)
    yRei = tabuleiro.posicaoRei(1)
    rei = tabuleiro.matrix[xRei][yRei]
    global melhorResultado 

    melhorResultado = {"peso": 0,'estrategia':None, "x": None, "y": None}

    pecasProximas = tabuleiro.pecasProximasAUmaPeca(soldado)

    PecaSuperior=pecasProximas["superior"]
    PecaInferior=pecasProximas["inferior"]
    PecaEsquerda=pecasProximas["esquerda"]
    PecaDireita=pecasProximas["direita"]
    vetorPecas = [PecaSuperior,PecaInferior,PecaEsquerda,PecaDireita]
    comerUmaPeca(vetorPecas,soldado)


    pecasProximas = tabuleiro.pecasProximasAUmaPeca(rei)

    pecaKingSuperior=pecasProximas["superior"]
    pecaKingInferior=pecasProximas["inferior"]
    pecaKingEsquerda=pecasProximas["esquerda"]
    pecaKingDireita=pecasProximas["direita"]
    vetorPecasProximasKing = [pecaKingSuperior,pecaKingInferior,pecaKingEsquerda,pecaKingDireita]

    protejamORei(vetorPecasProximasKing,tabuleiro,rei,soldado,xRei,yRei)
    movimentoRandow(soldado,tabuleiro,vetorPecas)

    return melhorResultado
    # Terminar no final
    # for ponto in PontosDeVitoria:
    #     if(tabuleiro.verificarSeEntre2casas(ponto[0],ponto[1],xRei,yRei,soldado)):