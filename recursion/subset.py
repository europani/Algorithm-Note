arr = [1, 2, 3]
result = []

def dfs(idx, sub_list):
    result.append(sub_list)

    for i in range(idx, len(arr)):
        dfs(i+1, sub_list+[arr[i]])

dfs(0, [])
print(result)  
# [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]