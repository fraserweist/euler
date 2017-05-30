def print_collatz(n):
  steps = 1
  print n
  while n != 1:
    if n % 2 == 0:
      n /= 2
    else:
      n = 3*n + 1
    steps += 1
    print n
  return steps

def main():
  size = 1000000
  results = [0] * size
  for i in range(1,size+1):
    steps = 1
    n = i
    while n != 1:
      if n <= size:
        if results[n-1] != 0:
          steps += (results[n-1]-1)
          break
      steps += 1
      if n % 2 == 0:
        n = n / 2
      else:
        n = 3*n + 1
    results[i-1] = steps

  max_len = max(results)
  num = results.index(max_len) + 1

  print max_len, num

main()