class Solution(object):
    
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        if len(s) == 0:
            return 0
        
        al = {}
        left = 0
        ans = 1
        
        for i in range(len(s)):
            if s[i] in al and left <= al[s[i]]:
                left = al[s[i]]+1
                ans = max(ans, i-left+1)
            else:
                ans = max(ans, i-left+1)
            al[s[i]] = i
        return ans