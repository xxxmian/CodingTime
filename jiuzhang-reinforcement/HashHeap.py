class HashHeapMax:

    def __init__(self):
        self.heap = []
        self.hash = {}
        self.totals = 0

    def size(self):
        return len(self.heap)

    def empty(self):
        return True if self.size() == 0 else False

    def top(self):
        return self.heap[0][0]

    def add(self, item):
        self.totals += 1
        if item in self.hash:
            pos = self.hash.get(item)
            self.heap[pos][1] += 1
            return
        self.heap.append([item, 1])
        self.hash[item] = self.size() - 1
        self._siftup(self.size() - 1)

    def pop(self):
        assert self.size() > 0
        self.totals -= 1
        if self.heap[0][1] > 1:
            self.heap[0][1] -= 1
            return self.heap[0][0]
        self._swap(0, self.size() - 1)
        del self.hash[self.heap[-1][0]]
        p = self.heap.pop(-1)
        self._siftdown(0)
        return p[0]

    def remove(self, value):
        pos = self.hash.get(value)

        if pos != -1:
            self.totals -= 1
            if self.heap[pos][1] > 1:
                self.heap[pos][1] -= 1
                return
            self._swap(pos, self.size() - 1)
            del self.hash[self.heap[-1][0]]
            self.heap.pop(-1)
            if pos >= self.size():
                return
            if pos == 0:
                self._siftdown(pos)
            else:
                father = (pos - 1) // 2
                if self.heap[pos] > self.heap[father]:
                    self._siftup(pos)
                else:
                    self._siftdown(pos)

    def _swap(self, i1, i2):
        self.heap[i1], self.heap[i2] = self.heap[i2], self.heap[i1]
        self.hash[self.heap[i2][0]] = i2
        self.hash[self.heap[i1][0]] = i1

    def _siftup(self, index):
        while index > 0:
            father = (index - 1) // 2
            if self.heap[father] >= self.heap[index]:
                break
            self._swap(father, index)
            index = father

    def _siftdown(self, index):
        while True:
            lchild, rchild = index * 2 + 1, index * 2 + 2
            if lchild >= self.size():
                return
            maximum = lchild
            if rchild < self.size():
                maximum = lchild if self.heap[lchild] > self.heap[rchild] else rchild
            if self.heap[maximum] <= self.heap[index]:
                return
            self._swap(maximum, index)
            index = maximum




class HashHeapMin:

    def __init__(self):
        self.heap = []
        self.hash = {}
        self.totals = 0

    def size(self):
        return len(self.heap)

    def empty(self):
        return True if self.size() == 0 else False

    def top(self):
        return self.heap[0][0]

    def add(self, item):
        self.totals += 1
        if item in self.hash:
            pos = self.hash.get(item)
            self.heap[pos][1] += 1
            return
        self.heap.append([item, 1])
        self.hash[item] = self.size() - 1
        self._siftup(self.size() - 1)

    def pop(self):
        assert self.size() > 0
        self.totals -= 1
        if self.heap[0][1] > 1:
            self.heap[0][1] -= 1
            return self.heap[0][0]
        self._swap(0, self.size() - 1)
        del self.hash[self.heap[-1][0]]
        p = self.heap.pop(-1)
        self._siftdown(0)
        return p[0]

    def remove(self, value):
        pos = self.hash.get(value)

        if pos != -1:
            self.totals -= 1
            if self.heap[pos][1] > 1:
                self.heap[pos][1] -= 1
                return
            self._swap(pos, self.size() - 1)
            del self.hash[self.heap[-1][0]]
            self.heap.pop(-1)
            if pos >= self.size():
                return
            if pos == 0:
                self._siftdown(pos)
            else:
                father = (pos - 1) // 2
                if self.heap[pos] < self.heap[father]:
                    self._siftup(pos)
                else:
                    self._siftdown(pos)

    def _swap(self, i1, i2):
        self.heap[i1], self.heap[i2] = self.heap[i2], self.heap[i1]
        self.hash[self.heap[i2][0]] = i2
        self.hash[self.heap[i1][0]] = i1

    def _siftup(self, index):
        while index > 0:
            father = (index - 1) // 2
            if self.heap[father] <= self.heap[index]:
                break
            self._swap(father, index)
            index = father

    def _siftdown(self, index):
        while True:
            lchild, rchild = index * 2 + 1, index * 2 + 2
            if lchild >= self.size():
                return
            minimum = lchild
            if rchild < self.size():
                minimum = lchild if self.heap[lchild] < self.heap[rchild] else rchild
            if self.heap[minimum] >= self.heap[index]:
                return
            self._swap(minimum, index)
            index = minimum



# The Skyline Problem



class Solution:
    """
    @param buildings: A list of lists of integers
    @return: Find the outline of those buildings
    """

    def buildingOutline(self, buildings):
        if not buildings:
            return []
        hh = HashHeapMax()
        rec = []
        ans = []
        for b in buildings:
            rec.append([b[0], True, b[2]])
            rec.append([b[1], False, b[2]])
        rec = sorted(rec, key=lambda x: x[0], reverse=False)
        sweep = rec[0][0]
        for r in rec:
            if r[1]:  # start
                if not hh.empty() and r[2] > hh.top():
                    ans.append([sweep, r[0], hh.top()])
                    sweep = r[0]
                hh.add(r[2])
            else:  # end
                hh.remove(r[2])
                if hh.empty() or r[2] > hh.top():
                    ans.append([sweep, r[0], r[2]])
                    sweep = r[0]

        return ans

s = Solution()
print(s.buildingOutline([[1,3,3],[2,4,4],[5,6,1]]))