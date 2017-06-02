from tqdm import *

def primes(n):
  sieve = [True]*n
  for i in range(3,int(n**.5)+1,2):
    if sieve[i]:
      sieve[i*i::2*i] = [False]*((n-i*i-1)/(2*i)+1)
  return [2] + [x for x in range(3,n,2) if sieve[x]]

def is_permutation(n1, n2):
	s1, s2 = str(n1), str(n2)
	if len(s1) != len(s2): return False

	lst1 = [s1[i] for i in range(len(s1))]
	lst2 = [s2[i] for i in range(len(s2))]
	return sorted(lst1) == sorted(lst2)

def main():
	limit = 10000000
	plst = primes(limit)
	tot = range(limit)
	for p in plst:
		tot[p] = p - 1
		num = 2*p
		while num < limit:
			tot[num] *= p-1
			tot[num] /= p
			num += p
	print "got totient array"
	sol = 10000000.
	soli = 0
	for i in range(2, limit):
		cur = (i+0.)/tot[i]
		if cur < sol:
			if is_permutation(i, tot[i]):
				sol = cur
				soli = i
	print sol, soli


main()