def square_digs(n):
  result = 0
  for c in str(n):
    result += int(c)**2
  return result

def main():
  limit = 10000000
  arr = [0]*limit
  for i in range(1,limit):
    cur = i
    while arr[i] != 1 and arr[i] != 89:
      if cur == 1 or cur == 89:
        arr[i] = cur
        break
      cur = square_digs(cur)
      if cur < limit:
        if arr[cur] == 1 or arr[cur] == 89:
          arr[i] = arr[cur]
          break

  count = 0
  for i in range(len(arr)):
    if arr[i] == 89:
      count += 1

  print count

main()