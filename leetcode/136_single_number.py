"""
LeetCode #136 - Single Number (Easy)

You're given an array of integers. Every number appears exactly twice, except for one number which appears only once. Find that single number.
Examples
Input:  [2, 2, 1]
Output: 1
Explanation: 1 is the only number that doesn't have a pair.

Input:  [4, 1, 2, 1, 2]
Output: 4
Explanation: 1 and 2 both appear twice. 4 appears once.

Input:  [1]
Output: 1
Explanation: There's only one number, so it's the single one.
Constraints

1 <= length of nums <= 30,000
Every element appears exactly twice except for one element which appears once
The array always has at least one element

Approach:
    Use a set as a "pairing tracker." Walk through nums once.
    For each number, if it's already in the set, remove it
    (we found its pair). If it's not, add it. The number that
    has no pair will be the only one left in the set at the end.
"""
class Solution:
    def singleNumber(self, nums):
        seen = set()

        for n in nums:
            if n in seen:
                seen.remove(n)
            else:
                seen.add(n)
        return seen.pop()


print(Solution().singleNumber([2, 2, 1]))           # Expected: 1
print(Solution().singleNumber([4, 1, 2, 1, 2]))     # Expected: 4
print(Solution().singleNumber([1]))                 # Expected: 1