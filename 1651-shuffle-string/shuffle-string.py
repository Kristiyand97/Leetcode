class Solution(object):
    def restoreString(self, s, indices):

        result = [""] * len(s)

        for i, index in enumerate(indices):
            result[index] = s[i]

        return "".join(result)


