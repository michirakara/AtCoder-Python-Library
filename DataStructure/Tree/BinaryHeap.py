class Heap:
    def __init__(self):
        self.l = []

    def __str__(self):
        re = "-start-\n"
        i = 1
        while 1:
            re += " ".join(
                [*map(str, self.l[2 ** (i - 1) - 1 : min(len(self.l), 2**i - 1)])]
            )
            if len(self.l) <= 2**i - 1:
                re += "\n--end--"
                return re
            re += "\n"
            i += 1

    def push(self, n):
        ind = len(self.l)
        self.l.append(n)
        while ind != 0 and self.l[(ind - 1) // 2] < self.l[ind]:
            self.l[(ind - 1) // 2], self.l[ind] = self.l[ind], self.l[(ind - 1) // 2]
            ind = (ind - 1) // 2

    def pop(self):
        if not self.l:
            return None
        if len(self.l) == 1:
            return self.l.pop()

        ret = self.l[0]
        v = self.l[0] = self.l.pop()

        ind = 0
        while ind * 2 + 1 < len(self.l):
            l_i = ind * 2 + 1
            r_i = ind * 2 + 2
            if r_i < len(self.l) and self.l[r_i] > self.l[l_i]:
                l_i = r_i
            if self.l[l_i] <= v:
                break
            self.l[ind] = self.l[l_i]
            ind = l_i
        self.l[ind] = v
        return ret
