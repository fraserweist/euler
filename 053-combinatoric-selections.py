from math import *

def choose(n, r):
  return factorial(n)/(factorial(r)*factorial(n-r))

def main():
  sols = []
  for n in range(1,101):
    for r in range(1,n+1):
      if choose(n,r) > 1000000:
        sols.append((n,r))
  print len(sols)

main()