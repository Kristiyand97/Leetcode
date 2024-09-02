class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        dict_numbers = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in dict_numbers:
                return [dict_numbers[complement], i]
            dict_numbers[num] = i


        