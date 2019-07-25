"""
class Comparator:
    def cmp(self, a, b)
You can use Compare.cmp(a, b) to compare nuts "a" and bolts "b",
if "a" is bigger than "b", it will return 1, else if they are equal,
it will return 0, else if "a" is smaller than "b", it will return -1.
When "a" is not a nut or "b" is not a bolt, it will return 2, which is not valid.
"""

import random
class Solution:
    # @param nuts: a list of integers
    # @param bolts: a list of integers
    # @param compare: a instance of Comparator
    # @return: nothing
    def partition(self, array, cmp, pivot, left, right):
        l, r = left, right
        for i in range(l,r+1):
            if cmp(array[i], pivot)==0 or cmp(pivot, array[i])==0:
                array[i], array[l] = array[l], array[i]
                record = array[l]
                break
        while l<r:
            while l<r and (cmp(array[r], pivot)==1 or cmp(pivot, array[r])==-1):
                r-=1
            array[l] = array[r]
            while l<r and (cmp(array[l], pivot)==-1 or cmp(pivot, array[l])==1):
                l+=1
            array[r] = array[l]
        array[l] = record
        return l
    def quick_sort(self, nuts, bolts, start, end, cmp):
        if start>=end:
            return
        pos = random.randint(start, end)
        pos = self.partition(bolts, cmp, nuts[pos], start, end)
        self.partition(nuts, cmp, bolts[pos], start, end)
        self.quick_sort(nuts,bolts,start,pos-1,cmp)
        self.quick_sort(nuts,bolts,pos+1,end,cmp)

    def sortNutsAndBolts(self, nuts, bolts, compare):
        # write your code here
        self.quick_sort(nuts,bolts,0,len(nuts)-1,compare.cmp)


