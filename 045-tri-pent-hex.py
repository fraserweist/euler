from math import *

def is_tri(n):
  return (sqrt(8*n+1)-1)/2 % 1 == 0

def is_pent(n):
  return (sqrt(24*n+1)+1)/6 % 1 == 0

def is_hex(n):
  return (sqrt(8*n+1)+1)/4 % 1 == 0

def main():
  answer = 0
  i = 144
  while True:
    hex_num = i*(2*i-1)
    print hex_num
    if is_pent(hex_num):
      if is_tri(hex_num):
        answer = hex_num
        break
    i += 1

  print answer

main()