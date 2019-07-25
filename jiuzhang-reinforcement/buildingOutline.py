class HashHeapMax:

    def __init__(self):
        self.heap = []
        self.hash = {}

    def size(self):
        return len(self.heap)

    def empty(self):
        return True if self.size() == 0 else False

    def top(self):
        return self.heap[0][0]

    def haskey(self,key):
        return key in self.hash

    def add(self, key,value):
        self.heap.append([key,value])
        self.hash[key] = self.size() - 1
        self._siftup(self.size() - 1)

    def pop(self):
        assert self.size() > 0
        self._swap(0, self.size() - 1)
        del self.hash[self.heap[-1][0]]
        p = self.heap.pop(-1)
        self._siftdown(0)
        return p[0]

    def remove(self, value):
        pos = self.hash.get(value)

        if pos != -1:
            self._swap(pos, self.size() - 1)
            del self.hash[self.heap[-1][0]]
            self.heap.pop(-1)
            if pos >= self.size():
                return
            if pos == 0:
                self._siftdown(pos)
            else:
                father = (pos - 1) // 2
                if self.heap[pos][0] > self.heap[father][0]:
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
            if self.heap[father][0] >= self.heap[index][0]:
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
                maximum = lchild if self.heap[lchild][0] > self.heap[rchild][0] else rchild
            if self.heap[maximum][0] <= self.heap[index][0]:
                return
            self._swap(maximum, index)
            index = maximum

class Solution:
    """
    @param buildings: A list of lists of integers
    @return: Find the outline of those buildings
    """

    def buildingOutline(self, buildings):
        if not buildings:
            return []
        record = []

        for i,bu in enumerate(buildings):
            record.append([bu[0],bu[2],i])
            record.append([bu[1],bu[2],i])
        record = sorted(record, key=lambda x:(x[0], x[2]), reverse=False)
        hh = HashHeapMax()
        height={}
        for x, h, index in record:
            if hh.haskey(index):
                hh.remove(index)
            else:
                hh.add(h, index)
            height[x] = hh.top()

        temp = []
        lastX, lastY = None, None
        for x in sorted(height.keys()):
            if lastX is not None and lastY != 0:
                temp.append((lastX, x, lastY))
            lastX, lastY = x, height[x]

        results = []
        lastInterval = temp[0]
        for start, end, height in temp[1:]:
            if start == lastInterval[1] and height == lastInterval[2]:
                lastInterval = lastInterval[0], end, height
            else:
                results.append(lastInterval)
                lastInterval = (start, end, height)
        results.append(lastInterval)
        return results


s=Solution()
print(s.buildingOutline([[1,2,3],[2,3,3]]))