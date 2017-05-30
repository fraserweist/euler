from math import *

def gcd(a,b):
  if not b: return a
  else: return gcd(b, a % b)

def is_prime(n):
  if n is 1: return False
  if n is 2: return True
  if n % 2 == 0: return False
  for i in range(3,int(sqrt(n))+1,2):
    if n % i == 0:
      return False
  return True

def primes(n):
  sieve = [True]*n
  for i in range(3,int(sqrt(n))+1,2):
    if sieve[i]:
      sieve[i*i::2*i] = [False]*((n-i*i-1)/(2*i)+1)
  return [2] + [x for x in range(3,n,2) if sieve[x]]

def main():
  ps = primes(200)
  limit = 1000000
  res = 1
  i = 0
  while res*ps[i] < limit:
    res *= ps[i]
    i += 1
  print res

main()