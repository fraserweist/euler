def is_pandigital(n):
  s = str(n)
  digits = set()
  for c in s:
    digits.add(int(c))
  for i in range(2,10):
    if digits == set(range(1,i+1)) and len(s) == i:
      return 1
  return 0

def primes(n):
  sieve = [True] * n
  for i in xrange(3,int(n**0.5)+1,2):
    if sieve[i]:
      sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
  return [2] + [i for i in xrange(3,n,2) if sieve[i]]

def main():
  arr = primes(10000000)
  print "got the primes..."
  arr = arr[::-1]
  ans = 0
  for num in arr:
    if is_pandigital(num):
      ans = num
      break
  print ans

main()