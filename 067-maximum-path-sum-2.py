def main():
  triangle = []
  with open("067-maximum-path-sum-2.txt","r") as f:
    for line in f:
      triangle.append(map(int,line.split()))

  max_sums = triangle[:]
  for i in range(1,len(triangle)):
    for j in range(i+1):
      if j == 0:
        max_sums[i][j] = max_sums[i-1][j] + triangle[i][j]
      elif j == i:
        max_sums[i][j] = max_sums[i-1][j-1] + triangle[i][j]
      else:
        max_sums[i][j] = max(max_sums[i-1][j], max_sums[i-1][j-1]) + triangle[i][j]

  print max(max_sums[len(max_sums)-1])

main()