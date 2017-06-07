from math import *
from tqdm import tqdm

def main():
	limit = 1000000000
	mlim = int((limit/2)**.5)
	res = 0

	for n in tqdm(range(1,mlim+1)):
		for m in range(n+1,mlim+1):
			a = m**2 - n**2
			b = 2*m*n
			c = m**2 + n**2
			base = 2*(min(a,b))
			if base + 2*c > limit:
				break
			if abs(c - base) > 1:
				continue
			else:
				res += 2*c+base
	print res

main()