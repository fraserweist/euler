def gcd(a,b):
  if not b:
    return a
  else:
    return gcd(b, a % b)

def main():
  limit = 1000000
  numer = 0
  denom = 1
  next_numer, next_denom = 3, 8
  while next_denom <= limit:
    numer = next_numer
    denom = next_denom
    next_numer += 3
    next_denom += 7
    f = gcd(next_numer, next_denom)
    next_numer /= f
    next_denom /= f

  print str(numer)+" / "+str(denom)+" < 3 / 7"

main()