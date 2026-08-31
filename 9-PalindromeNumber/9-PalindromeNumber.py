# Last updated: 31/08/2026, 15:53:24
1class Solution:
2    def isPalindrome(self, x: int) -> bool:
3        if x < 0:
4            return False
5
6        original = x
7        reversed_num = 0
8
9        while x > 0:
10            reversed_num = reversed_num * 10 + x % 10
11            x //= 10
12
13        return original == reversed_num