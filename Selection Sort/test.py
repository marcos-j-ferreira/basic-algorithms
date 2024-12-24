def a (arr):

    size = len(arr) 

    for i in range(size):

        index = i

        for j in range(i + 1, size):

            if arr[j] < arr[index]:

                index = j

        arr[i], arr[index] = arr[index], arr[i]

def prin(arr):

    for i in arr:
        print(i, end=" ")
    print()


if __name__ == "__main__":
    arr = [1,3,4,6,8,7,4,2]

    print("Origin array: ", end="")
    prin(arr)

    a(arr)
    print("array with select: ", end="")
    prin(arr)