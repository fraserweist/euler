def dig_sum(n):
  return sum(map(int,list(str(n))))

def main():
  limit = 100
  terms = [(2,1),(3,1)]
  mult = 2
  for i in range(limit-2):
    n1, d1 = terms[i]
    n2, d2 = terms[i+1]
    new_n = 0
    new_d = 0
    if i % 3 == 0:
      new_n = n1 + n2*mult
      new_d = d1 + d2*mult
      mult += 2
    else:
      new_n = n1 + n2
      new_d = d1 + d2
    terms.append((new_n, new_d))
  last_n, last_d = terms[-1]
  print dig_sum(last_n)

main()