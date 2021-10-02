def sequential_search(n, target, array):
    for i in range(n):
        if array[i] == target:
            return i+1

input_data = input().split()
n = int(input_data[0])      # 원소 갯수
target = input_data[1]      # 찾으려는 값
array = input().split()     # n개의 원소를 갖는 배열

print(sequential_search(n, target, array))