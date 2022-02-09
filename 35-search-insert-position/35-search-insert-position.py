class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target in nums:
            return (nums.index(target))
        else:
            i = 0
            for n in nums:
                if n > target:
                    return i
                i = i + 1
            return i