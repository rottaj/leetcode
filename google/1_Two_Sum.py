
class BruteForce:  # O(n^2)
  def twoSum(self, nums, target):
    for i in range(len(nums)):
      for j in range(len(nums)):
        if nums[i]+nums[j] == target and i != j:
          return [i,j]


class SlidingWindow: # O(n)
  def twoSum(self, nums, target):
    hMap = {}
    nums.sort()
    for i in range(len(nums)):
      hMap[nums[i]] = i

    print(hMap)
    i, j = 0, len(nums)-1
    while i <= j:
      if nums[i] + nums[j] == target:
        return [hMap[nums[i]], hMap[nums[j]]]
      if nums[i] + nums[j] > target:
        j-=1
      else:
        i+=1


if __name__ == "__main__":
  
  '''
  nums = [3,3]
  target = 6

  nums = [3,2,4]
  target = 6

  nums = [3,2,4]
  target = 6

  '''
  nums = [2,7,11,15]
  target = 9


  x = SlidingWindow().twoSum(nums, target)
  print(x)
  



  '''

  x = BruteForce().twoSum(nums, target)
  print("ANS: ", x)
  '''
