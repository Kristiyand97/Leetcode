class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        words = text.split(" ")
        counter = 0

        broken_set = set(brokenLetters)

        for word in words:
            checker = True
            for w in broken_set:
                if w in word:
                    checker = False
                    break
            if checker:
                counter += 1

        return counter


