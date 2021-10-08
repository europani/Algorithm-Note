array = [7, 5, 1, 3, 4, 9, 2, 8, 6, 0]

for i in range(len(array)-1):
    for j in range(len(array)-1-i):
        if array[j] > array[j+1]:
            array[j], array[j+1] = array[j+1], array[j]
    
print(array)