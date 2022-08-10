class Solution:
  def longestPalindrome(self, s):
    print(s) 
    x = list(s)
    x.reverse()
    x = ''.join(x)
    print(s, x)
    if x == s:
      return str(x)
    elif x[:-1] == s:
      return str(x[:-1])
    elif x[1:] == s:
      return str(x[1:])
    else:
      s = ''.join(list(s)[1:-1])
      return self.longestPalindrome(s)
     

if __name__ == "__main__":
  s = "babad"
  #s = "cbbd"
  x = Solution().longestPalindrome(s)
  print("ANS", x)
