def dicionario(di, dek):
    for i in dek:
        if '3' in i:
            di[i] = di.get(i, 10)
        elif '2' in i:
            di[i] = di.get(i, 9)
        elif 'a' in i:
            di[i] = di.get(i, 8)
        elif 'k' in i:
            di[i] = di.get(i, 7)
        elif 'j' in i:
            di[i] = di.get(i, 6)
        elif 'q' in i:
            di[i] = di.get(i, 5)
        elif '7' in i:
            di[i] = di.get(i, 4)
        elif '6' in i:
            di[i] = di.get(i, 3)
        elif '5' in i:
            di[i] = di.get(i, 2)
        elif '4' in i:
            di[i] = di.get(i, 1)