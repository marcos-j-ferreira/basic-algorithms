
def add(arr, target):

    for i in range(1,target + 1,1):
        arr.append(i)
    
def remove(arr, target):

    for i in range(target):
        arr.pop(0)

def print_array(arr):
    for i in arr:
        print(i, end=" ")
    print()


if __name__== "__main__":
    arr = []

    print("origi array: ", end="")
    print_array(arr)

    add(arr,100)

    print("array with add itens: ", end="")
    print_array(arr)

    remove(arr, 50)

    print("Array with delete: ", end="")
    print_array(arr)