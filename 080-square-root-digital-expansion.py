from math import *

def sq_digits(n):
  c = n
  p = 0
  x, y = 0, 0
  lim = 100
  digits = []
  while len(digits) < lim:
    for i in range(10):
      if i*(20*p+i) <= c and (i+1)*(20*p+i+1) > c:
        x = i
        break
    y = x*(20*p+x)
    digits.append(x)
    c -= y
    c *= 100
    p = int(''.join(map(str, digits)))
  return sum(digits)

def main():
  result = 0
  for i in range(1,100):
    if sqrt(i) % 1 != 0:
      result += sq_digits(i)
  print result

main()