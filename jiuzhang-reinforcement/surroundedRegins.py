class Solution:
    """
    @param: board: board a 2D board containing 'X' and 'O'
    @return: nothing
    """

    def surroundedRegions(self, board):
        # write your code here
        if not board:
            return []
        n, m = len(board), len(board[0])
        newboard = [['X' for j in range(m)] for _ in range(n)]
        visited = [[False for j in range(m)] for _ in range(n)]

        def findConnect(i, j):
            for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if x < 0 or y < 0 or x >= n or y >= m or board[x][y] == 'X' or visited[x][y]:
                    continue
                newboard[x][y] = 'O'
                visited[x][y] = True
                findConnect(x, y)

        for i in range(n):
            if board[i][0] == 'O':
                visited[i][0] = True
                newboard[i][0] = 'O'
                findConnect(i, 0)
            if board[i][m - 1] == 'O':
                visited[i][m - 1] = True
                newboard[i][m - 1] = 'O'
                findConnect(i, m - 1)
        for j in range(1, m - 1):
            if board[0][j] == 'O':
                newboard[0][j] = 'O'
                visited[0][j] = True
                findConnect(0, j)
            if board[n - 1][j] == 'O':
                newboard[n - 1][j] = 'O'
                visited[n - 1][j] = True
                findConnect(n - 1, j)
        for i in range(n):
            for j in range(m):
                board[i][j] = newboard[i][j]












