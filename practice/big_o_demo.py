def linear_search(nums, target):
    steps = 0
    for i, value in enumerate(nums):
        steps = steps + 1
        if value == target:
            print("Found at position", i, "after", steps, "steps")
            return i
    print("Not found after", steps, "steps")
    return -1

small = list(range(10))
medium = list(range(100))
big = list(range(1000))
huge = list(range(10000))

print("Searching for the LAST item in each list:")
linear_search(small, 9)
linear_search(medium, 99)
linear_search(big, 999)
linear_search(huge, 9999)