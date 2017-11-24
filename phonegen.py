def phonegen():
    d1, d2, d3, d4, d5, d6, d7 = 0, 0, 0, 0, 0, 0, 0
    phlist = []
    for d1 in range(1, 10):
        for d2 in range(1, 10):
            for d3 in range(1, 10):
                for d4 in range(1, 10):
                    for d5 in range(1, 10):
                        for d6 in range(1, 10):
                            for d7 in range(1, 10):
                                phone = '010' + '-' + str(d1) + str(d2) + str(d3)
                                phone = phone + '-' + str(d4) + str(d5) + str(d6) + str(d7)
                                phlist.append(phone)
    return phlist

phonegen()