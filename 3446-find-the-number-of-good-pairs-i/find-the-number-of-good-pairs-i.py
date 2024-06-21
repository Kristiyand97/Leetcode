class Solution(object):
    def numberOfPairs(self, nums1, nums2, k):
        counter = 0

        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums2[j] * k != 0 and nums1[i] % (nums2[j] * k) == 0:
                    counter += 1

        return counter
        