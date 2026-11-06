from collections import defaultdict
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        counts = defaultdict(lambda: defaultdict(int))
        counts[0][nums[0]] += 1
        counts[0][-nums[0]] += 1

        for i in range(1, len(nums)):
            pos = nums[i]
            neg = -nums[i]
            for key in counts[i-1]:
                counts[i][key+pos] += counts[i-1][key]
                counts[i][key+neg] += counts[i-1][key]

        return counts[len(nums)-1][target]