class Solution:
  def lengthOfLongestSubstring(self, s):
    hMap = {} 
    for i in range(len(s)): # Populate hash map
      if s[i] in hMap:
         hMap[s[i]].append(i)     
      else:
        hMap[s[i]] = [i]
    print(hMap) 
    t = list(hMap.values())
    longest = []
    for arr in t: # get longest distance ( repeating char )
      print(arr)
      for i in range(len(arr)-1): 
        print(range(arr[i], arr[i+1])) 
        if len(range(arr[i], arr[i+1])) > len(longest):
          print(arr[i], arr[i+1])
          longest = s[arr[i]:arr[i+1]]

    return longest 
    

    
if __name__ == "__main__":
  #s = "abcabcbb"
  #s = "bbbbb"
  s = "pwwkew"
  x = Solution().lengthOfLongestSubstring(s)
  print(x)
