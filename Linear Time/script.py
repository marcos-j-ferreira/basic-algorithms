def time (x:int = 10) -> int:
    number:int  = 0  

    for i in range(x + 1):
        number = i + number
    return number

def print_(y:int = 0) -> None:
    result = time(y)

    print(f"A soma dos {y} primeiros números é: {result}", end=" ")

print_(10)