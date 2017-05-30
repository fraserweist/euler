def is_pandigital(s):
  digits = set()
  for c in s:
    digits.add(int(c))
  return digits == set(range(1,10))

def main():
  limit = 100000
  pans = []
  for i in range(1,limit):
    digits = len(str(i))
    num = str(i)
    counter = 2
    while digits < 9:
      cur = i*counter
      num += str(cur)
      digits += len(str(cur))
      counter += 1
    if is_pandigital(num) and len(num) == 9:
      pans.append(int(num))
  print max(pans)

main()