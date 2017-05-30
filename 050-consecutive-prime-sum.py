def primes(n):
  sieve = [True] * n
  for i in xrange(3,int(n**.5)+1,2):
    if sieve[i]:
      sieve[i*i::2*i] = [False]*((n-i*i-1)/(2*i)+1)
  return [2] + [i for i in xrange(3,n,2) if sieve[i]]

def main():
  limit = 1000000
  ps = primes(limit)
  cum_sum = [0,2]
  for i in range(len(ps)-1):
    cum_sum.append(cum_sum[-1]+ps[i+1])
  max_cons = 0
  max_p = 0
  print "about to find consecutive sums..."
  for i in range(len(ps)):
    for j in range(i+1-max_cons)[::-1]:
      if cum_sum[i] > limit: break
      cur_sum = cum_sum[i] - cum_sum[j]
      if cur_sum > limit: break
      if cur_sum not in ps: continue
      if i - j > max_cons:
        max_cons = i - j
        max_p = cur_sum
  print max_cons, max_p



main()