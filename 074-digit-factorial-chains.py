from math import *
from tqdm import tqdm

def main():
  result = 0
  limit = 1000000
  arr = [0] * limit
  for i in tqdm(range(1,limit)):
    cur = i
    count = 1
    seen = set()
    seen.add(cur)
    while count <= 60:
      next = 0
      for c in str(cur):
        next += factorial(int(c))
      if next in seen:
        break
      if next <= limit:
        if arr[next-1] != 0:
          count += arr[next-1]
          break
      seen.add(next)
      cur = next
      count += 1
    arr[i-1] = count
    if count == 60:
      result += 1
  print result

main()