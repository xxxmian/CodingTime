class Node:
    def __init__(self):
        self.isword = False
        self.child = dict()


class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word):
        node = self.root
        for letter in word:
            child = node.child.get(letter)
            if not child:
                child = Node()
                node.child[letter] = child
            node = child
        node.isword = True

    def startsWith(self, word):
        node = self.root
        for letter in word:
            child = node.child.get(letter)
            if not child:
                return False
            node = child
        return True

    def search(self, word):
        node = self.root
        for letter in word:
            child = node.child.get(letter)
            if not child:
                return False
            node = child
        if node.isword:
            return True
        return False


class Solution:
    """
    @param board: A list of lists of character
    @param words: A list of string
    @return: A list of string
    """

    def wordSearchII(self, board, words):
        # write your code here
        if not board or not words:
            return []

        trie = Trie()
        for word in words:
            trie.insert(word)
        n, m = len(board), len(board[0])
        # visited = [[False for j in range(m)] for i in range(n)]
        ans = set()
        visited = set()

        def dfs(x, y, word):
            if trie.search(word):
                ans.add(word)
            for i, j in ([x + 1, y], [x - 1, y], [x, y + 1], [x, y - 1]):
                if i < 0 or j < 0 or i >= n or j >= m or ((i, j) in visited) or not trie.startsWith(word + board[i][j]):
                    continue
                visited.add((i, j))
                dfs(i, j, word + board[i][j])
                visited.remove((i, j))

        for i in range(n):
            for j in range(m):
                visited.add((i, j))
                dfs(i, j, str(board[i][j]))
                visited.remove((i, j))
        return list(ans)


