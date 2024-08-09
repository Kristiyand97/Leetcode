class Solution(object):
    def findDifference(self, nums1, nums2):

        nums1 = set(nums1)
        nums2 = set(nums2)

        result_1 = []
        result_2 = []

        for num in nums1:
            if num not in nums2:
                result_1.append(num)

        for num in nums2:
            if num not in nums1:
                result_2.append(num)

        return [result_1, result_2]
