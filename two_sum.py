class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        s = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in s:
                return [s[complement], i]
            s[num] = i

        return []    
