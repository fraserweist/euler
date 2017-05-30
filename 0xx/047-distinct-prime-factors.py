def num_factors(n):
  i = 2
  factors = []
  while i * i <= n:
    if n % i:
      i += 1
    else:
      n //= i
      factors.append(i)
  if n > 1:
    factors.append(n)
  return len(set(factors))

def main():
  f = 4
  flag = 0
  start = 630
  num_fs = [num_factors(start-3), num_factors(start-2), num_factors(start-1)]
  for i in range(10000000):
    num_fs.append(num_factors(start+i))
    if num_fs[i] == f:
      if num_fs[i+1] == f:
        if num_fs[i+2] == f:
          if num_fs[i+3] == f:
            print i-f+1+start
            return

main()