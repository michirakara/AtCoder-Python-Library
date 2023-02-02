import random


class TreapNode:
    def __init__(self, data):
        self.data = data  # ノードの値
        self.priority = random.random()
        self.left = None
        self.right = None
        self.count = 1
        self.sum = data


def count(t):
    if not t:
        return 0
    return t.count


def sum_(t):
    if not t:
        return 0
    return t.sum


def update(node):
    node.count = count(node.left) + count(node.right) + 1
    node.sum = sum_(node.left) + sum_(node.right) + node.data
    return node


def rotate_right(node):
    lnode = node.left
    node.left = lnode.right
    lnode.right = node
    update(node)
    update(lnode)
    return lnode


def rotate_left(node):
    rnode = node.right
    node.right = rnode.left
    rnode.left = node
    update(node)
    update(rnode)
    return rnode


def insert(node, x):
    if node is None:
        return TreapNode(x)
    elif x == node.data:
        return node
    elif x < node.data:
        node.left = insert(node.left, x)
        update(node)
        if node.priority > node.left.priority:
            node = rotate_right(node)
    else:
        node.right = insert(node.right, x)
        update(node)
        if node.priority > node.right.priority:
            node = rotate_left(node)
    return node


def delete(node, x):
    if node is not None:
        if x == node.data:
            if node.left is None and node.right is None:
                return None
            elif node.left is None:
                node = rotate_left(node)
            elif node.right is None:
                node = rotate_right(node)
            else:
                if node.left.priority < node.right.priority:
                    node = rotate_right(node)
                else:
                    node = rotate_left(node)
            node = delete(node, x)
            update(node)
        elif x < node.data:
            node.left = delete(node.left, x)
            update(node)
        else:
            node.right = delete(node.right, x)
            update(node)
    return node


def search(node, x):
    while node is not None:
        if x == node.data:
            return True
        elif x < node.data:
            node = node.left
        else:
            node = node.right
    return False


def traverse(node):
    if node is not None:
        for x in traverse(node.left):
            yield x
        yield node.data
        for x in traverse(node.right):
            yield x


class Treap:
    def __init__(self):
        self.root = None

    def insert(self, x):
        self.root = insert(self.root, x)

    def delete(self, x):
        self.root = delete(self.root, x)

    def search(self, x):
        return search(self.root, x)

    def __getitem__(self, ind):
        node = self.root
        ni = node.left.count if node.left else 0
        while ni != ind:
            if ni > ind:
                node = node.left
                ni -= node.right.count + 1 if node.right else 1
            else:
                node = node.right
                ni += node.left.count + 1 if node.left else 1
        return node.data

    def __str__(self):
        if self.root is None:
            return "Treap()"
        buff = "Treap("
        for x in traverse(self.root):
            buff += "%s, " % x
        buff = buff.rstrip(",  ")
        buff += ")"
        return buff
