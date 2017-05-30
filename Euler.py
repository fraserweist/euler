from math import *

def is_prime(n):
  if n is 1: return False
  if n is 2: return True
  if n % 2 == 0: return False
  for i in range(3,int(sqrt(n))+1,2):
    if n % i == 0:
      return False
  return True

def is_tri(n):
  return (sqrt(8*n+1)-1)/2 % 1 == 0

def is_pent(n):
  return (sqrt(24*n+1)+1)/6 % 1 == 0

def is_hex(n):
  return (sqrt(8*n+1)+1)/4 % 1 == 0

def is_hept(n):
  return (sqrt(40*n+9)+3)/2 % 1 == 0

def is_oct(n):
  return (sqrt(3*n+1)+1)/3 % 1 == 0