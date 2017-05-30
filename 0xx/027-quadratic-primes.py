from math import *

def is_prime(n):
  limit = int(sqrt(n))
  for i in range(2, limit+1):
    if n % i == 0:
      return 0
  return 1

def main():
  lim = 1000
  max_a, max_b, max_n = 0, 0, 0
  for a in range(-lim + 1, lim):
    for b in range(0, lim + 1):
      if not is_prime(b):
        continue
      n = 0
      result = b
      while result > 0:
        if not is_prime(result):
          break
        n += 1
        result = n**2 + a*n + b
      if n > max_n:
        max_a, max_b, max_n = a, b, n

  print max_a, max_b, max_n
  for i in range(max_n):
    print i**2 + max_a*i + max_b
  print max_a * max_b

main()