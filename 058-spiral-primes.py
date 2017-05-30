from math import *

def is_prime(n):
  if n is 1: return False
  if n is 2: return True
  if n % 2 == 0: return False
  for i in range(3,int(sqrt(n))+1,2):
    if n % i == 0:
      return False
  return True

def main():
  sol = 0
  side = 1
  primes = 0
  denom = 1.
  counter = 1
  while True:
    counter = side**2 + 1
    side += 2
    denom += 4
    for i in range(4):
      idx = side-2 + i*(side-1)
      if is_prime(counter + idx):
        primes += 1
    ratio = primes / denom
    if ratio < .1:
      sol = side
      break

  print sol

main()