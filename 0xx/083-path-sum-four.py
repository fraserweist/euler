def h_matrix(matr):
	n = len(matr)
	h_matr = [[0]*n for _ in range(n)]
	minval = min(map(min, matr))
	for i in range(n):
		for j in range(n):
			h_matr[i][j] = ((n-(i+1))+(n-(j+1)))*minval
	return h_matr

def minpath(matr):
	n = len(matr)
	openlist = dict()
	closedlist = []

	g_matr = [[0]*n for _ in range(n)]
	g_matr[0][0] = matr[0][0]
	h_matr = h_matrix(matr)
	openlist[(0,0)] = h_matr[0][0]+g_matr[0][0]

	while (n-1,n-1) not in closedlist:
		curi, curj = min(openlist, key=openlist.get)
		openlist.pop((curi,curj))
		closedlist.append((curi,curj))

		for i in range(4):
			# up
			if i == 0:
				if curi == 0: continue
				adji, adjj = curi-1, curj
			# down
			elif i == 1:
				if curi == n-1: continue
				adji, adjj = curi+1, curj
			# left
			elif i == 2:
				if curj == 0: continue
				adji, adjj = curi, curj-1
			# right 
			elif i == 3:
				if curj == n-1: continue
				adji, adjj = curi, curj+1

			if (adji,adjj) in closedlist: continue

			g = g_matr[curi][curj]+matr[adji][adjj]
			f = g + h_matr[adji][adjj]

			if (adji,adjj) not in openlist:
				openlist[(adji,adjj)] = f
				g_matr[adji][adjj] = g
			else:
				if f < openlist[(adji,adjj)]:
					openlist[(adji,adjj)] = f
					g_matr[adji][adjj] = g
					
	return g_matr[n-1][n-1]

def main():
	matr = []
	with open('083-path-sum-four.txt','r') as file:
		for line in file:
			line = map(int, map(lambda x: x.strip(), line.split(",")))
			matr.append(line)
	print minpath(matr)

main()