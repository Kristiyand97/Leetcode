class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        counter = 0

        for i in range(len(items)):
            if ruleKey == "color":
                if ruleValue == items[i][1]:
                    counter += 1
            elif ruleKey == "type":
                if ruleValue == items[i][0]:
                    counter += 1
            elif ruleKey == "name":
                if ruleValue == items[i][2]:
                    counter += 1

        return counter