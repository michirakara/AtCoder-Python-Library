class BIT:
    # 0-indexed
    def __init__(self, n, l=[]):
        self.size = n
        self.tree = [0] * (n + 1)
        if l:
            self.tree = [0] + l[:]
            c = [0] * (n + 1)
            for i, j in enumerate(l, 1):
                c[i] = j + c[i - 1]
            for x in range(1, n + 1):
                self.tree[x] = c[x] - c[x - (x & -x)]

    def sum_(self, r):
        # [0,r)
        if r == 0:
            return 0
        s = 0
        while r > 0:
            s += self.tree[r]
            r -= r & -r
        return s

    def sum(self, l, r):
        # [l,r)
        return self.sum_(r) - self.sum_(l)

    def add(self, i, x):
        i += 1
        while i <= self.size:
            self.tree[i] += x
            i += i & -i
