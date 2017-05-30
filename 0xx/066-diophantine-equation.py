from math import *

def gcd(a, b):
  if b == 0: return a
  else: return gcd(b, a % b)

def conv(n, k):
  if sqrt(n) % 1 == 0:
    return 0
  a = int(sqrt(n))
  a0 = a
  num, den = a, 1
  add, coeff, denom = a, 1, n-a**2
  lst = []
  for _ in range(k):
    lst.append([num, den])
    a = int(coeff*(sqrt(n)+add)/denom)
    add -= a * denom / coeff
    coeff = denom
    denom = n - add**2
    add /= -1
    if len(lst) == 1:
      num = a0*a + 1
      den = a
    else:
      num = a*lst[-1][0] + lst[-2][0]
      den = a*lst[-1][1] + lst[-2][1]
    f = gcd(coeff,denom)
    if f != 1:
      coeff /= f
      denom /= f
  return lst[-1]

def main():
  sols = [0] * 1000
  for i in range(2, 1000):
    if sqrt(i) % 1 == 0: continue
    ctr = 1
    while True:
      ans = conv(i, ctr)
      if ans[0]**2 - i*ans[1]**2 == 1:
        sols[i] = ans[0]
        break
      ctr += 1
  print max(sols), sols.index(max(sols))

main()