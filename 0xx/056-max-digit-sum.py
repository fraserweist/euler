def digit_sum(n):
  result = 0
  for c in str(n):
    result += int(c)
  return result

def main():
  dig_sums = []
  for a in range(1,101):
    for b in range(1,101):
      dig_sums.append(digit_sum(a**b))
  print max(dig_sums)

main()