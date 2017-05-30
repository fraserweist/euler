def is_pandigital(S):
  digits = set()
  for num in S:
    for c in str(num):
      digits.add(int(c))
  return 1 if digits == set(range(1,10)) else 0

def main():
  limit = 10000
  prods = set()
  for i in range(2,limit):
    i_dig = len(str(i))
    for j in range(2,limit):
      j_dig = len(str(j))
      if i_dig+j_dig < 4:
        break
      prod = i*j
      prod_dig = len(str(prod))
      if i_dig+j_dig+prod_dig > 9:
        break
      elif is_pandigital([i,j,prod]):
        prods.add(prod)

  result = 0
  for prod in prods:
    result += prod
  print result

main()