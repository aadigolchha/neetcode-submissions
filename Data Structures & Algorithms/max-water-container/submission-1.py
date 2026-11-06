class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        l = 0
        r = len(heights) - 1

        max = (r - l) * min(heights[l], heights[r])
        
        while l < r:

            if min(heights[l+1], heights[r]) * (r - (l+1)) > max:
                max =  min(heights[l+1], heights[r]) * (r - (l+1))
                l += 1
                continue
            if min(heights[l], heights[r-1]) * (r-1-l) > max:
                max = min(heights[l], heights[r-1]) * (r-1-l)
                r -= 1
                continue
            
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
                
            
        return max

             





            