def primes(n):
  sieve = [True] * n
  for i in xrange(3,int(n**0.5)+1,2):
    if sieve[i]:
      sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
  return [2] + [i for i in xrange(3,n,2) if sieve[i]]

def contains_bad(n):
  l = list(str(n))
  evens = ["0","2","4","5","6","8"]
  for e in evens:
    if e in l:
      return 1
  return 0

def main():
  limit = 1000000
  arr = primes(limit)
  eligible = [x for x in arr if not contains_bad(x) or x < 100]
  truncs = []
  while len(truncs) < 11:
    for p in eligible[4:]:
      s = str(p)
      flag = 1
      for i in range(1,len(str(p))):
        if not (p % (10**i) in arr and p / (10**i) in arr):
          flag = 0
      if flag:
        truncs.append(p)
      if len(truncs) > 10:
        break

  print truncs
  result = 0
  for num in truncs:
    result += num

  print result

main()