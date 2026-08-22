# Last updated: 22/08/2026, 18:13:49
1class Solution:
2    def shuffle(self, nums: List[int], n: int) -> List[int]:
3        result = []
4        for i in range(n):
5            result.append(nums[i])
6            result.append(nums[i + n])
7        return result