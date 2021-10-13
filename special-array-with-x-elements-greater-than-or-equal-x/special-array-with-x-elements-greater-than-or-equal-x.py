from bisect import bisect_left, bisect_right

class Solution(object):
    def specialArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s, m = 0, len(nums)
        nums.sort()
        tall = nums[-1]
        
        for i in range(tall+1):
            s = bisect_left(nums, i)
            if m-s == i:
                ans = i
                return i
        return -1
            