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
    ni = node.left.count if node.left else 0
    while node is not None:
        if x == node.data:
            return ni
        elif x < node.data:
            node = node.left
            if node is None:
                return -1
            ni -= node.right.count + 1 if node.right else 1
        else:
            node = node.right
            if node is None:
                return -1
            ni += node.left.count + 1 if node.left else 1
    return -1


def traverse(node):
    if node is not None:
        for x in traverse(node.left):
            yield x
        yield node.data
        for x in traverse(node.right):
            yield x


class Treap:
    def __init__(self, l=[]):
        # 初期化したいリストを与えるとO(N log N)で初期化してくれます
        self.root = None
        if l:
            for i in l:
                self.insert(i)

    def insert(self, x):
        # xを挿入します O(logN)
        self.root = insert(self.root, x)

    def delete(self, x):
        # xが存在する場合、xを削除します O(logN)
        self.root = delete(self.root, x)

    def index(self, x):
        # xが存在するならそのindexを、存在しないなら-1を返します O(logN)
        return search(self.root, x)

    def __contains__(self, x):
        # xが存在するかを t in x で判定できます
        return search(self.root, x) != -1

    def __getitem__(self, ind):
        # t[index]で配列のindex番目に大きい要素にアクセスできます O(logN)
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
        # Treapをリスト形式で返します O(N)
        if self.root is None:
            return "Treap()"
        buff = "Treap("
        for x in traverse(self.root):
            buff += "%s, " % x
        buff = buff.rstrip(",  ")
        buff += ")"
        return buff
