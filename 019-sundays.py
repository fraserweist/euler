def dayofweek(y,m,d):
  t = [0,3,2,5,0,3,5,1,4,6,2,4]
  y -= (m < 3)
  return (y + y/4 - y/100 + y/400 + t[m-1] + d) % 7

def main():
  sundays = 0
  thirty = [4, 6, 9, 11]
  thirtyone = [1, 3, 5, 7, 8, 10, 12]
  for year in range(1901,2001):
    for month in range(1, 13):
      if dayofweek(year,month,1) == 0:
        sundays += 1
  print sundays

main()