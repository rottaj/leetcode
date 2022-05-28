def missingNumber(nums):
  largest, smallest = nums[0], nums[0]
  for i in nums: # could just use sorted list to determine smallest and largest.. :hackerman:
    if i > largest:
      largest = i
    if i < smallest:
      smallest = i
  tempRange = list(range(smallest, largest+1))
  nums.sort()
  for idx, x in enumerate(tempRange):
    if tempRange[idx] != nums[idx]:
      return tempRange[idx]

nums = [3,0,1]
#nums = [0, 1]
#nums = [9,6,4,2,3,5,7,0,1]
ans = missingNumber(nums)
print("ANSWER", ans)
