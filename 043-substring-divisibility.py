import itertools

def check(s):
  primes = [2,3,5,7,11,13,17]
  for i in range(7):
    sub = int(s[i+1:i+4])
    if sub % primes[i] != 0:
      return 0
  return 1

def main():
  pans = list(itertools.permutations(range(10)))
  good_pans = []
  for i in range(len(pans)):
    (d1,d2,d3,d4,d5,d6,d7,d8,d9,d10) = pans[i]
    if d1 != '0':
      good_pans.append(str(d1)+str(d2)+str(d3)+str(d4)+str(d5)+
        str(d6)+str(d7)+str(d8)+str(d9)+str(d10))

  sols = []

  for num in good_pans:
    if check(num):
      sols.append(num)
  print sols
  result = 0
  for num in sols:
    result += int(num)
  print result

main()