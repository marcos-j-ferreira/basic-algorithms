class linear_search:

    def __init__(self, arr, number):

        self.arr = arr
        self.number = number

    
    def busca_linear_invertida(arr, number):

        for i in range(len(arr) - 1, -1, -1):

            if arr[i] == number:
                return print(True)
        print(False)



arr = [1,2,3,4]

number = 3

linear_search.busca_linear_invertida(arr,number)