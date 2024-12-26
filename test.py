arr = [3,2,5,4,1,0]

for i in range(len(arr) - 1):
    index = i
    for j in range(i + 1, len(arr)):
        if arr[j] < arr[index]:
            index = j
    arr[i], arr[index] = arr[index], arr[i]

print(arr)