# Last updated: 24/10/2026, 23:58:58
1
2class Solution:
3    def threeSumClosest(self, nums: List[int], target: int) -> int:
4        nums.sort()
5        closest = nums[0] + nums[1] + nums[2]
6
7        for i in range(len(nums) - 2):
8            left = i + 1
9            right = len(nums) - 1
10
11            while left < right:
12                total = nums[i] + nums[left] + nums[right]
13
14                if abs(total - target) < abs(closest - target):
15                    closest = total
16
17                if total == target:
18                    return total
19                elif total < target:
20                    left += 1
21                else:
22                    right -= 1
23
24        return closest
25