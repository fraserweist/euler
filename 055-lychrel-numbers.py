def rev_and_add(n):
  n_rev = int(str(n)[::-1])
  return n+n_rev

def is_palindrome(n):
  sn = str(n)
  srev = sn[::-1]
  return sn == srev

def main():
  limit = 10000
  lychrels = []
  for i in range(1,limit):
    num = i
    lflag = 1
    for _ in range(50):
      num = rev_and_add(num)
      if is_palindrome(num):
        lflag = 0
        break
    if lflag:
      lychrels.append(i)

  print lychrels, len(lychrels)

main()