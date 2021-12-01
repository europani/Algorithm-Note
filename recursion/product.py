r = int(input())        # 2
arr = [1, 2, 3]
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
        dfs(level+1, sub_list+[arr[i]])

dfs(0, [])
print(result)
# [[1, 1], [1, 2], [1, 3], [2, 1], [2, 2], [2, 3], [3, 1], [3, 2], [3, 3]]

