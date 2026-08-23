# Watching a range shrink. No searching yet, just the mechanic.

low = 0
high = 9
print("Range: positions", low, "to", high)

mid = (low + high) // 2
print("Middle position:", mid)

# Pretend the thing I want is to the right of mid.
# So everything from low up to and including mid is useless. Throw it away.

low = mid + 1
print("Range: position", low, "to", high)

mid = (low + high) // 2
print("Middle position:", mid)

# Pretend the thing I want is to the left of mid this time.
# So everything from mid up to high is useless. Throw it away.

high = mid - 1
print("Range: positions", low, "to", high)

print("---")

# How many times can I halve 10000 before I'm down to 1?
size = 10000
halvings = 0

while size > 1:
    size = size // 2
    halvings += 1

print("Halvings needed for 10000 items:", halvings)