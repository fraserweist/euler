import sys



def main():
  limit = 8
  totients = range(2,limit+1)
  for i in range(2,limit+1):
    if i == totients[i-2]:
      m = 2
      while m*i < limit:
        totients[m*i-2] *= (1. - 1/i)
  print sum(totients)

main()