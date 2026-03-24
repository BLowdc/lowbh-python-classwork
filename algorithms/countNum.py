def countNum(arr: list):
    dict = {}
    for n in arr:
        if n not in dict:
            dict[n] = 1
        else:
            dict[n] += 1

    for n in dict:
        print(n, ":", dict[n], "times")


a = [1, 5, 2, 7, 4, 7, 8, 4, 8, 7]
countNum(a)
