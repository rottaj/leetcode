def reverse(x):
  xList = list(str(x))
  i = len(xList)-1;
  out = []
  while i >=0:
    out.append(xList[i])
    i-=1

  print(''.join(out))
x = -123
reverse(x)
