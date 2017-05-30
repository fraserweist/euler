from Euler import *

def is_perm(a,b):
  return sorted(str(a)) == sorted(str(b))

def longer(a,b):
  return len(str(a)) > len(str(b))

def main():
  sol = float('inf')
  pows = []
  limit = 10000
  for n in range(400,limit):
    n_cub = n**3
    for p1 in range(n+1,limit):
      p1_cub = p1**3
      if longer(p1_cub,n_cub):
        break
      elif is_perm(n_cub,p1_cub):
        for p2 in range(p1+1,limit):
          p2_cub = p2**3
          if longer(p2_cub,p1_cub):
            break
          elif is_perm(p1_cub,p2_cub):
            for p3 in range(p2+1,limit):
              p3_cub = p3**3
              if longer(p3_cub,p2_cub):
                break
              elif is_perm(p2_cub,p3_cub):
                for p4 in range(p3+1,limit):
                  p4_cub = p4**3
                  if longer(p4_cub,p3_cub):
                    break
                  elif is_perm(p3_cub,p4_cub):
                    if n < sol:
                      print n,p1,p2,p3,p4
                      print n_cub,p1_cub,p2_cub,p3_cub,p4_cub
                      return

main()