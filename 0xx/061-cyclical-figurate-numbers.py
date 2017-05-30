from math import *
from tqdm import *

def tri_num(n):
	return n*(n+1)/2

def sq_num(n):
	return n*n

def pent_num(n):
	return n*(3*n-1)/2

def hex_num(n):
	return n*(2*n-1)

def hept_num(n):
	return n*(5*n-3)/2

def oct_num(n):
	return n*(3*n-2)

def tri_idx(x):
	return ceil((sqrt(8*x+1.)-1)/2.)

def sq_idx(x):
	return ceil(sqrt(x))

def pent_idx(x):
	return ceil((sqrt(24*x+1.)+1.)/6.)

def hex_idx(x):
	return ceil((sqrt(8*x+1.)+1.)/4.)

def hept_idx(x):
	return ceil((sqrt(40*x+9.)+3.)/10.)

def oct_idx(x):
	return ceil((sqrt(3*x+1.)+1.)/3.)

def main():
	tris = []
	sqs = []
	pents = []
	hexs = []
	hepts = []
	octs = []
	trictr = tri_idx(1000)
	while True:
		next_tri = int(tri_num(trictr))
		if next_tri >= 10000:
			break
		tris.append(next_tri)
		trictr += 1

	sqctr = sq_idx(1000)
	while True:
		next_sq = int(sq_num(sqctr))
		if next_sq >= 10000:
			break
		sqs.append(next_sq)
		sqctr += 1

	pentctr = pent_idx(1000)
	while True:
		next_pent = int(pent_num(pentctr))
		if next_pent >= 10000:
			break
		pents.append(next_pent)
		pentctr += 1

	hexctr = hex_idx(1000)
	while True:
		next_hex = int(hex_num(hexctr))
		if next_hex >= 10000:
			break
		hexs.append(next_hex)
		hexctr += 1

	heptctr = hept_idx(1000)
	while True:
		next_hept = int(hept_num(heptctr))
		if next_hept >= 10000:
			break
		hepts.append(next_hept)
		heptctr += 1

	octctr = oct_idx(1000)
	while True:
		next_oct = int(oct_num(octctr))
		if next_oct >= 10000:
			break
		octs.append(next_oct)
		octctr += 1

	nums = [tris, sqs, pents, hexs, hepts, octs]

	for o in range(len(octs)):
		sol = [0, 0, 0, 0, 0, octs[o]]

		def find_next(last, length):
			for i in range(len(sol)):
				if sol[i] != 0: continue
				for j in range(len(nums[i])):
					unique = True
					for k in range(len(sol)):
						if sol[k] == nums[i][j]:
							unique = False
							break
					if unique and (sol[last] % 100 == nums[i][j] / 100):
						sol[i] = nums[i][j]
						if length == 5:
							if sol[5] / 100 == sol[i] % 100: return True
						if find_next(i, length + 1): return True
				sol[i] = 0
			return False

		res = find_next(5, 1)
		if res:
			print sol, sum(sol)
			break

main()