from tqdm import tqdm

def sum_of_factors(n):
    limit = int(n**.5)
    factors = set([1])
    for i in range(2,limit+1):
        if n%i == 0:
            factors.add(i)
            factors.add(n/i)
    return sum(factors)

def main():
    limit = 1000000
    lst = [0]*(limit+1)
    limit_flag = False
    maximum = 0
    for i in tqdm(range(2,limit+1)):
        lst[i] = sum_of_factors(i)
    chain_lengths = [0]*(limit+1)
    tocheck = set(lst)
    tocheck.remove(0)
    tocheck.remove(1)
    for num in tocheck:
        seen = set([num])
        if num > limit: continue
        next = lst[num]
        ctr = 0
        while next != num:
            if next > limit:
                ctr = 0
                break
            if next in seen:
                ctr = 0
                seen = set([num])
                break
            if next == 0 or next == 1:
                ctr = 0
                break
            seen.add(next)
            ctr += 1
            next = lst[next]
        for el in seen:
            chain_lengths[el] = ctr
    idx = chain_lengths.index(max(chain_lengths))
    res = idx
    next = lst[idx]
    while next != idx:
        res = min(res, next)
        next = lst[next]
    print res

main()