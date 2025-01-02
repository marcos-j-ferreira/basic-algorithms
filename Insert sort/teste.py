

def sort (arr:list=None, target:int = 5) -> list:

    if arr is None:
        arr = []
    
    arr.append(0)

    print(f"Array with value None: {arr}")

    size:int = len(arr) - 2

    print(size)

    c = 0

    for i in arr:

        c += 1

        if i > target:

            while size:

                value = arr[c]
                arr[c] = target
                target = value
                
                c +=  1
    
                size = size - 1
    
    if arr[size + 1] == 0:
        arr[size + 1] = target
    
    print(f"Array with orde in insert: {arr}")


arr:list = [0,2,4,5]

target:int = 1

sort(arr, target)

#print(result)

