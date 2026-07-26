class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        total = 0
        ans = []
        for i in nums:
            total += i
            ans.append(total)
        return ans