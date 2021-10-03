class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        ans = 0
        for c in operations:
            if c[1] == "+":
                ans += 1
            else:
                ans -= 1
        return ans
        