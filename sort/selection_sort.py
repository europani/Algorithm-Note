array = [7, 5, 1, 3, 4, 9, 2, 8, 6, 0]

for i in range(len(array)):
    min_index = i
    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]
    
print(array)