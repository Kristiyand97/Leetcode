class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        counter = 0

        for s in stones:
            if s in jewels:
                counter += 1

        return counter

            