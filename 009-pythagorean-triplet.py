import math

def main():
  for a in range(1,1000):
    asq = a**2
    for b in range(a,1000):
      bsq = b**2
      for c in range(int(math.floor(math.sqrt(asq + bsq))),1000):
        csq = c**2
        if asq + bsq == csq:
          if a + b + c == 1000:
            print a*b*c

main()