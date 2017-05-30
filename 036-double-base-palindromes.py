def is_palindrome(s):
  srev = s[::-1]
  return s == srev

def dec_to_bin(n):
  ans = ""
  while n > 0:
    ans += str(n % 2)
    n /= 2
  return ans

def main():
  double_palin = []
  for i in range(1000000):
    if is_palindrome(str(i)):
      if is_palindrome(dec_to_bin(i)):
        double_palin.append(i)

  print double_palin
  result = 0
  for num in double_palin:
    result += num

  print result

main()