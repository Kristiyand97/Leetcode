class Solution(object):
    def uniqueMorseRepresentations(self, words):

        unique_words = {}

        code = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---",
                ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]

        for word in words:
            new_word = ""
            for w in word:
                letter = ord(w) - ord("a")
                for i in range(len(code)):
                    if letter == i:
                        new_word += code[i]
                        break
            if new_word not in unique_words:
                unique_words[new_word] = 1
            else:
                unique_words[new_word] += 1

        result = len([key for key in unique_words.keys()])

        return result
