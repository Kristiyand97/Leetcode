class Solution(object):
    def decompressRLElist(self, nums):
        result = []
        for i in range(0, len(nums) - 1, 2):

            while nums[i] > 0:
                result.append(nums[i + 1])
                nums[i] -= 1
        return result
        