class Solution(object):
    def scoreOfString(self, s):
        total = 0

        for i in range(len(s) - 1):
            value = abs(ord(s[i]) - ord(s[i + 1]))
            total += value

        
        return total
        