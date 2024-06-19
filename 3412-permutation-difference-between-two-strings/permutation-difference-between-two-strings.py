class Solution(object):
    def findPermutationDifference(self, s, t):
        total = 0

        for i in range(len(s)):
            for j in range(len(t)):
                if s[i] == t[j]:
                    sum = abs(i - j)
                    total += sum
        return total