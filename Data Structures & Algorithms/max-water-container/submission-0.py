class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i,j = 0, len(heights)-1
        area = 0

        while i < j:
            new_area = min(heights[i],heights[j]) * (j-i)
            if new_area > area:
                area = new_area
            if heights[i] < heights[j]:
                i+=1
            else:
                j-=1
        return area

