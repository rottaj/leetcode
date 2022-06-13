##  Brute Force
class BruteForce:
  def twoSum(self, nums, target):
    for i in range(len(nums)):
      for j in range(len(nums)):
        if i != j:
          if nums[i]+nums[j] == target:
            return i, j


class Hashmap:
  def twoSum(self, nums, target):
    hashmap = {}
    for i in range(len(nums)):
      hashmap[nums[i]] = i
    print(hashmap)
    for i in range(len(nums)):
      temp = target - nums[i]
      if temp in hashmap and hashmap[temp] != i:
        return hashmap[temp], i

if __name__ == '__main__':
  nums = [2,7,11,15]
  target = 9

  print("NUMS: ", nums)
  #nums = [3,2,4]
  #target = 6

  #nums = [3,3]
  #target = 6

  #x, x1 = BruteForece().twoSum(nums, target)
  #print(x, x1)

  x, x1 = Hashmap().twoSum(nums, target)
  print(x, x1)
