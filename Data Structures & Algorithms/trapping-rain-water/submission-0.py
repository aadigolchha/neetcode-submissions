class Solution:
    def trap(self, height: List[int]) -> int:

        max_left = {}
        max_right = {}

        max_l = 0
        for i in range(len(height)):
            max_left[i] = max_l
            max_l = max(height[i], max_l)
        
        max_r = 0
        for i in range(len(height)-1, -1, -1):
            max_right[i] = max_r
            max_r = max(height[i], max_r)
        
        water = 0
        for i in range(len(height)):
            if min(max_left[i], max_right[i]) - height[i] > 0:
                water += (min(max_left[i], max_right[i]) - height[i])

        return water



