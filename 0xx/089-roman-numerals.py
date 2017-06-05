def value_string(s):
  srev = s[::-1]
  maxseen = 0
  total = 0
  for i in range(len(srev)):
    v = val(srev[i])
    if v >= maxseen:
      total += v
      if v > maxseen:
        maxseen = v
    else:
      total -= v
  return total

def val(c):
  if c == 'I':
    return 1
  elif c == 'V':
    return 5
  elif c == 'X':
    return 10
  elif c == 'L':
    return 50
  elif c == 'C':
    return 100
  elif c == 'D':
    return 500
  elif c == 'M':
    return 1000

def create_string(n):
  num = n
  res = ""
  if num >= 1000:
    for _ in range(num/1000):
      res += "M"
      num -= 1000
  if num >= 900:
    res += "CM"
    num -= 900
  if num >= 500:
    res += "D"
    num -= 500
  if num >= 400:
    res += "CD"
    num -= 400
  if num >= 100:
    for _ in range(num/100):
      res += "C"
      num -= 100
  if num >= 90:
    res += "XC"
    num -= 90
  if num >= 50:
    res += "L"
    num -= 50
  if num >= 40:
    res += "XL"
    num -= 40
  if num >= 10:
    for _ in range(num/10):
      res += "X"
      num -= 10
  if num >= 9:
    res += "IX"
    num -= 9
  if num >= 5:
    res += "V"
    num -= 5
  if num >= 4:
    res += "IV"
    num -= 4
  if num >= 1:
    for _ in range(num):
      res += "I"
      num -= 1
  return res

def main():
  numerals = []
  with open("089-roman-numerals.txt","r") as file:
    for line in file:
      num = line.strip('\n')
      numerals.append(num)

  res = 0
  for s in numerals:
    new = create_string(value_string(s))
    res += len(s) - len(new)
  print res

main()