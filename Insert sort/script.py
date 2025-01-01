def insert(arr:list = [None], target:int = 0) -> list:

    array = arr

    if arr is None:
        arr = []

    array.append(target)
    return array

def sort(arr:list = [None]) -> list:

    for i in range(len(arr)):
        index = i 

        for j in range(i + 1, len(arr)):

            if arr[j] < arr[index]:
                index = j

        arr[i], arr[index] = arr[index], arr[i]

    return arr


if __name__ == "__main__":

    arr:list =  [9,3,1,7,2,4,6,8,5]
    target:int = 10

    print(f"Array original: {arr}", end="\n")

    result = insert(arr, target)

    print(f"Array with insert: {result}", end="\n")

    new_result = sort(result)

    print(f"Array with sort: {new_result}", end="")