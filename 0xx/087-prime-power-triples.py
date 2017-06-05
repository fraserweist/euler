def primes(n):
  sieve = [True] * n
  for i in xrange(3,int(n**.5)+1,2):
    if sieve[i]:
      sieve[i*i::2*i] = [False]*((n-i*i-1)/(2*i)+1)
  return [2] + [i for i in xrange(3,n,2) if sieve[i]]

def main():
  limit = 50000000
  ps = primes(int(limit**.5))
  n = len(ps)
  seen = set()
  for i in range(n):
    c = ps[i]**4
    if c > limit: continue
    for j in range(n):
      b = ps[j]**3
      if b + c > limit: break
      for k in range(n):
        a = ps[k]**2
        if a + b + c > limit: break
        seen.add(a+b+c)
  print len(seen)

main()