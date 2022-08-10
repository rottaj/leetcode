class Solution:
  def reverse(self, x):
    x = list(str(x))
    x.reverse()
    x = ''.join(x)
    if "-" in x:
      x = x[:-1]
      x = int(x)*-1
    return int(x)
    
if __name__ == "__main__":
  #x = 123 
  #x = -123
  x = 120
  a = Solution().reverse(x)
  print("ANS", a)
