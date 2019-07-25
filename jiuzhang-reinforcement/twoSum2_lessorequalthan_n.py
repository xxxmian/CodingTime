


"""
the number of pairs which sum are less or equal than n
"""
class Solution:

    def twoSum2(self, nums, n):
        list.sort(nums)
        lo, hi = 0,len(nums)-1
        sum = 0
        while lo < hi:
            while nums[lo] + nums[hi] > n and lo < hi:
                hi -= 1
            sum += hi - lo
            lo += 1
        return sum
s=Solution()
print(s.twoSum2([1,2,3,4,0,5,6,7], 5))