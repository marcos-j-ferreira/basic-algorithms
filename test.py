class DynamicArray:

    def __init__(self, tamanho:int = 5):
        self.array = [None] * tamanho
        self.size = 0
        self.livre = tamanho
    
    def append(self, value:int = 1) -> None:

        if self.size == self.livre:
            self.more()
        
        self.array[self.size] = value
        self.size += 1
    
    def more(self) -> None:

        novo_tamanho = self.livre * 2
        nova_array = [None] * novo_tamanho

        for i in range(self.size):
            nova_array[i] = self.array[i]
        
        self.array = new_array
        self.livre = novo_tamanho
    
    def get_array(self):
        print(f"Array: {self.array}")
        return 
    
    def get_size(self):

        print(f"Ocupado: {self.size}")
        return 
    def get_tamanho(self):

        print(f"Tamanho: {self.livre}")

arr = DynamicArray()

arr.append(1)
arr.append(2)
arr.append(3)
arr.append(4)
arr.append(5)

arr.get_array()

arr.get_size()

arr.get_tamanho()
