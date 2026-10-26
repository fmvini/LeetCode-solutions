# Last updated: 25/10/2026, 22:51:12
1class Solution:
2    def mySqrt(self, x: int) -> int:
3        left, right = 0, x
4
5        while left <= right:
6            mid = (left + right) // 2
7
8            if mid * mid == x:
9                return mid
10            elif mid * mid < x:
11                left = mid + 1
12            else:
13                right = mid - 1
14
15        return right