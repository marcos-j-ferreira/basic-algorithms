def insert(arr:list = [None], target:int = 10) -> None:

    if arr == None:
        arr = []
    
    arr.append(target)
    print(f"Array with add number: {arr}")
    arr.sort()
    print(f"Array sort: {arr}")


arr:list = [0,2,3,4]
target:int = 1

insert(arr, target)