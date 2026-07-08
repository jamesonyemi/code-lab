"""
**Fixed Size Sliding Window**

Given an array(list) nums of integers consisted of only non-negative numbers and an integer k, find the maximum/largest sum among  all sub-arrays of length k in nums.  

For example, if nums = [1, 2, 3, 4, 5] and k = 3, 
the sub-arrays of length 3 are [1, 2, 3], [2, 3, 4], and [3, 4, 5]. The sums of these sub-arrays are 6, 9, and 12 respectively. The maximum/largest sum among these is 12.


"""


def sub_array_sum_fixed(nums: list[int], k: int) -> int:
    win_sum = 0
    for i in range(k):
        win_sum += nums[i]
    largest = win_sum
    
    for right in range(k, len(nums)):
        left = right - k
        win_sum -= nums[left]
        win_sum += nums[right]
        largest = max(largest, win_sum)
    return largest        