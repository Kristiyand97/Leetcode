class Solution(object):
    def missingNumber(self, nums):
        all_numbers = {}

        for num in nums:
            all_numbers[num] = True

        for i in range(len(nums) + 1):
            if i not in all_numbers:
                return i
        