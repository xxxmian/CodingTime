class Node:
    def __init__(self):
        self.isword = False
        self.child = dict()


class WordDictionary:
    """
    @param: word: Adds a word into the data structure.
    @return: nothing
    """

    def __init__(self):
        self.root = Node()

    def addWord(self, word):
        # write your code here

        node = self.root
        for letter in word:
            child = node.child.get(letter)
            if not child:
                child = Node()
                node.child[letter] = child
            node = child
        node.isword = True

    """
    @param: word: A word could contain the dot character '.' to represent any one letter.
    @return: if the word is in the data structure.
    """

    def search(self, word):
        # write your code here
        def find(start, myroot):
            if start == len(word):
                return True
            if not myroot:
                return False
            node = myroot
            for i in range(start, len(word)):
                if word[i] == '.':
                    for key in node.child:
                        if find(i + 1, node.child[key]):
                            return True
                    return False

                child = node.child.get(word[i])
                if not child:
                    return False
                node = child
            if node.isword:
                return True
            return False

        return find(0, self.root)
s=WordDictionary()

s.addWord("a")
print(s.search("."))