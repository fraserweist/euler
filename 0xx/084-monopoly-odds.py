import heapq

GO = 0
JAIL = 10
C1 = 11
E3 = 24
H2 = 39
R1 = 5
R2 = 15
R3 = 25
R4 = 35
U1 = 12
U2 = 28
G2J = 30

CC1 = 2
CC2 = 17
CC3 = 33

CH1 = 7
CH2 = 22
CH3 = 36

def cc(pos, n):
	res = [0]*40
	res[pos] = n*14./16.
	res[GO] = n*1./16.
	res[JAIL] = n*1./16.
	return res

def chance(pos,n):
	res = [0]*40
	res[pos] = n*6./16.
	res[GO] = n*1./16.
	res[JAIL] = n*1./16.
	res[C1] = n*1./16.
	res[E3] = n*1./16.
	res[H2] = n*1./16.
	res[R1] = n*1./16.
	next_r = (((pos+5)/10)*10 + 5) % 40
	res[next_r] = n*2./16.
	if pos > U1 and pos < U2:
		next_u = U2
	else:
		next_u = U1
	res[next_u] = n*1./16.
	res[(pos-3) % 40] = n*1./16.
	return res

def adjust(vec):
	n = len(vec)
	res = [0.]*n
	temp = [0.]*n
	# first, roll the dice!
	for i in range(n):
		temp[(i+2) % 40] += vec[i]*1./16.
		temp[(i+3) % 40] += vec[i]*2./16.
		temp[(i+4) % 40] += vec[i]*3./16.
		temp[(i+5) % 40] += vec[i]*4./16.
		temp[(i+6) % 40] += vec[i]*3./16.
		temp[(i+7) % 40] += vec[i]*2./16.
		temp[(i+8) % 40] += vec[i]*1./16.

	# then, move people around
	for i in range(n):
		if i == G2J:
			res[JAIL] += temp[i]
			res[i] = 0
		elif i == CC1 or i == CC2 or i == CC3:
			res = [x + y for x, y in zip(cc(i, temp[i]), res)]
		elif i == CH1 or i == CH2 or i == CH3:
			res = [x + y for x, y in zip(chance(i, temp[i]), res)]
		else:
			res[i] += temp[i]

	return res

def main():
	spaces = 40
	curvector = [0]*spaces
	curvector[GO] = 100
	nextvector = adjust(curvector)
	while map(lambda x: round(x, 2), nextvector) != map(lambda x: round(x, 2), curvector):
		curvector = nextvector
		nextvector = adjust(curvector)

	nextvector = map(lambda x: round(x, 2), nextvector)
	topthree = heapq.nlargest(3, nextvector)
	topthree_idx = []
	for i in range(3):
		topthree_idx.append(nextvector.index(topthree[i]))
	print topthree_idx

main()