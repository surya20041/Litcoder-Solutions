MOD = 1000000007
MAXN = 1000

T = [[0] * (MAXN + 1) for _ in range(MAXN + 1)]
B = [0] * (MAXN + 1)
G = [0] * (MAXN + 1)

def init():
    T[1][0] = 1
    for j in range(1, MAXN + 1):
        T[1][j] = T[1][j - 1]
        if j >= 2:
            T[1][j] = (T[1][j] + T[1][j - 2]) % MOD
        if j >= 3:
            T[1][j] = (T[1][j] + T[1][j - 3]) % MOD
        if j >= 4:
            T[1][j] = (T[1][j] + T[1][j - 4]) % MOD
    for i in range(2, MAXN + 1):
        for j in range(1, MAXN + 1):
            T[i][j] = (T[i - 1][j] * T[1][j]) % MOD

def do_something():
    init()
    n = int(input())
    m = int(input())
    B[1] = 0
    G[1] = 1
    for j in range(2, m + 1):
        B[j] = 0
        for k in range(1, j):
            B[j] = (B[j] + (T[n][j - k] * G[k]) % MOD) % MOD
        G[j] = (T[n][j] + MOD - B[j]) % MOD
    print(G[m])

if __name__ == "__main__":
    do_something()
