class Solution:
  def myAtoi(self, string):
    temp, isNeg = [], False
    print(string)
    for i in list(string):
      if i.isnumeric():
        print(i)
        temp.append(i)
      elif i == '-':
        isNeg = True
    if isNeg is True:
      return int(''.join(temp)) * -1
    else:
      return int(''.join(temp))
        
     


if __name__ == '__main__':
  s = "-42 is the number"
  ans = Solution().myAtoi(s)
  print(ans)
  
