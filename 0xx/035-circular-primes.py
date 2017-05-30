def primes(n):
  sieve = [True] * n
  for i in xrange(3,int(n**0.5)+1,2):
    if sieve[i]:
      sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
  return [2] + [i for i in xrange(3,n,2) if sieve[i]]

def circs(n):
  array = primes(n)
  circs = []
  for p in array:
    for c in str(p):
      if int(c) % 2 == 0:
        continue
    if p in circs:
      continue
    s = str(p)
    l = len(s)
    perms = [int(s)]
    for i in range(l-1):
      s = s[1:]+s[0]
      if int(s) not in array:
        perms = []
        break
      perms.append(int(s))
    circs.extend(perms)
  return circs

def main():
  limit = 1000000
  sol = circs(limit)
  print sol

main()