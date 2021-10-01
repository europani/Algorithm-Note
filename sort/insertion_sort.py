array = [7, 5, 1, 3, 4, 9, 2, 8, 6, 0]

for i in range(1, len(array)):
    for j in range(i, 0, -1):
        if array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
        else:
            break
    
print(array)