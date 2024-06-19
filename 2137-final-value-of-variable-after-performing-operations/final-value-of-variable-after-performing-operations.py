class Solution(object):
    def finalValueAfterOperations(self, operations):
        total = 0
        for o in operations:
            if o == "++X" or o == "X++":
                total += 1
            else:
                total -= 1

        return total