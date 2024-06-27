class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        new_string = "".join(word1)
        second_string = "".join(word2)

        if new_string == second_string:
            return True
        else:
            return False
        