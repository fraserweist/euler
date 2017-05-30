def fracs_between(n1,d1,n2,d2,d):
  stack = [((n1,d1),(n2,d2))]
  count = 0
  while stack:
    (n1,d1),(n2,d2) = stack.pop()
    if d1+d2 <= d:
      count += 1
      stack.append(((n1,d1),(n1+n2,d1+d2)))
      stack.append(((n1+n2,d1+d2),(n2,d2)))
  return count

def main():
  print fracs_between(1,3,1,2,12000)

main()