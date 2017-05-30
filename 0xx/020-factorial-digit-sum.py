import math

def main():
  num = math.factorial(100)
  result = 0
  for char in str(num):
    result += int(char)

  print result

main()