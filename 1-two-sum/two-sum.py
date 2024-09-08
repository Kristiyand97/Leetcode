class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        numbers = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in numbers:
                return [numbers[complement], i]
            else:
                numbers[num] = i





        