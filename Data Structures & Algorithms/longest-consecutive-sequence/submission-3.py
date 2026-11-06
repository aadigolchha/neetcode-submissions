class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if nums == []:
            return 0

        unq = set()
        
        for num in nums:
            unq.add(int(num))

        max_len = 1

        leng = 1
        for n in nums:
            if n - 1 not in unq:
                leng = 1
                while n + leng in unq:
                    leng += 1
                max_len = max(leng, max_len)

        
        return max_len
        




            
        