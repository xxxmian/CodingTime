class Solution:

    def minimumSize(self, nums, s):
        # write your code here
        if not nums:
            return -1
        sum = 0
        minlen = float('inf')
        find = False
        r = 0
        for l in range(len(nums)):
            while r < len(nums) and sum < s:
                sum += nums[r]
                r += 1
            if sum >= s:
                find = True
                if r - l < minlen:
                    minlen = r - l
            sum -= nums[l]
        return minlen if find else -1
