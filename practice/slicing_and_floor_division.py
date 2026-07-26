"""
Practice: slicing, floor division, and while loops.

1. I practised three tools: slicing, the two kinds of division, and the
   while loop.
2. / outputs a float, while // outputs an integer. // is used for list
   positions because it gives a clean whole number with no decimal, and
   a list position has to be a whole number.
3. letters[4:2] outputs [] because it means "start at 4 and stop before
   2", and a slice only moves forward, so it takes nothing. letters[100:200]
   also outputs [] when the list is too short to reach those positions,
   because a slice returns whatever exists in that range, even if that is
   nothing.
4. (low + high) // 2 finds the middle of the range between low and high,
   so it still works when low is not 0. high // 2 only finds the middle
   when the range starts at 0, so it breaks the moment low moves.
"""

# Block A1 - two kinds of division
print(7 / 2)
print(7 // 2)
print(type(7 / 2))
print(type(7 // 2))

# Block A2 - what // does to a range of numbers
print(9 // 2)
print(10 // 2)
print(11 // 2)
print(1 // 2)
print(0 // 2)

# Block A3 - negative numbers behave differently than you expect
print(-7 // 2)
print(7 % 2)
print(-7 % 2)

# Block A4 - list positions must be whole numbers
letters = ["a", "b", "c", "d", "e"]
print(len(letters))
print(letters[len(letters) // 2])

# Block A5 - why the position must be a whole number type
print(4 / 2)
print(type(4 / 2))
nums = [10, 20, 30, 40]
print(nums[2])

# Block B1 - taking a piece of a list
letters = ["a", "b", "c", "d", "e", "f"]
print(letters[0:3])
print(letters[3:6])
print(letters[:3])
print(letters[3:])
print(letters[:])

# Block B2 - the edges
print(letters[2:2])
print(letters[4:2])
print(letters[0:100])

# Block B3 - counting from the right
print(letters[-1])
print(letters[-2])
print(letters[-3:])
print(letters[:-1])

# Block B4 - step
print(letters[::2])
print(letters[1::2])
print(letters[::-1])

# Block B5 - does slicing change the original?
nums = [1, 2, 3, 4]
part = nums[0:2]
part[0] = 99
print(part)
print(nums)

# Block B6 - strings slice the same way
word = "python"
print(word[0:3])
print(word[2:])
print(word[::-1])

# Block B7 - why some slices come back empty
letters = ["a", "b", "c", "d", "e", "f"]
print(letters[2:6])
print(letters[2:5])
print(letters[2:4])
print(letters[2:3])
print(letters[2:2])
print(letters[2:1])
print(letters[2:0])

# Block B8 - negative positions are a shortcut
letters = ["a", "b", "c", "d", "e", "f"]
print(len(letters))
print(letters[-1], letters[len(letters) - 1])
print(letters[-2], letters[len(letters) - 2])
print(letters[-6], letters[len(letters) - 6])

# Block C1 - finding the middle of a range
letters = ["a", "b", "c", "d", "e", "f", "g"]
low = 0
high = len(letters) - 1
mid = (low + high) // 2
print(low, high, mid)
print(letters[mid])

# Block C2 - same calculation, even number of items
letters = ["a", "b", "c", "d", "e", "f"]
low = 0
high = len(letters) - 1
mid = (low + high) // 2
print(low, high, mid, letters[mid])

# Block C3 - the two halves around mid
letters = ["a", "b", "c", "d", "e", "f", "g"]
mid = (0 + len(letters) - 1) // 2
print(letters[:mid])
print(letters[mid])
print(letters[mid + 1:])

# Block C4 - how many times can you halve a number
n = 1000
steps = 0
while n > 1:
    n = n // 2
    steps += 1
print(steps)

# Block C5 - does low actually matter here
letters = ["a", "b", "c", "d", "e", "f", "g"]
low = 0
high = len(letters) - 1
print((low + high) // 2)
print(high // 2)

# Block C6 - the middle of a piece of the list, not the whole list
letters = ["a", "b", "c", "d", "e", "f", "g"]
low = 4
high = 6
print(letters[(low + high) // 2])
print(letters[high // 2])

# Block C7 - watch the halving happen
n = 1000
steps = 0
while n > 1:
    n = n // 2
    steps += 1
    print(steps, n)
print("total steps:", steps)

# Block D - exercises
#D1
nums = [3, 8, 1, 9, 4, 7, 2, 6]
mid = len(nums) // 2
print(nums[:mid])
print(nums[mid:])

#D2
word = "engineering"
mid = len(word) // 2
print(word[mid])

word = "code"
mid = len(word) // 2
print(word[mid])

#D3
nums = [10, 20, 30, 40, 50, 60]
print(nums[::-2])

#D4
n = 64
count = 0

while n <= 1000:
    n = n * 2
    count += 1
    print(count, n)
print("doublings: ", count)