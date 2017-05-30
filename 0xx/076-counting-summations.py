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

def main():
    sol = count(range(1,5),5)
    print sol

main()