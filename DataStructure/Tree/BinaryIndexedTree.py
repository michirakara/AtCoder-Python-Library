class BIT:
    # 0-indexed
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)

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
