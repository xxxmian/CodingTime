def validTree(n, edges):
    # write your code here
    if not edges or len(edges) != n - 1:
        return False

    def find(uf, a):
        while a != uf[a]:
            a = uf[a]
        return a

    def union(uf, a, b):
        fa = find(a)
        fb = find(b)
        if fa != fb:
            uf[fa] = fb

    uf = [i for i in range(n)]
    for edge in edges:
        union(uf, edge[0], edge[1])

    res = 0
    for i in range(n):
        if uf[i] == i:
            res += 1
    if res != 1:
        return False
    return True
print(validTree(5,[[0,1],[0,2],[0,3],[1,4]]))