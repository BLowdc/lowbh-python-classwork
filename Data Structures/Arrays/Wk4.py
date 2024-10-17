def calculateTotal(outletSales):
    total = [0] * 4
    for q in range(4):
        for o in range(50):
            total[q] += outletSales[q][o]
        #next o
    #next q
    for i in total:
        print(i)