r = int(input())        # 2
arr = [1, 2, 3]
visited = [0]*len(arr)
result=[]

def dfs(level, sub_list):
    # Exception
    if r == 0:
        return

    # Base Case
    if level == r:
        result.append(sub_list)
        return
    
    for i in range(len(arr)): 
        if not visited[i]:
            visited[i]=1
            dfs(level+1, sub_list+[arr[i]])
            visited[i]=0   

dfs(0, [])
print(result)
# [[1, 2], [1, 3], [2, 1], [2, 3], [3, 1], [3, 2]]

