from math import *

def main():
  number = 600851475143
  limit = int(floor(sqrt(number)))
  print "limit = "+str(limit)

  def primes1(n):
    sieve = [True] * (n/2)
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i/2]:
            sieve[i*i/2::i] = [False] * ((n-i*i-1)/(2*i)+1)
    return [2] + [2*i+1 for i in xrange(1,n/2) if sieve[i]]

  primes = primes1(limit)

  result = 1

  for i in primes:
    if number % i == 0:
      result = i

  print "result: "+str(result)


main()