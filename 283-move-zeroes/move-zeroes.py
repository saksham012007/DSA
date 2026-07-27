class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        r = 0
        w = 0
        while r < len(nums):
            if nums[r] != 0:
                nums[r],nums[w]=nums[w],nums[r]
                r += 1
                w += 1
            else:
                r += 1    