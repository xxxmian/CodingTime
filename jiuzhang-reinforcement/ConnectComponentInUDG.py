class UDGNode:
    def __init__(self, name, num):
        self.num = num
        self.name = name
        self.neighbors = None
class UnionFind:
    def __init__(self, num):
        self.num = num
        self.rec = [i for i in range(num)]

    def find(self, a):
        assert a < self.num
        while a != self.rec[a]:
            a = self.rec[a]
        return a

    def union(self, a, b):
        assert a < self.num
        assert b < self.num
        fa = self.find(a)
        fb = self.find(b)
        if fa != fb:
            self.rec[fa] = fb
    def countPlate(self):
        c = 0
        for i in range(self.num):
            if self.rec[i] == i:
                c += 1
        return c

def connectcomponentInUDG(graph):
    uf = UnionFind(len(graph))
    for node in graph:
        if not node.neighbors:
            continue
        for next in node.neighbors:
            uf.union(node.num, next.num)
    return uf.countPlate()




a = UDGNode('A', 0)
b = UDGNode('B', 1)
c = UDGNode('C', 2)
d = UDGNode('D', 3)
e = UDGNode('E', 4)
a.neighbors = [b, d]

c.neighbors = [e]


g = [a,b,c,d,e]
count = connectcomponentInUDG(g)
print(count)
