class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        left_range = {}
        right_range = {}

        left_range[0] = 0
        right_range[len(heights)-1] = 0 

        stack = []
        for i in range(len(heights)):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            left_range[i] = i - (stack[-1] if stack else -1) - 1
            stack.append(i)

        stack = []
        for i in range(len(heights) - 1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            right_range[i] = (stack[-1] if stack else len(heights)) - i - 1
            stack.append(i)
            
        max_size = 0
        for i in range(len(heights)):
            size = heights[i] * (left_range[i] + right_range[i] + 1)
            max_size = max(size, max_size)

        return max_size            




            
            

        