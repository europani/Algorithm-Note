array = [7, 5, 1, 3, 4, 9, 2, 8, 6, 0]

def quick_sort(array, start, end):
    if start >= end:    # 원소 1개일 경우
        return
    
    pivot = start
    left = start+1
    right = end

    while left <= right:
        # 피봇보다 큰 데이터 찾기
        while left <= end and array[left] <= array[pivot]:
            left+=1
        # 피봇보다 작은 데이터 찾기
        while right > start and array[right] >= array[pivot]:
            right-=1

        # 엇갈린 경우 피봇과 작은 데이터(right)를 교환
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        # 일반적인 경우 큰 데이터(left)와 작은 데이터(right)를 교환
        else: 
            array[right], array[left] = array[left], array[right]

    # 다음회전 정렬 시행
    quick_sort(array, start, right-1)   # 왼쪽부분
    quick_sort(array, right+1, end)     # 오른쪽부분

    
quick_sort(array, 0, len(array)-1)
print(array)