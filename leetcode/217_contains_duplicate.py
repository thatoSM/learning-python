"""
LeetCode #217 - Contains Duplicate (Easy)

Problem (in my words):
    Given an array of integers, return True if any value appears at
    least twice in the array. Return False if every element is unique.

Examples:
    [1, 2, 3, 1]                       ->  True
    [1, 2, 3, 4]                       ->  False
    [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]     ->  True

Constraints:
    1 <= len(nums) <= 100,000
    Numbers can be very large or very negative

Approach:
    Single pass with a set ("seen" tracker).
    1. Start with an empty set.
    2. For each number, check if it's already in the set.
       - If yes -> we've seen it before -> duplicate exists -> return True.
       - If no -> add it to the set, continue.
    3. If the loop finishes without finding a repeat -> return False.

What I learned:
    - Sets are unordered collections with no duplicates allowed
    - Create empty set with set() (NOT {} which makes a dict)
    - Add to a set with .add(item)
    - Check membership with `if item in my_set`
    - Sets check membership in near-constant time, regardless of size
      (lists check in linear time, which is much slower for big inputs)
    - The "have I seen this?" pattern: seen = set() + loop + check + add
    - Returning early from inside a loop ends the function immediately

Pattern: hash set (membership tracking)
Time complexity: O(n) - one pass through nums, set ops are O(1)
Space complexity: O(n) - in worst case, every element ends up in set
"""
def containsDuplicate(nums):
    seen = set()

    for n in nums:
        if n in seen:
            return True     
        else:
            seen.add(n)

    return False            

print(containsDuplicate([1, 2, 3, 1]))                   # Expected: True
print(containsDuplicate([1, 2, 3, 4]))                   # Expected: False
print(containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2])) # Expected: True    