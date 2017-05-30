def numers(n):
  result = [3,7]
  if n < 3:
    return result[:n]
  for i in range(n-2):
    result.append(result[i]+2*result[i+1])
  return result

def denoms(n):
  result = [2,5]
  if n < 3:
    return result[:n]
  for i in range(n-2):
    result.append(result[i]+2*result[i+1])
  return result

def more_digits(n,d):
  sn = str(n)
  sd = str(d)
  return len(sn) > len(sd)

def main():
  limit = 1000
  ns = numers(limit)
  ds = denoms(limit)
  result = 0
  for i in range(limit):
    if more_digits(ns[i],ds[i]):
      result += 1
  print result

main()