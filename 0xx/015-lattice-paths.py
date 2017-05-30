def dp(m,n,array):
  for i in range(m):
    array[i][0] = 1
  for j in range(n):
    array[0][j] = 1

  for i in range(1,m):
    for j in range(1,n):
      array[i][j] = array[i-1][j] + array[i][j-1]

def main():
  n = 21
  array = [[0] * n for _ in range(n)]
  dp(n,n,array)
  print array[-1][-1]

main()