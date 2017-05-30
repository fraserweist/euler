from math import *
import time

def gcd(a,b):
  if b == 0: return a
  else: return gcd(b, a % b)

def period(n):
  if sqrt(n) % 1 == 0:
    return 0
  a = int(sqrt(n))
  add, coeff, denom = a, 1, n-a**2
  lst = []
  while (add,coeff,denom) not in lst:
    lst.append((add,coeff,denom))
    a = int(coeff*(sqrt(n)+add)/denom)
    add -= a * denom / coeff
    coeff = denom
    denom = n - add**2
    add /= -1
    f = gcd(coeff,denom)
    if f != 1:
      coeff /= f
      denom /= f
  return len(lst)

def main():
  limit = 10000
  count = 0
  for i in range(2,limit+1):
    if period(i) % 2 == 1:
      count += 1

  print count

main()