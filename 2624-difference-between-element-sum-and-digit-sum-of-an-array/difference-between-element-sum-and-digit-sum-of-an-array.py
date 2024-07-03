class Solution(object):
    def differenceOfSum(self, nums):
        digits ="".join(str(num) for num in nums)
        digits_sum = 0
        for d in digits:
            digits_sum += int(d)

        return abs(sum(nums) - digits_sum)

        