class Solution:
  def isPalindrome(self, x):
    if x < 0:
      return False
    if int(''.join(list(str(x))[::-1])) == x:
      return True
    else: return False

if __name__ == '__main__':
  x = 121
  sol = Solution().isPalindrome(x)
  print(sol)
