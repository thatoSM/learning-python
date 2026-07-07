def merge(nums1, m, nums2, n):
    # Step 1: copy nums2 values into nums1's empty slots
    # The empty slots in nums1 start at index m and end at index m+n-1
    # nums2 has n values total
    for i in range(n):
        # YOUR CODE: put nums2[i] into nums1 at the right position
        if i == 0:
            return nums1.append(nums2[i])
    
    # Step 2: sort nums1 in place
    nums1.sort()


# Test cases
nums1 = [1, 2, 3, 0, 0, 0]
merge(nums1, 3, [2, 5, 6], 3)
print(nums1)  # Expected: [1, 2, 2, 3, 5, 6]

nums1 = [1]
merge(nums1, 1, [], 0)
print(nums1)  # Expected: [1]

nums1 = [0]
merge(nums1, 0, [1], 1)
print(nums1)  # Expected: [1]