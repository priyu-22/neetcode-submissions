class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxHeight = 0
        l, r = 0, len(heights)-1

        while l < r:
            dist = r-l
            if heights[l] < heights[r]:
                h = heights[l] * dist
                l+=1
            else:
                h = heights[r] * dist
                r-=1
            maxHeight = max(maxHeight, h)
        return maxHeight
                