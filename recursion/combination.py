r = int(input())        # 2
arr = [1, 2, 3]
result=[]

def dfs(idx, sub_list):
    # Exception
    if r == 0:
        return

    # Base Case
    if len(sub_list) == r:
        result.append(sub_list)
        return
    
    for i in range(idx, len(arr)): 
        dfs(i+1, sub_list+[arr[i]]) 

dfs(0,[])
print(result)
# [[1, 2], [1, 3], [2, 3]]

