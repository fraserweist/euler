import math

def factor_sum(n):
  result = 1
  for i in range(2, int(math.sqrt(n)) + 1):
    if n % i == 0:
      q = n / i
      if q == i:
        result += q
      else:
        result += q + i
  return result

def main():
  limit = 30000
  factor_sums = [factor_sum(i) for i in range(1, limit + 1)]

  abundant_nums = []
  for i in range(1, limit + 1):
    if factor_sums[i-1] > i:
      abundant_nums.append(i)

  non_abundant_sums = range(1, limit + 1)

  for i in abundant_nums:
    for j in abundant_nums[abundant_nums.index(i):]:
      if i + j <= limit:
        non_abundant_sums[i + j - 1] = 0

  result = 0
  for num in non_abundant_sums:
    result += num

  print result

main()