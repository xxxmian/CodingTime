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


class Solution:
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """

    def numIslands(self, grid):
        # write your code here
        if not grid:
            return 0
        n, m = len(grid), len(grid[0])
        uf = UnionFind(n * m)
        water = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    water += 1
                    continue
                for x, y in [(i + 1, j), (i, j + 1)]:
                    if x >= n or y >= m or grid[x][y] == 0:
                        continue
                    uf.union(i * m + j, x * m + y)
        return uf.countPlate() - water


input = [[1,0,0,1,1,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0],[1,0,0,1,1,0,0,1,0,0,0,1,0,1,0,1,0,0,1,0],[0,0,0,1,1,1,1,0,1,0,1,1,0,0,0,0,1,0,1,0],[0,0,0,1,1,0,0,1,0,0,0,1,1,1,0,0,1,0,0,1],[0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0],[1,0,0,0,0,1,0,1,0,1,1,0,0,0,0,0,0,1,0,1],[0,0,0,1,0,0,0,1,0,1,0,1,0,1,0,1,0,1,0,1],[0,0,0,1,0,1,0,0,1,1,0,1,0,1,1,0,1,1,1,0],[0,0,0,0,1,0,0,1,1,0,0,0,0,1,0,0,0,1,0,1],[0,0,1,0,0,1,0,0,0,0,0,1,0,0,1,0,0,0,1,0],[1,0,0,1,0,0,0,0,0,0,0,1,0,0,1,0,1,0,1,0],[0,1,0,0,0,1,0,1,0,1,1,0,1,1,1,0,1,1,0,0],[1,1,0,1,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,1],[0,1,0,0,1,1,1,0,0,0,1,1,1,1,1,0,1,0,0,0],[0,0,1,1,1,0,0,0,1,1,0,0,0,1,0,1,0,0,0,0],[1,0,0,1,0,1,0,0,0,0,1,0,0,0,1,0,1,0,1,1],[1,0,1,0,0,0,0,0,0,1,0,0,0,1,0,1,0,0,0,0],[0,1,1,0,0,0,1,1,1,0,1,0,1,0,1,1,1,1,0,0],[0,1,0,0,0,0,1,1,0,0,1,0,1,0,0,1,0,0,1,1],[0,0,0,0,0,0,1,1,1,1,0,1,0,0,0,1,1,0,0,0]]
s=Solution()
print(s.numIslands(input))
