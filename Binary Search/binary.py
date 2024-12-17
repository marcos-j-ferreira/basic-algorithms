def busca(arr, target):

    index = 0

    end = len(arr) - 1

    while index <= end:

        middle  = (index + end) // 2

        if arr[middle] == target:
            return middle
        elif arr[middle] < target:
            index = middle + 1 
        else:
            end = middle - 1
        
    return -1

arr = [1,2,3,4,5]

target = 5

result = busca(arr, target)

if result == -1:
    print("Númeor não encontrado")
else:
    print(f"Número encontrado {result}")
