def main():
  fib = [1,2]
  i = 2
  result = 2
  while 1:
    new = fib[i-1] + fib[i-2]
    if new > 4000000:
      break
    fib.append(new)
    if fib[-1] % 2 == 0:
      result += fib[i]
    i += 1

  print "result = "+str(result)

main()