class Solution(object):
    def minPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tmp = []
        nums = sorted(nums, reverse = True)
        for i in range(len(nums)//2):
            tmp.append(nums[0+i]+nums[-1-i])
        ans = max(tmp)
        return ans