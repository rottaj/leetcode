class BruteForce:
  def longestSubstring(self, s):
    curr, longest = [], "" # create map if contains: --> reset
    for i in list(s):
      print("CURR", curr)
      if i in curr:
        if len(curr) > len(list(longest)):
          longest = ''.join(curr)
        curr = []
        curr.append(i)
      else:
        curr.append(i)
    print(curr, longest)
    if len(curr) > len(longest):
      return len(''.join(curr))
    else: return len(longest)



class Solution:
  def longestSubstring(self, s):
    print(s) 


if __name__ == '__main__':
  #s = "abcabcbb" 
  #s = "bbbbbb"
  #s = "pwwkew"
  #s = "au"
  #s = " "
  s = "dvdf"
  sol = BruteForce().longestSubstring(s)
  print(sol)
