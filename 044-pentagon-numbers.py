def pent_num(n):
  return n*(3*n-1)/2

def main():
  pents = [pent_num(i) for i in range(1,2500)]
  sols = []
  for j in range(len(pents)):
    for k in range(j,len(pents)):
      psum = pents[j]+pents[k]
      pdiff = pents[k]-pents[j]
      if psum in pents and pdiff in pents:
        sols.append(pdiff)

  print sols
  print min(sols)

main()