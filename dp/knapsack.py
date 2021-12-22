n, c = map(int, input().split())        # 4 11
dp=[0]*(c+1)

for i in range(n):
    w, v = map(int, input().split())    # 5 12 / 3 8 / 6 14 / 4 8
    for j in range(w, c+1):
        dp[j]=max(dp[j-w]+v, dp[j])

print(dp[c])        # 28