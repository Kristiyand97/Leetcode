class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        unique_jewels = {}
        counter = 0

        for j in jewels:
            unique_jewels[j] = 0

        for s in stones:
            if s in unique_jewels:
                counter += 1
        return counter
            