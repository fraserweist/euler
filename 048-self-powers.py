def main():
  result = 0
  for i in range(1,1001):
    result += i**i
  print list(str(result))[-10:]

main()