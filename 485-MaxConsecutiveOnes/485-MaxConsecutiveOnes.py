# Last updated: 23/08/2026, 21:35:54
1class Solution:
2    def findMaxConsecutiveOnes(self, nums):
3        max_ones = 0
4        current_ones = 0
5
6        for num in nums:
7            if num == 1:
8                current_ones += 1
9                max_ones = max(max_ones, current_ones)
10            else:
11                current_ones = 0
12
13        return max_ones