# Last updated: 23/10/2026, 01:14:22
1
2class Solution:
3    def plusOne(self, digits: list[int]) -> list[int]:
4        for i in range(len(digits) - 1, -1, -1):
5            if digits[i] < 9:
6                digits[i] += 1
7                return digits
8
9            digits[i] = 0
10
11        return [1] + digits
12