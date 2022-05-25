def isPalindrome(x): # solve w/ out reverse()
  i = len(list(str(x)))-1
  x1 = []
  while i >= 0:
    x1.append(list(str(x))[i]) 
    i-=1
  print(''.join(x1))
  if ''.join(x1) == str(x):
    return True
  else: 
    return False


x = 122
ans = isPalindrome(x)
print(ans)
    
