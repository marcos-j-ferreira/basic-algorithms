arr = [1,2,3,4]

number = 5

def linear (arr, number):

    for x in arr:
        if number == x:
            return True
            
    return False


result = linear(arr, number)

print(f"\n{result}\n")