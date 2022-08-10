class Solution:
  def isPalindrome(self, x):
    x1 = list(str(x))
    x1.reverse()
    if str(x) == str(''.join(x1)):
      return True
    else:
      return False


if __name__ == "__main__":
  #x = 121
  #x = -121
  x = 10
  a = Solution().isPalindrome(x)
  print("ANS", a)
