class Solution(object):
    def findDifference(self, nums1, nums2):
        result_1 = []
        result_2 = []
        for i in range(len(nums1)):
            if nums1[i] in result_1:
                continue
            if nums1[i] not in nums2:
                result_1.append(nums1[i])

        for i in range(len(nums2)):
            if nums2[i] in result_2:
                continue
            if nums2[i] not in nums1:
                result_2.append(nums2[i])

        return [result_1, result_2]