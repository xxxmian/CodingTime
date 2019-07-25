class HashHeap:

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
            if self.heap[father] < self.heap[index]:
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
            if self.heap[minimum] > self.heap[index]:
                return
            self._swap(minimum, index)
            index = minimum


class Solution:
    """
    @param nums: A list of integers
    @param k: An integer
    @return: The median of the element inside the window at each moving
    """

    def medianSlidingWindow(self, nums, k):
        # write your code here
        if not nums or k > len(nums):
            return []
        if k == 1:
            return nums
        leftMaxHeap = HashHeap()
        rightMinHeap = HashHeap()
        ans = []
        mid = nums[0]

        def addTo(i, mid):
            if nums[i] < mid:
                leftMaxHeap.add(-nums[i])
                if leftMaxHeap.totals > rightMinHeap.totals:
                    rightMinHeap.add(mid)
                    mid = -leftMaxHeap.pop()
            else:
                rightMinHeap.add(nums[i])
                if rightMinHeap.totals > leftMaxHeap.totals + 1:
                    leftMaxHeap.add(-mid)
                    mid = rightMinHeap.pop()
            return mid

        def removeFrom(i, mid):
            if nums[i] == mid:
                if rightMinHeap.totals == leftMaxHeap.totals:
                    mid = -leftMaxHeap.pop()
                else:
                    mid = rightMinHeap.pop()
            elif -nums[i] in leftMaxHeap.hash:
                leftMaxHeap.remove(-nums[i])
                if leftMaxHeap.totals < rightMinHeap.totals - 1:
                    leftMaxHeap.add(-mid)
                    mid = rightMinHeap.pop()
            elif nums[i] in rightMinHeap.hash:
                rightMinHeap.remove(nums[i])
                if rightMinHeap.totals < leftMaxHeap.totals:
                    rightMinHeap.add(mid)
                    mid = -leftMaxHeap.pop()
            return mid

        for i in range(1, k):
            mid = addTo(i, mid)
        ans.append(mid)
        for i in range(k, len(nums)):
            mid = removeFrom(i - k, mid)
            mid = addTo(i, mid)
            ans.append(mid)
        return ans


