class Solution:
    """
    @param n: An integer
    @param nums: An array
    @return: the Kth largest element
    """
    def partition(self, nums, i, left, right):
        pivot = nums[i]
        nums[i] = nums[left]
        l,r=left,right
        while l<r:
            while l<r and nums[r] <= pivot:
                r -= 1
            nums[l] = nums[r]
            while l<r and nums[l] >= pivot:
                l += 1
            nums[r] = nums[l]
        nums[l] = pivot
        return l
    def kthLargestElement(self, k, nums):
        # write your code here
        if not nums or k>len(nums):
            return -1

        import random
        left, right = 0,len(nums)-1
        while True:
            i = random.randint(left, right)
            pos = self.partition(nums, i, left, right)
            if pos == k-1:
                return nums[pos]
            elif pos>k-1:
                right = pos-1
            else:
                left = pos+1

s = Solution()
print(s.kthLargestElement(10,[1,2,3,4,5,6,8,9,10,7]))