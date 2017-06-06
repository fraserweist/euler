def primes(n):
  sieve = [True] * n
  for i in xrange(3,int(n**.5)+1,2):
    if sieve[i]:
      sieve[i*i::2*i] = [False]*((n-i*i-1)/(2*i)+1)
  return [2] + [i for i in xrange(3,n,2) if sieve[i]]

def factor(n):
	num = n
	ps = primes(int(num/2))
	fs = []
	for i in range(len(ps)):
		while num % ps[i] == 0:
			num /= ps[i]
			fs.append(ps[i])
	return fs

def main():
	limit = 12
	ps = primes(limit/2)
	mins = [0]*(limit+1)
	mins[0] = 1
	mins[1] = 1
	ctr = 4
	for k in range(2,limit+1):
		while mins[k] == 0:
			fs = factor(ctr)

main()