class Solution: 
  def maxArea(self, height):
    longest, left, right = 0, 0, len(height)-1

    if len(height) == 2:
      if height[0] > height[1]:
        return height[1]
      else: return height[0]
    while left < right:
      temp = 0
      while height[left] != 0 or height[right] != 0:
        print(height[left], height[right])
        if height[left] == height[right]:
          temp = height[right] * (right - left)
          left+=1
        else:
          if height[left] < height[right]: 
            left +=1
          else:
            right -=1
          if height[right] < height[left]:
            temp = height[right] * (right - left)
          else:
            temp = height[left] * (right - left)
        if temp > longest: longest = temp
        return longest
          

          

          
if __name__ == '__main__':
  height = [1,8,6,2,5,4,8,3,7]
  #height = [1,1]
  #height = [4,3,2,1,4]
  #height = [1,2]
  #height = [1,2,4,3]
  #height = [1,0,0,0,0,0,2,2]
  sol = Solution().maxArea(height)
  print(sol)
