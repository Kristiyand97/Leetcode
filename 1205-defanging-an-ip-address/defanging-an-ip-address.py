class Solution(object):
    def defangIPaddr(self, address):
        result = ""
        for a in address:
            if a == ".":
                result += "[.]"
            else:
                result += a
        return result
        