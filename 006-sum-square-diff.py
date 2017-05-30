def main():
  n = 100
  sum_sqr = n*(n+1)*(2*n+1)/6
  sqr_sum = (n*(n+1)/2)**2

  diff = abs(sum_sqr - sqr_sum)
  print diff

main()