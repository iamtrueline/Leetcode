class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        arr = nums1+nums2
        arr.sort()

        if (len(arr)) % 2 == 0: #even
            m = len(arr)//2
            return (float(arr[m])+arr[m-1])/2
        else: #odd
            return arr[len(arr)//2]