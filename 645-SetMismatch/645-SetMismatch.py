# Last updated: 27/08/2026, 14:43:56
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        repeated = -1
        missing = -1
        
        for n in nums:
            if nums.count(n)>1:
                repeated = n
                break
                

        for i in range(len(nums)+1):
            if i+1 not in nums:
                missing= i+1
                break
        return [repeated,missing]
        

