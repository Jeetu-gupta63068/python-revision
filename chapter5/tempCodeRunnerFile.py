i = 0
while i < len(nums):
    if nums[i] == x:
        print("Found at index", i)
        break
    else:
        print("Finding...")
    i += 1