class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x > 0:
            ans = int(str(x)[::-1])
        else:
            ans = -1*int(str(x*-1)[::-1])
            
        if ans < -2**31 or ans > 2**31:
            ans = 0
        
        return ans