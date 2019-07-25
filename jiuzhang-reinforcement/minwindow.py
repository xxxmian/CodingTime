class Solution:
    """
    @param source : A string
    @param target: A string
    @return: A string denote the minimum window, return "" if there is no such a string
    """

    def minWindow(self, source, target):
        # write your code here
        if not source or not target:
            return ""

        targetHash = {}
        for t in target:
            targetHash[t] = targetHash.get(t, 0) + 1
        newhash = {}
        distinct = len(targetHash)
        already = 0
        r = 0
        minlen = len(source) + 1
        minstring = ""

        for l in range(len(source)):
            while r < len(source) and already < distinct:
                if source[r] in targetHash:
                    newhash[source[r]] = newhash.get(source[r], 0) + 1
                    if newhash[source[r]] == targetHash[source[r]]:
                        already += 1
                r += 1
            if already == distinct and minlen > r - l:
                minlen = r - l
                minstring = source[l:r]
            if source[l] in targetHash:
                if targetHash[source[l]] == newhash[source[l]]:
                    already -= 1
                newhash[source[l]] -= 1
        return minstring




