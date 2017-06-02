from math import *
from tqdm import *

def integral(xy,z):
	c2 = (xy)**2 + z**2
	sol = int(sqrt(c2))
	return sol**2 == c2

def main():
	m = 3
	target = 1000000
	solution = 0
	lst = []
	ctr = 0
	while True:
		for xy in range(3,2*m+1):
			if integral(xy,m):
				if xy <= m:
					ctr += xy / 2
				else:
					ctr += m - (xy+1)/2 + 1
		if ctr > target:
			solution = m
			break
		m += 1
	print solution

main()