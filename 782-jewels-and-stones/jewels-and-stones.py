class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        unique_stones = {}
        total = 0
        
        for s in stones:
            if s in jewels:
                if s not in unique_stones:
                    unique_stones[s] = 1
                else:
                    unique_stones[s] += 1
                    
        for stone in unique_stones:
            total += unique_stones[stone]

        return total