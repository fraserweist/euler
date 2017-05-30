def main():
  limit = 100
  s = ""
  for i in range(1,1000000):
    s += str(i)
  result = 1
  for i in range(7):
    result *= int(s[10**i-1])

  print result

main()