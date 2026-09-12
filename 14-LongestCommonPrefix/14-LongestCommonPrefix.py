# Last updated: 11/09/2026, 23:27:16
1class Solution:
2    def longestCommonPrefix(self, strs: list[str]) -> str:
3        prefix = strs[0]
4
5        for word in strs[1:]:
6            while not word.startswith(prefix):
7                prefix = prefix[:-1]
8
9                if prefix == "":
10                    return ""
11
12        return prefix