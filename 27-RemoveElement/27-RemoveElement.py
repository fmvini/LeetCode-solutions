# Last updated: 20/10/2026, 23:23:39
1class Solution:
2    def removeElement(self, nums: list[int], val: int) -> int:
3        k = 0
4
5        for num in nums:
6            if num != val:
7                nums[k] = num
8                k += 1
9
10        return k