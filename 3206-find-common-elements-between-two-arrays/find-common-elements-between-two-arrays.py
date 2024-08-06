class Solution(object):
    def findIntersectionValues(self, nums1, nums2):
        result = []
        counter = 0
        for i in range(len(nums1)):
            if nums1[i] in nums2:
                counter += 1
        result.append(counter)
        
        counter = 0

        for j in range(len(nums2)):
            if nums2[j] in nums1:
                counter += 1
        result.append(counter)

        return result