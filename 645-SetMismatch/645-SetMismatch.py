# Last updated: 27/08/2026, 14:43:24
1class Solution:
2    def findErrorNums(self, nums):
3        n = len(nums)
4        count = [0] * (n + 1)
5
6        for num in nums:
7            count[num] += 1
8
9        duplicate = missing = 0
10
11        for i in range(1, n + 1):
12            if count[i] == 2:
13                duplicate = i
14            elif count[i] == 0:
15                missing = i
16
17        return [duplicate, missing]