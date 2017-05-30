def main():
  result = 0
  for char in str(2**1000):
    result += int(char)

  print result

main()