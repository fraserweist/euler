from tqdm import tqdm
from math import *

def pent(n):
    return n*(3*n-1)/2

def pent_lim(n):
    return int((sqrt(24*n+1)-1) / 6)

def main():
    limit = 100000
    p = [1, 1]
    answer = 0
    for i in range(2,limit+1):
        result = 0
        cur_limit = pent_lim(i)
        k = 1
        while True:
            sign = (-1)**(k-1)
            pos_pent = pent(k)
            neg_pent = pent(-k)
            if i-pos_pent < 0: break
            result += p[i-pos_pent]*sign
            if i-neg_pent < 0: break
            result += p[i-neg_pent]*sign
            k += 1
        if result % 1000000 == 0:
            answer = i
            break
        p.append(result)
    print answer

main()