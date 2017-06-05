from tqdm import *

def gcd(a,b):
	if b == 0: return a
	else: return gcd(b, a%b)

def main():
	lim = 1500000
	sums = dict()
	for n in tqdm(range(1, int((lim/2)**.5))):
		nsq = n**2
		if nsq > lim/2: 
			break
		for m in range(n+1, lim/2):
			c = m**2 + nsq
			if c > lim/2: 
				break
			a = m**2 - n**2
			b = 2*m*n
			f = gcd(a,gcd(b,c))
			if f != 1: continue
			p = a+b+c
			k = 1
			while p*k < lim:
				if p*k not in sums:
					sums[p*k] = 1
				else:
					sums[p*k] += 1
				k += 1

	result = 0
	sumlst = []
	for key in sorted(sums.iterkeys()):
		if sums[key] == 1:
			result += 1
	print result

main()