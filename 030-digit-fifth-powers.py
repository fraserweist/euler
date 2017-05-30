def main():
  # first, let's find the upper limit:
  power = 5
  lim = 1
  digits = len(str(lim*(9**power)))
  while digits > lim:
    lim += 1
    digits = len(str(lim*(9**power)))
  print lim

  nums = []
  for i in range(10,10**(lim)):
    digit_sum = 0
    for c in str(i):
      digit_sum += int(c)**power
    if digit_sum == i:
      nums.append(i)

  print nums
  result = 0
  for num in nums:
    result += num

  print result

main()