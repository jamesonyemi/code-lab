"""
3Sum
Level: Medium

Given an integer array nums, return all 
unique triplets [nums[i], nums[j], nums[k]] 
such that i != j != k and nums[i] + nums[j] + nums[k] == 0. 
The solution set must not contain duplicate triplets.

Example:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: The unique triplets that sum to zero are [-1,

"""

def triplets_with_sum_0(nums: list[int]) -> list[list[int]]:
	nums.sort()
	n = len(nums)
	results = []

	for i in range(n - 2):

		if i > 0 and nums[i] == nums[ i + 1]:
			continue

		left  = i + 1
		right = n - 1

		while left < right:
			total = nums[i]	+ nums[left] + nums[right]
			if total == 0:
				results.append([nums[i], nums[left], nums[right]])

				left  += 1
				right -= 1

			    while left < right and nums[left] == nums[left - 1]:
				   left += 1
			    while left < right and nums[right] == nums[right + 1]:
				   right -= 1	
            elif total < 0:
            	left += 1
            else:
            	right -= 1


    return results
