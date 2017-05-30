def main():
  fracs = []
  for numer in range(10,100):
    for denom in range(numer+1,100):
      fracs.append((list(str(numer)),list(str(denom))))

  eliminatable = [str(x) for x in range(1,10)]
  solutions = []
  for numer, denom in fracs:
    for elim in eliminatable:
      if elim not in numer or elim not in denom:
        continue
      else:
        new_numer = numer[:]
        del new_numer[numer.index(elim)]
        new_denom = denom[:]
        del new_denom[denom.index(elim)]
        if new_denom == ['0']:
          continue
        elif (float("".join(numer))/float("".join(denom)) ==
          float("".join(new_numer))/float("".join(new_denom))):
          solutions.append(("".join(numer), "".join(denom)))

  print solutions
  numer_prod = 1
  denom_prod = 1
  for numer, denom in solutions:
    numer_prod *= int(numer)
    denom_prod *= int(denom)

  print numer_prod, denom_prod

main()