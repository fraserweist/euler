def main():
  nums = range(2,21)
  primes = [2,3,5,7,11,13,17,19]
  minimum = 1
  for i in primes:
    minimum *= i
  print minimum

  def correct(num):
    for i in nums:
      if num % i != 0:
        return 0
    return 1

  result = minimum

  while not correct(result):
    result += minimum

  print "result = "+str(result)

main()