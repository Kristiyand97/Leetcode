class Solution(object):
    def sumOfUnique(self, nums):
        unique_nums = {}
        for n in nums:
            if n not in unique_nums:
                unique_nums[n] = 1
            else:
                unique_nums[n] += 1

        result = sum(key for key, value in unique_nums.items() if value == 1)

        return result