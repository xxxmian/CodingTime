class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @param target: An integer
    @return: return the sum of the three integers, the sum closest target.
    """

    def threeSumClosest(self, numbers, target):
        # write your code here
        list.sort(numbers)
        diff = float('inf')

        for i in range(2, len(numbers)):
            lo, hi = 0, i - 1

            while lo < hi:
                temp = numbers[i] + numbers[lo] + numbers[hi]
                if diff > abs(target - temp):
                    diff = abs(target - temp)
                    ans = temp
                    if diff == 0:
                        return ans

                if numbers[lo] + numbers[hi] < target - numbers[i]:
                    lo += 1
                elif numbers[lo] + numbers[hi] > target - numbers[i]:
                    hi -= 1

        return ans