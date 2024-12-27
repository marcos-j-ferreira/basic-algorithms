class DynamicArray:

    def __init__(self, start_size:int = 5):
        self.array = [None] * start_size
        self.size = 0
        self.tamanho = start_size

    def append(self, value:int = 2):

        if self.size == self.tamanho:
            self.resize()
        
        self.array[self.size] = value
        self.size += 1

    
    def resize(self) -> None:

        new_capacity = self.tamanho * 2
        new_array = [None] * new_capacity 

        for i in range(self.size):
            new_array[i] = self.array[i]
        
        self.array = new_array
        self.tamanho = new_tamanho

        print(f"Redimensionado para capacidade: {self.tamanho}")
    
    def get_array(self):
        return self.array
    
    def get_size(self):
        return self.size
    
    def get_tamanho(self):
        return self.tamanho