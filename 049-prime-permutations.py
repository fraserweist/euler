from itertools import *

def is_perm(n, m):
  sn, sm = str(n), str(m)
  if len(sn) != len(sm):
    return False
  arrn = [0] * 10
  arrm = [0] * 10
  for i in range(len(sn)):
    arrn[int(sn[i])] += 1
    arrm[int(sm[i])] += 1
  return arrn == arrm


def primes(n):
  sieve = [True] * n
  for i in xrange(3,int(n**0.5)+1,2):
    if sieve[i]:
      sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
  return [2] + [i for i in xrange(3,n,2) if sieve[i]]

def main():
  limit = 10000
  ps = primes(10000)
  ps = [p for p in ps if p > 1487]
  for i in range(len(ps)):
    for j in range(i+1,len(ps)):
      k = ps[j] + (ps[j] - ps[i])
      if k in ps and k < limit:
        if is_perm(ps[i], ps[j]) and is_perm(ps[i], k):
          result = str(ps[i])+str(ps[j])+str(k)
          print result
          return

main()