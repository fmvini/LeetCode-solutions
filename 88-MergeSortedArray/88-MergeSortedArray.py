# Last updated: 28/10/2026, 23:02:23
1class Solution:
2    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
3        i = m - 1
4        j = n - 1
5        k = m + n - 1
6
7        while j >= 0:
8            if i >= 0 and nums1[i] > nums2[j]:
9                nums1[k] = nums1[i]
10                i -= 1
11            else:
12                nums1[k] = nums2[j]
13                j -= 1
14
15            k -= 1