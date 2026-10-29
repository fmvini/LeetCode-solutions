# Last updated: 29/10/2026, 15:55:59
1class Solution:
2    def climbStairs(self, n: int) -> int:
3        if n <= 2:
4            return n
5
6        a, b = 1, 2
7
8        for i in range(3, n + 1):
9            a, b = b, a + b
10
11        return b