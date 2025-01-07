def fibonacci(number:int = 5) -> None:

    result:int = 0
    count:int = 1

    while number > 0:
        number -= 1
        count, result = count + result, count
    
    return result

#fibonacci(5)
for i in range(10):
    result:int = fibonacci(i)
    print(f"O fibonacci do número {i} é {result}")