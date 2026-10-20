# Last updated: 19/10/2026, 23:14:57
1
2class Solution:
3    def removeDuplicates(self, nums: list[int]) -> int:
4        k = 1
5
6        for i in range(1, len(nums)):
7            if nums[i] != nums[k - 1]:
8                nums[k] = nums[i]
9                k += 1
10
11        return k
12