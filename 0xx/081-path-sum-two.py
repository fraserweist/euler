def path_sum_two(n,m,arr):
  sol = [[0]*m for _ in range(n)]
  sol[0][0] = arr[0][0]
  for i in range(n):
    sol[i][0] = sol[i-1][0]+arr[i][0]
  for i in range(m):
    sol[0][i] = sol[0][i-1]+arr[0][i]
  for i in range(1,n):
    for j in range(1,m):
      sol[i][j] = min(sol[i-1][j],sol[i][j-1])+arr[i][j]
  return sol[n-1][m-1]


def main():
  arr = []
  with open("081-path-sum-two.txt","r") as f:
    for line in f:
      arr.append(line.split(","))
  arr = map(lambda lst: map(int,lst), arr)
  print path_sum_two(len(arr),len(arr[0]),arr)

main()