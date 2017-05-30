import math

def factor_sum(n):
  result = 1
  for i in range(2,int(math.sqrt(n))+1):
    if n % i == 0:
      if i != n/i:
        result += (i + n/i)
      else:
        result += i
  return result

def main():
  limit = 10000
  nums = range(1,limit)
  amicable = [0]*(limit-1)
  sums = [0]*(limit-1)

  for num in nums:
    sums[num-1] = factor_sum(num)]

  result = 0
  for num in nums:
    if sums[num-1] < limit:
      if sums[sums[num-1]-1] == num and sums[num-1] != num:
        result += num

  print result

main()