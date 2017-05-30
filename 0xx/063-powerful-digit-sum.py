def main():
  nums = [2,3,4,5,6,7,8,9]
  e = 1
  sols = []
  while sum(nums):
    e += 1
    for num in nums:
      power = num**e
      length = len(str(power))
      if len(str(power)) == e:
        sols.append((power,num,e))
      elif len(str(power)) != e:
        nums[nums.index(num)] = 0
  print sols, len(sols)

main()