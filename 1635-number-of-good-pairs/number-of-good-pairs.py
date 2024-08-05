class Solution(object):
    def numIdenticalPairs(self, nums):
        
        counter = 0
        dict_pairs = {}

        for num in nums:
            if num in dict_pairs:
                counter += dict_pairs[num]
                dict_pairs[num] += 1
            else:
                dict_pairs[num] = 1
        return counter