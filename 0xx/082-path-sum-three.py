def arr_fill(arr):
	n = len(arr)
	sol = [[0] * n for _ in range(n)]
	for i in range(n):
		sol[i][0] = arr[i][0]
	for i in range(n):
		for j in range(1,n):
			sol[i][j] = sol[i][j-1]+arr[i][j]


	for _ in range(n):	
		for i in range(1,n):
			for j in range(1,n):
				sol[i][j] = min(sol[i][j], sol[i-1][j]+arr[i][j])
		for i in range(n-1):
			for j in range(1,n):
				sol[i][j] = min(sol[i][j], sol[i+1][j]+arr[i][j])
		for i in range(n):
			for j in range(1,n):
				sol[i][j] = min(sol[i][j], sol[i][j-1]+arr[i][j])

	return sol


def main():
	test = [
		[131, 673, 234, 103, 18], 
		[201, 96, 342, 965, 150],
		[630, 803, 746, 422, 111],
		[537, 699, 497, 121, 956],
		[805, 732, 524, 37, 331]]
	
	arr = []
	with open("082-path-sum-three.txt") as f:
		for line in f:
			arr.append(map(int,line.split(",")))

	result = 1000000000
	ans = arr_fill(arr)
	for i in range(len(arr)):
		if ans[i][-1] < result:
			result = ans[i][-1]
	print result

main()