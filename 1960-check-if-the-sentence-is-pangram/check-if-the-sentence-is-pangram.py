class Solution(object):
    def checkIfPangram(self, sentence):
        alphabet = "abcdefghijklmnopqrstuvwxyz"

        for l in alphabet:
            if l not in sentence:
                return False
        return True
        