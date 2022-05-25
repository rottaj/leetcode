def longestPalindrome(s):
  x = list(s)
  print(x[::-1], x)
  if x[::-1] == x:
    return s
  else:
    return longestPalindrome(''.join(x[:-1]))



s = "cbbd"
test = longestPalindrome(s)
print(test)
