# Last updated: 29/08/2026, 18:59:34
1class Solution:
2    def smallerNumbersThanCurrent(self, nums):
3        sorted_nums = sorted(nums)
4
5        count = {}
6
7        for i, num in enumerate(sorted_nums):
8            if num not in count:
9                count[num] = i
10
11        return [count[num] for num in nums]