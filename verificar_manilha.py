def verifica_manilha(qual_manilha, qual_dek, qual_lista):
    for i in range(0, len(qual_lista)):
        if qual_manilha in qual_lista[i]:
            if 'p' in qual_lista[i]:
                qual_dek[qual_lista[i]] = 14
            elif 'c' in qual_lista[i]:
                qual_dek[qual_lista[i]] = 13
            elif 'e' in qual_lista[i]:
                qual_dek[qual_lista[i]] = 12
            elif 'o' in qual_lista[i]:
                qual_dek[qual_lista[i]] = 11
