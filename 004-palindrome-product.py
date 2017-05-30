def palindrome(num):
  str_num = str(num)
  stack = []
  center_flag = 0
  digits = len(str_num)
  for i in range(digits):
    if i < digits/2:
      stack.append(str_num[i])
    elif 2*i + 1 == digits and digits % 2 == 1:
      continue
    elif str_num[i] != stack[-1]:
      return 0
    elif str_num[i] == stack[-1]:
      del stack[-1]
  if not stack:
    return 1
  else:
    return 0

def main():
  multipliers = range(1,1000)
  result = 1
  nums = [1,1]
  for i in multipliers:
    for j in multipliers:
      product = i*j
      if palindrome(product) and product > result:
        result = product
        nums = [i,j]

  print "result = "+str(result)
  print "numbers = "+str(nums)

main()