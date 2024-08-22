class Solution(object):
    def uniqueOccurrences(self, arr):
        unique_occur = {}

        for num in arr:
            if num in unique_occur:
                unique_occur[num] += 1
            else:
                unique_occur[num] = 1

        unique_numbers = set()

        for value in unique_occur.values():
            unique_numbers.add(value)

        return len(unique_numbers) == len(unique_occur)