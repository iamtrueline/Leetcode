class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs == [""]:
            return ""
        elif len(strs) == 1:
            return strs[0]
        
        strs = sorted(strs, key=len)
        for i in range(len(strs[0])):
            for j in range(1,len(strs)):
                if strs[0][i] != strs[j][i]:
                    return strs[0][0:i]
        
        return strs[0]