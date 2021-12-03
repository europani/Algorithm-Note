def binary_search(array, target, start, end):
    if start > end:
        return None

    mid = (start + end) // 2
    if array[mid] == target:    # search 성공
        return mid
    elif array[mid] > target:   # 찾으려는 값이 작으면 왼쪽만 확인
        return binary_search(array, target, start, mid-1)
    else:                       # 찾으려는 값이 크면 오른쪽만 확인
        return binary_search(array, target, mid+1, end)

n = int(input())        # 원소 갯수
target = int(input())   # 찾으려는 값
array = list(map(int, input().split()))     # n개의 원소를 갖는 배열

result = binary_search(array, target, 0, n-1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result+1)
