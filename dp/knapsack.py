n, c = map(int, input().split())
dp=[0]*(c+1)

for i in range(n):
    w, v = map(int, input().split())
    for j in range(w, c+1):
        dp[j]=max(dp[j-w]+v, dp[j])

print(dp[c])