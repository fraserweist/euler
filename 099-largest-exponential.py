from math import *

def main():
  lst = []
  with open("099-largest-exponential.txt","r") as f:
    text = f.read()
  pairs = text.splitlines()
  for pair in pairs:
    lst.append(pair.split(","))

  lst = list(map(lambda x: map(int, x), lst))
  vals = []
  for b, e in lst:
    vals.append(e*log(b))
  max_idx = vals.index(max(vals))
  print max_idx+1

main()