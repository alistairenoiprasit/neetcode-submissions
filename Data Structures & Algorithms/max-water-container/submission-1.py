class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0 
        r = len(heights) - 1
        vol = 0
        while l != r:
            if heights[l] < heights[r]:
               # l is smaller
               vol = max(vol, (r - l) * heights[l]) 
               l += 1
            elif heights[l] > heights[r]: # r is smaller
                vol = max(vol, (r - l) * heights[r])
                r -= 1
            else: # equal
                vol = max(vol, (r - l) * heights[l])
                l += 1
            
        return vol