class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        w = 0
        r  = 0
        while r < len(nums):
            if nums[r] == nums[w]:
                r += 1
            else:
                nums[w+1] = nums[r]
                r += 1
                w += 1
        return w+1           
        