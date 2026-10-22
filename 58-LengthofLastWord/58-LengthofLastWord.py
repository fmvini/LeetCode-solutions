# Last updated: 21/10/2026, 23:34:45
1class Solution:
2    def lengthOfLastWord(self, s: str) -> int:
3        return len(s.strip().split()[-1])