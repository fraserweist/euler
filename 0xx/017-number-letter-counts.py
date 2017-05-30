def letters_in_num(n):
  ones = {1:3, 2:3, 3:5, 4:4, 5:4, 6:3, 7:5, 8:5, 9:4}
  teens = {10:3, 11:6, 12:6, 13:8, 14:8, 15:7, 16:7, 17:9, 18:8, 19:8}
  tens = {2:6, 3:6, 4:5, 5:5, 6:5, 7:7, 8:6, 9:6}
  if n < 10:
    return ones[n]
  elif n < 20:
    return teens[n]
  elif n < 100:
    if n % 10 != 0:
      return tens[n / 10] + ones[n % 10]
    else:
      return tens[n / 10]
  elif n < 1000:
    if n % 100 == 0:
      return ones[n/100] + 7
    elif n % 100 < 10:
      return ones[n/100] + 10 + ones[n % 100]
    elif n % 100 < 20:
      return ones[n/100] + 10 + teens[n % 100]
    elif n % 10 == 0:
      return ones[n/100] + 10 + tens[(n % 100) / 10]
    else:
      return ones[n/100] + 10 + tens[(n % 100) / 10] + ones[n % 10]
  elif n == 1000:
    return 11

def main():
  result = 0
  for i in range(1,1001):
    result += letters_in_num(i)

  print result

main()