n = int(input())
dp = [0]*(n+1)
dp[1]=1

def fibo(n):
    for i in range(2, n+1):
        dp[i]=dp[i-2]+dp[i-1]

    return dp[n]

print(fibo(n))