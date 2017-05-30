def count(S, n):
    num_coins = len(S)
    table = [[0 for x in range(num_coins)] for x in range(n+1)]

    for i in range(num_coins):
        table[0][i] = 1

    for i in range(1, n+1):
        for j in range(num_coins):
            x = table[i - S[j]][j] if i-S[j] >= 0 else 0
            y = table[i][j-1] if j >= 1 else 0
            table[i][j] = x + y

    return table[n][num_coins-1]

def primes(n):
  sieve = [True] * n
  for i in xrange(3,int(n**0.5)+1,2):
    if sieve[i]:
      sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
  return [2] + [i for i in xrange(3,n,2) if sieve[i]]

def main():
  limit = 100
  for i in range(2,100):
    c = count(primes(i), i)
    if c >= 5000:
      print i, c
      break

main()