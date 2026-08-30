# Last updated: 30/08/2026, 19:07:48
1class Solution:
2    def twoSum(self, nums, target):
3        vistos = {}
4
5        for i, num in enumerate(nums):
6            complemento = target - num
7
8            if complemento in vistos:
9                return [vistos[complemento], i]
10
11            vistos[num] = i