X = "AGGTAB"
Y = "GXTXAYB"


class LCS:

    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.cache = {}

    def lcs(self, i, j):

        if (i, j) in self.cache:
            return self.cache[(i, j)]

        if i >= len(self.a) or j >= len(self.b):
            return 0

        if self.a[i] == self.b[j]:
            sol = 1 + self.lcs(i + 1, j + 1)
            print(self.a[i], self.b[j])
        else:
            sol = max(self.lcs(i, j + 1), self.lcs(i + 1, j))

        self.cache[(i, j)] = sol

        return sol


lcs = LCS(X, Y)
print(lcs.lcs(0, 0))
