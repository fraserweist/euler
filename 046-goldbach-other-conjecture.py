from math import *

def primes(n):
  sieve = [True] * n
  for i in xrange(3,int(n**0.5)+1,2):
    if sieve[i]:
      sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
  return [2] + [i for i in xrange(3,n,2) if sieve[i]]

def odd_composites(n):
  prime = primes(n)
  return [x for x in range(n) if x not in prime and x % 2 != 0]

def main():
  limit = 10000
  comp = odd_composites(limit)[1:]
  ps = primes(limit)
  squares = [n*n*2 for n in range(int(sqrt(limit)))][1:]
  for c in comp:
    flag = 0
    for p in ps:
      for s in squares:
        if p + s == c:
          flag = 1
          break
      if flag: break
    if not flag:
      print c
      break


main()