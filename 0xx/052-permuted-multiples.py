def same_digits(n,m):
  ln = sorted(list(str(n)))
  lm = sorted(list(str(m)))
  return ln == lm

def main():
  limit = 1000000
  result = 0
  for i in range(1,limit):
    if len(str(6*i)) > len(str(i)):
      continue
    if same_digits(i, 2*i):
      if same_digits(i, 3*i):
        if same_digits(i, 4*i):
          if same_digits(i, 5*i):
            if same_digits(i, 6*i):
              result = i
              break
  for i in range(1,7):
    print i*result

main()