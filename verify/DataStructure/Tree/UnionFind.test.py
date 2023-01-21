# verification-helper: PROBLEM https://judge.yosupo.jp/problem/unionfind

from DataStructure.Tree.UnionFind import UnionFind
N,Q=map(int,input().split())
uf=UnionFind(N)
for _ in range(Q):
    t,u,v=map(int,input().split())
    if t==0:
        uf.unite(u,v)
    else:
        print(int(uf.same(u,v)))
