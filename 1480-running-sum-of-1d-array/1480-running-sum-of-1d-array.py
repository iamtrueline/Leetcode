class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        li = []
        ans = 0
        for i in nums:
            ans += i
            li.append(ans)
        return li