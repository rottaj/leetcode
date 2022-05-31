class Solution:
  def solve(self, nums, k, c):
    for i in range(len(nums)):
      for j in range(len(nums)):
        if i != j:
          if nums[i] + nums[j] == k:
            c+=1
            for z in sorted([i, j], reverse=True):
              del nums[z]
            return solve(nums, k, c)
    return c
  

if __name__ == '__main__':
  #nums = [3,1,3,4,3]
  nums = [1,2,3,4]
  k = 5
  c = 0
  out = Solution().solve(nums, k, c)
  print("OUT", out)

