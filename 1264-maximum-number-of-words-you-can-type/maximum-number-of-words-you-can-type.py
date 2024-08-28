class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        words = text.split(" ")
        counter = 0

        for word in words:
            checker = True
            for w in set(brokenLetters):
                if w in word:
                    checker = False
                    break
            if checker:
                counter += 1

        return counter

