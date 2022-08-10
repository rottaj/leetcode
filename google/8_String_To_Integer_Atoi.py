class Solution:
  def myAtoi(self, s):
    listS, new = list(s), []
    for i in listS: # convert string to number ( try )
      try:
        new.append(str(int(i))) 
      except: None
    new = int(''.join(new))
    if "-" in s:
      new = new *-1
    return new


if __name__ == "__main__":
  #s = "42"
  #s = "   -42"
  #s = "4193 with words"
  x = Solution().myAtoi(s)
  print("ANS", x)
