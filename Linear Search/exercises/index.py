class linear_search:

    def __init__(self, arr, number):

        self.arr = arr
        self.number = number

    
    def busca_linear_invertida(arr, number):

        for i in range(len(arr) - 1, -1, -1):

            if arr[i] == number:
                return print(True)
        print(False)
    
    def contagem_ocorrencias (arr, number):

        c = 0

        for i in arr:

            if number == i:
                c = c + 1
            
        print(c)



arr = [1,2,3,4,3]

number = 3

linear_search.contagem_ocorrencias(arr,number)