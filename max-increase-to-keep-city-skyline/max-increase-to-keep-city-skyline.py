class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ans = 0
        revgrid = list(map(list, zip(*grid)))
        rowmax = []
        colmax = []
        
        for h in grid:
            rowmax.append(max(h))
        for h in revgrid:
            colmax.append(max(h))
            
        for i, arr in enumerate(grid):
            for j, h in enumerate(arr):
                tmp = min(rowmax[i], colmax[j])
                if h < tmp:
                    ans += tmp - h
        return ans
        