import math

def divisors(n):
  divs = [1,n]
  for i in range(2,int(math.sqrt(n))+1):
    if n%i == 0:
      divs.extend([i,n/i])
  return list(set(divs))

def main():
  result = 0
  i = 2
  while 1:
    i += 1
    tri = i*(i+1)/2
    fact = divisors(tri)
    if len(fact) > 500:
      print tri, fact
      break

main()