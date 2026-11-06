class Solution:
    def hammingWeight(self, n: int) -> int:
        
        string = str(bin(n))
        string = string[2:]

        nums = [int(string[i]) for i in range(len(string))]

        return sum(nums)