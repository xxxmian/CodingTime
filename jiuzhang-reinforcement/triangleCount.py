"""
Description: Given an array of intergers, choose three of them to form a triangle.
how many different triangles can be formed.
"""
def trangleCount(nums):
    list.sort(nums)
    sum = 0
    for i in range(2, len(nums)):
        lo, hi = 0, i-1
        while lo < hi:
            while lo < hi and nums[lo] + nums[hi] <= nums[i]:
                lo += 1
            sum += hi - lo
            hi -= 1
    return sum
print(trangleCount([0,1,2,3,4]))