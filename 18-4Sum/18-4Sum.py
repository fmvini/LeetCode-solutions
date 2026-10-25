# Last updated: 24/10/2026, 23:58:30
1class Solution:
2    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
3        nums.sort()
4        result = []
5        n = len(nums)
6
7        for i in range(n - 3):
8            if i > 0 and nums[i] == nums[i - 1]:
9                continue
10
11            for j in range(i + 1, n - 2):
12                if j > i + 1 and nums[j] == nums[j - 1]:
13                    continue
14
15                left = j + 1
16                right = n - 1
17
18                while left < right:
19                    total = nums[i] + nums[j] + nums[left] + nums[right]
20
21                    if total == target:
22                        result.append([
23                            nums[i], nums[j], nums[left], nums[right]
24                        ])
25
26                        left += 1
27                        right -= 1
28
29                        while left < right and nums[left] == nums[left - 1]:
30                            left += 1
31
32                        while left < right and nums[right] == nums[right + 1]:
33                            right -= 1
34
35                    elif total < target:
36                        left += 1
37                    else:
38                        right -= 1
39
40        return result