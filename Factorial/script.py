def factorial(number:int = 5) -> None:

    result:int = 1
    for i in range(number):
        result += i * result

    print(f"The factorial of {number} is {result}")

factorial(10)
