import random

adaptacao = []  #guardar a adaptação de cada individuo nesse vetor
c = 1 #contador de gerações
passos = []

#2 primeiros bits = canibais do lado esquerdo
#bit 3 e 4 = canibais do lado direito
#bit 5 lado atual do barco
#bit 5 e 7 missionarios do lado esquerdo
#bit 8 e 9 missionarios do lado direito
estado_inicial = [1, 1, 0, 0, 0, 1, 1, 0, 0]
estado_final = [0, 0, 1, 1, 1, 0, 0, 1, 1]


def gera_populacao():
    pass


def penalidade():
    pass


def muta():
    pass


def calcula_adaptacao():
    pass


def seleciona():
    pass


def isvalid_moviment():
    pass

def decodifica(move):
    cani_esq = int((''.join(list(map(str, move[0:2])))), 2)
    cani_dir = int((''.join(list(map(str, move[2: 4])))), 2)
    barco = move[4]
    miss_esq = int((''.join(list(map(str, move[5:7])))), 2)
    miss_dir = int((''.join(list(map(str, move[7:9])))), 2)

    return(cani_esq, cani_dir, barco, miss_esq, miss_dir)


gera_populacao()