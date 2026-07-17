"""
LeetCode #88 - Merge Sorted Array (Easy)

Problem (in my words):
    >>> WRITE 2-3 sentences in your own words.

Examples:
    nums1=[1,2,3,0,0,0], m=3, nums2=[2,5,6], n=3   ->   [1,2,2,3,5,6]
    nums1=[1], m=1, nums2=[], n=0                   ->   [1]
    nums1=[0], m=0, nums2=[1], n=1                  ->   [1]

Constraints:
    nums1.length == m + n, nums2.length == n, 0 <= m, n <= 200

Pattern: Copy into empty slots + sort
Time complexity: O((m+n) log(m+n)) - the sort dominates
Space complexity: O(1) - modified in place
"""
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        for i in range(n):
            nums1[m + i] = nums2[i]
        nums1.sort()


# Local test
nums1 = [1, 2, 3, 0, 0, 0]
Solution().merge(nums1, 3, [2, 5, 6], 3)
print(nums1)  # Expected: [1, 2, 2, 3, 5, 6]

nums1 = [1]
Solution().merge(nums1, 1, [], 0)
print(nums1)  # Expected: [1]

nums1 = [0]
Solution().merge(nums1, 0, [1], 1)
print(nums1)  # Expected: [1]