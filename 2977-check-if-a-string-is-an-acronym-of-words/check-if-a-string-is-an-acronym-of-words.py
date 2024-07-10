class Solution(object):
    def isAcronym(self, words, s):
        result = ""

        for word in words:
            result += word[0]

        return result == s 
        