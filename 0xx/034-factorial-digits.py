from math import *

def main():
  solutions = []
  factorials = [factorial(n) for n in range(10)]
  print factorials
  for i in range(10,2540160):
    cur_sum = 0
    for c in str(i):
      cur_sum += factorials[int(c)]
    if cur_sum == i:
      solutions.append(i)

  print solutions
  result = 0
  for num in solutions:
    result += num

  print result

main()