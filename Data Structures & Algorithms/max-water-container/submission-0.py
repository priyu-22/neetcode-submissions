class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right, max_water = 0, len(heights)-1, 0
        while left < right:
            area = min(heights[left], heights[right]) * (right-left)
            max_water = max(max_water, area)
            if heights[left] < heights[right]:
                left+=1
            else:
                right-=1
        return max_water