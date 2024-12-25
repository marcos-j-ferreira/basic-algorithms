
def stack(arr, item):

    print(f" Array origin: {arr} ",  end="\n")

    arr.append(item)

    print(f" Array with append: {arr} ",  end="\n")

    arr.pop()

    print(f"Array with remove the end element? {arr}", end="\n")

arr = [1,2,3,4]

item = 5

stack(arr, item)

