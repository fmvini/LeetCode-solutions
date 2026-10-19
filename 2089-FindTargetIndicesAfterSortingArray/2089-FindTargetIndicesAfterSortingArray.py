# Last updated: 18/10/2026, 21:51:04
1class Solution:
2    def targetIndices(self, nums: list[int], target: int) -> list[int]:
3        nums.sort()
4        result =[]
5
6        for i, num in enumerate(nums):
7            if num == target:
8                result.append(i)
9
10        return result