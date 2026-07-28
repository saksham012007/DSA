class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        r = 0
        w = 0
        while r < len(nums):
            if nums[r] != val:
                nums[w],nums[r]=nums[r],nums[w]
                r += 1
                w += 1
            else:
                r += 1
        return w            
       