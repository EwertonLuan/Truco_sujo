def distribuir(play_lis, play, dek, di):

    from random import choice
    i = 0
    while i < 3:
        f = choice(dek)
        d = di.pop(f)
        play[f] = d
        play_lis.append(f)
        dek.remove(f)
        i += 1

