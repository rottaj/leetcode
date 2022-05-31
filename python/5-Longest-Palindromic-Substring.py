
class Solution:

  def longestPalindrome(self, s):
    x = list(s)
    print(x[::-1], x)
    if x[::-1] == x:
      return s
    else:
      return longestPalindrome(''.join(x[:-1]))


if __name__ == '__main__':
  s = "cbbd"
  test = Solution().longestPalindrome(s)
  print(test)
