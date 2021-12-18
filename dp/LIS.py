n = int(input())
nums = list(map(int, input().split()))
dp=[0]*n
dp[0]=1

for i in range(1, n):
    max_value = 1
    for j in range(i-1,-1,-1):
        if nums[i] > nums[j]:
            max_value = max(dp[j]+1, max_value)
    dp[i]=max_value
    
print(max(dp))

