# LeetCode #1 — Two Sum (Easy)

# Given a list of numbers and a target, find the two numbers that add up
# to the target and return their positions (indices).

# Example: nums = [2, 7, 11, 15], target = 9
# Answer: [0, 1] because nums[0] + nums[1] = 2 + 7 = 9

# My approach: brute force for each number, check every number after it
# to see if they add up to the target.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        