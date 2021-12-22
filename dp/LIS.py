n = int(input())            # 8
nums = list(map(int, input().split()))      # 5 3 7 8 6 2 9 4
dp=[1]*n

for i in range(1, n):
    for j in range(i-1,-1,-1):
        if nums[i] > nums[j]:
            dp[i] = max(dp[j]+1, dp[i])
    
print(max(dp))      # 4

