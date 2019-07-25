class Solution:
    """
    @param heights: a matrix of integers
    @return: an integer
    """
    def trapRainWater(self, heights):
        n, m = len(heights), len(heights[0])
        vol = 0
        flag = True
        dir = [[-1, 0], [1, 0], [0,-1], [0, 1]]
        def lianTong1(i,j):
            for d in range(4):
                if i+dir[d][0]>=0 and j+dir[d][1]>=0 and i+dir[d][0]<n and j+dir[d][1]<m and heights[i+dir[d][0]][j+dir[d][1]] == 0:
                    heights[i+dir[d][0]][j+dir[d][1]] = -1
                    lianTong(i+dir[d][0], j+dir[d][1])
        def lianTong2(i,j):
            f=True
            while f:
                f=False
                for d in range(4):
                    if i + dir[d][0] >= 0 and j + dir[d][1] >= 0 and i + dir[d][0] < n and j + dir[d][1] < m and \
                            heights[i + dir[d][0]][j + dir[d][1]] == 0:
                        heights[i + dir[d][0]][j + dir[d][1]] = -1
                        lianTong(i + dir[d][0], j + dir[d][1])

        def isQiang(i,j):
            if i==0 or j==0 or i==n-1 or j == m-1 or heights[i-1][j] == -1 or heights[i+1][j] == -1 or heights[i][j-1] == -1 or heights[i][j+1] == -1:
                return True
            return False
        while flag:
            flag = False
            for i in range(n):
                for j in range(m):
                    if isQiang(i, j) and heights[i][j] == 0:
                            heights[i][j] = -1
                            lianTong(i, j)
            for i in range(n):
                for j in range(m):
                    if heights[i][j] == -1: continue
                    if heights[i][j] == 0: vol += 1
                    else: heights[i][j] -= 1
                    flag = True
        return vol
