class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers)-1
        while r > l:
            summ = numbers[l]+numbers[r]
            if summ == target:
                return l+1,r+1
                break
            elif summ < target:
                l += 1
            else:
                r -= 1        