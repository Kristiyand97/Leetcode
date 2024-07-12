class Solution(object):
    def maxProductDifference(self, nums):
        sorted_nums = sorted(nums)
        result = 0

        for i in range(len(sorted_nums)):
            difference = abs((sorted_nums[0] * sorted_nums[1]) - (sorted_nums[-1] * sorted_nums[-2]))
            result += difference
            break

        return result

        