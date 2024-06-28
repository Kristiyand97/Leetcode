class Solution(object):
    def truncateSentence(self, s, k):
        words = s.split()
        new_string = []
        counter = k

        for i in range(len(words)):
            new_string.append(words[i])
            counter -= 1
            if counter == 0:
                return " ".join(new_string)