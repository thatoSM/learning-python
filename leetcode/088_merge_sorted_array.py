"""
LeetCode #88 - Merge Sorted Array (Easy)

Problem:
    I get two sorted lists, nums1 and nums2. nums1 has extra empty slots
    (zeros) at the end, exactly enough to hold all of nums2. I must merge
    nums2 into nums1 so the final nums1 is one sorted list. No return
    value - nums1 is modified in place.

Examples:
    nums1=[1,2,3,0,0,0], m=3, nums2=[2,5,6], n=3   ->   [1,2,2,3,5,6]
    nums1=[1], m=1, nums2=[], n=0                   ->   [1]
    nums1=[0], m=0, nums2=[1], n=1                  ->   [1]

Constraints:
    nums1.length == m + n, nums2.length == n, 0 <= m, n <= 200

Approach:
    Copy each element of nums2 into nums1's empty slots using index
    assignment (nums1[m + i] = nums2[i]), then sort nums1 in place
    with .sort(). The empty slots start at index m, so offsetting by
    m places each nums2 element exactly where a zero was.

What I learned:
    - nums1[i] = value REPLACES at a position; .append() ADDS a new
      element at the end - different tools for different jobs
    - .sort() sorts a list in place and returns None
    - "In place" means modifying the given list, not building a new one

Pattern: Index assignment + in-place sort
Time complexity: O((m+n) log(m+n)) - the sort dominates the copy loop
Space complexity: O(1) - modified in place, no new list created
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