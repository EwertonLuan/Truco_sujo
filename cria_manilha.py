
def criar_manilha(dek, manilha, manilha_l):
    from random import randint
    p_carta = randint(0, len(dek)-1)  # escolha da primeira carta

    print('A primeira carta é {}'.format(dek[p_carta]))
    lista_cartas = ['4','5', '6', '7', 'q', 'k', 'j', 'a', '2', '3']
    c = 0
    while c <= 9:
        if lista_cartas[c] in dek[p_carta]:

            if c < (len(lista_cartas) - 1):
                mani = lista_cartas[c + 1]
            elif c == 9:
                mani = lista_cartas[0]
            print(mani)
            for i in range(0, len(dek) - 1):
                if mani in dek[i]:
                    manilha_l.append(dek[i])

        c += 1
    manilha.append(mani)