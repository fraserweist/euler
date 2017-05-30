from math import *

def main():
  limit = 500
  triples = []
  for a in range(1,limit+1):
    for b in range(a,limit+1):
      c = sqrt(a**2 + b**2)
      if c % 1 == 0 and c < 1000:
        triples.append((a,b,int(c)))


  max_sols = 0
  max_p = 0
  for p in range(1001):
    sols = 0
    for a,b,c in triples:
      if a+b+c == p:
        sols += 1
    if sols > max_sols:
      max_sols = sols
      max_p = p

  print max_sols, max_p

main()