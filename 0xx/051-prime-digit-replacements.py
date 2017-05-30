from math import *
def is_prime(n):
  if n is 1: return False
  if n is 2: return True
  if n % 2 == 0: return False
  for i in range(3,int(sqrt(n))+1,2):
    if n % i == 0: return False
  return True

def five_digits():
  result = []
  result.append([1,0,0,0,1])
  result.append([0,1,0,0,1])
  result.append([0,0,1,0,1])
  result.append([0,0,0,1,1])
  return result

def six_digits():
  result = []
  result.append([1,1,0,0,0,1])
  result.append([1,0,1,0,0,1])
  result.append([1,0,0,1,0,1])
  result.append([1,0,0,0,1,1])
  result.append([0,1,1,0,0,1])
  result.append([0,1,0,1,0,1])
  result.append([0,1,0,0,1,1])
  result.append([0,0,1,1,0,1])
  result.append([0,0,1,0,1,1])
  result.append([0,0,0,1,1,1])
  return result

def fill_pattern(pattern, num):
  n = num
  p = pattern[:]
  for i in range(len(p))[::-1]:
    if p[i] == 1:
      p[i] = n % 10
      n /= 10
    else:
      p[i] = -1
  return p

def complete_number(filled_pattern, digit):
  fp = filled_pattern[:]
  for i in range(len(fp)):
    if fp[i] == -1: fp[i] = digit
  s = ""
  for c in fp:
    s += str(c)
  return int(s)

def fam_size(dig, p):
  fs = 1
  for i in range(dig+1,10):
    if is_prime(complete_number(p, i)):
      fs += 1
  return fs

def main():
  result = 0
  for i in range(11,1000,2):
    patterns = []
    if i < 100:
      patterns = five_digits()
    else:
      patterns = six_digits()
    for j in range(len(patterns)):
      for k in range(3):
        if patterns[j][0] == 0 and k == 0:
          continue
        p = fill_pattern(patterns[j], i)
        num = complete_number(p, k)
        if is_prime(num):
          if fam_size(k, p) == 8:
            result = num
            break

  print result

main()