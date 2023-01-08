class Hash:
    def __init__(self, s: str, base, mod):
        self.mod = mod
        self.l = [0] * len(s)
        self.p = [1] * len(s)
        for i in range(len(s)):
            self.p[i] = (self.p[i - 1] * base) % self.mod
            self.l[i] = (self.l[i - 1] * base + (ord(s[i]) - 96)) % self.mod
        self.l.append(0)

    def hash(self, l, r):
        # [l,r)
        return (self.l[r - 1] - self.l[l - 1] * self.p[r - l - 1]) % self.mod
