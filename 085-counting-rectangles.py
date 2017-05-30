from math import *

def count(n,m):
  result = 0
  for i in range(1,n+1):
    for j in range(1,m+1):
      result += i*j
  return result

def main():
  limit = 10000
  start = 0
  res = 0
  for i in range(1,limit+1):
    c = count(i,i)
    if c > 2000000:
      start = i
      res = c
      break
  i, j = start, start
  while abs(res) > 3:
    if res > 0:
      i -= 1
    elif res < 0:
      j += 1
    res = count(i,j) - 2000000
  print i*j

main()