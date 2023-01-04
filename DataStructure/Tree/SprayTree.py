class Node:
    def __init__(self):
        self.left = None
        self.right = None
        self.parent = None
        self.size = 1
        self.value = 0

    def rotate(self):
        p = self.parent
        pp = p.parent

        if p.left == self:
            c = self.right
            self.right = p
            p.left = c
        else:
            c = self.left
            self.left = p
            p.right = c

        if pp:
            if pp.left == p:
                pp.left = self
            if pp.right == p:
                pp.right = self
        self.parent = pp
        p.parent = self
        if c:
            c.parent = p

        p.update()
        self.update()

    def state(self):
        if not self.parent:
            return 0
        if self.parent.left == self:
            return 1
        if self.parent.right == self:
            return -1
        return 0

    def splay(self):
        while self.state():
            if not self.parent.state():
                self.rotate()
            elif self.state() == self.parent.state():
                self.parent.rotate()
                self.rotate()
            else:
                self.rotate()
                self.rotate()

    def update(self):
        self.size = 1
        if self.left:
            self.size += self.left.size
        if self.right:
            self.size += self.right.size


def get(ind, node):
    now = node
    while 1:
        lsize = now.left.size if now.left else 0
        if ind < lsize:
            now = now.left
        if ind == lsize:
            now.splay()
            return now
        if ind > lsize:
            now = now.right
            ind = ind - lsize - 1
