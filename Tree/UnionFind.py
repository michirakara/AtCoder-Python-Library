from collections import defaultdict


class UnionFind:
    def __init__(self, n):
        self.n = n
        self.par = [-1] * n
        self.groups = n

    def find(self, x):
        if self.par[x] < 0:
            return x
        self.par[x] = self.find(self.par[x])
        return self.par[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.par[x] > self.par[y]:
            x, y = y, x
        self.par[x] += self.par[y]
        self.par[y] = x
        self.groups -= 1

    def size(self, x):
        return -self.par[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.par) if x < 0]

    def grp_cnt(self):
        return self.groups

    def grp_mem(self):
        grp = defaultdict(list)
        for i in range(self.n):
            grp[self.find(i)].append(i)
        return grp

    def __str__(self):
        return "\n".join(f"{r}: {m}" for r, m in self.grp_mem().items())
