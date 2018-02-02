from random import randint
from verificar_manilha import verifica_manilha
from distribui_cartas import distribuir
from dek_dicionario import dicionario
from cria_manilha import criar_manilha


dek = ['p3', 'p2', 'pa', 'pk', 'pj', 'pq', 'p7', 'p6', 'p5', 'p4', 'c3', 'c2', 'ca', 'ck', 'cj', 'cq', 'c7', 'c6',
       'c5', 'c4', 'e3', 'e2', 'ea', 'ek', 'ej', 'eq', 'e7', 'e6', 'e5', 'e4', 'o3', 'o2', 'oa', 'ok', 'oj', 'oq',
       'o7', 'o6', 'o5', 'o4']
di = {}
# criando dek com valores(di)
dicionario(di, dek)

# Mão para saber qual é a maior

play1 = {}
play2 = {}

# Mão dos jogadores
play1_l = []
play2_l = []

# dando cartas
distribuir(play1_l, play1, dek, di)
distribuir(play2_l, play2, dek, di)

manilha = []
manilha_l = []

criar_manilha(dek, manilha, manilha_l)

print('manilha', manilha)
print('manilha lista', manilha_l)

verifica_manilha(manilha[0], di, dek)
verifica_manilha(manilha[0], play1, play1_l)
verifica_manilha(manilha[0], play2, play2_l)

j1_pontos = 0
j2_pontos = 0
print(play1_l, play2_l)

while True:
    n = 0
    c = 0
    for i in play1:
        print(f'{n} para escolher {i}')
        n += 1
    escolha = int(input('escolha a primeirra jogada: '))
    print('sua primeira jogada é {}'.format(play1_l[escolha]))
    j_1 = play1_l[escolha]
    j_1_escolha = play1[j_1]
    if c == 0:
        maior = j_1_escolha
    elif j_1_escolha >= maior:
        maior = j_1_escolha
    print(j_1_escolha)

    menor_2 = play2_l[0]
    maior_2 = play2_l[0]
    meio = play2_l[0]
    for carta in range(0, len(play2)):
        print(play2[play2_l[carta]], play2[maior_2])
        if len(play2) > 0:
            if play2[play2_l[carta]] > play2[maior_2]:
                maior_2 = play2_l[carta]
            elif carta == 1:
                if play2[play2_l[carta]] < play2[meio]:
                    meio = play2_l[carta]
                    menor_2 = play2_l[carta]
            elif play2[play2_l[carta]] < play2[menor_2]:
                menor_2 = play2_l[carta]

    if play2[menor_2] >= maior:
        j_2_escolha = play2[menor_2]
    elif play2[meio] >= maior:
        j_2_escolha = play2[meio]
    elif play2[maior_2] >= maior:
        j_2_escolha = play2[maior_2]

    print('menoar', menor_2, 'maior', maior_2, 'meio', meio)

    if j_2_escolha > maior:
        j2_pontos += 1
        vitoria = 'Maior carta do jogador 2'
        del play2[play2_l[escolha]]
        play2_l.remove(play2_l[escolha])
    menor_2 = play2_l[0]
    maior_2 = play2_l[0]
    meio = play2_l[0]
    for carta in range(0, len(play2)):
        print(play2[play2_l[carta]], play2[maior_2])
        if len(play2) > 0:
            if play2[play2_l[carta]] > play2[maior_2]:
                maior_2 = play2_l[carta]
            elif carta == 1:
                if play2[play2_l[carta]] < play2[meio]:
                    meio = play2_l[carta]
                    menor_2 = play2_l[carta]
            elif play2[play2_l[carta]] < play2[menor_2]:
                menor_2 = play2_l[carta]
    j_2_escolha = play2[menor_2]

    print(j_2_escolha)
    if j_1_escolha == maior:
        j1_pontos += 1

    del play1[play1_l[escolha]]
    play1_l.remove(play1_l[escolha])
    del play2[play2_l[escolha]]
    play2_l.remove(play2_l[escolha])
    c+=1

pontos = 0

print()
if j1_pontos > j2_pontos and j1_pontos > j2_pontos and j1_pontos > j4_pontos:
    print('voce ganhou 1')
    pontos += 1
elif j2_pontos > j1_pontos and j2_pontos > j3_pontos and j2_pontos > j4_pontos:
    print('voce ganhou 1')
    pontos += 1
