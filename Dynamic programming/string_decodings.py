a = [1, 2, 1]

mapper = {i: chr(96 + i) for i in range(1, 27)}


def numToAplha(index, s):

    if index >= len(a):
        print(s)
        return

    first = mapper[a[index]]

    numToAplha(index + 1, s + first)

    if not (a[index] == 2 and a[index + 1] > 7):
        second = mapper[a[index] * 10 + a[index + 1]]
        numToAplha(index + 2, s + second)


numToAplha(0, "")