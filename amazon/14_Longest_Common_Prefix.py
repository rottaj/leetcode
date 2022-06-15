'''
  Steps:
    1.) Get longest string
    3.) Check each string in list by element
'''
class Solution:
  def longestCommonPrefix(self, strs):
    x, prefix = strs[0],""
    for i in strs:
      if len(i) > len(x):
        x = i
    c = 0
    while True:
      res = all(x in s for s in strs)
      if (res):
        print("HELLO", x)
        prefix = x
        break
      else:
        x = x[:-1]
    
    return prefix
 
if __name__ == '__main__':
 #strs = ["flower", "flow", "flight"]
 #strs = ["dog", "racecar", "car"]
 strs = ["a"]
 sol = Solution().longestCommonPrefix(strs)
 print("Sol", sol)
