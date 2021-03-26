import sys
R = sys.stdin.readline
d = []
N = int(R())
for i in range(N):
    M = list(map(int, R().split()))
    d.append(M[0])
    if i == N-1:
        d.append(M[1]) 
dp = [[-1 for _ in range(N+1)] for _ in range(N+1)]
#min_Matrix_mult fuc.
def minM(i, j):
    if dp[i][j] != -1:
        return dp[i][j]
    elif i - j == 0:
        dp[i][j] = 0
    elif i - j == 1:
        dp[i][j] = d[i-1]*d[i]*d[i+1]
    else:
        tmp = []
        for k in range(i, j):
            tmp.append(minM(i, k) + minM(k+1, j) + d[i-1]*d[k]*d[j])
        dp[i][j] = min(tmp)
    return dp[i][j]

print(minM(1, N))




# 5 3 2 6 : input
# 5 2 6 : 30
# 5 6 : 30 + 60 = 90