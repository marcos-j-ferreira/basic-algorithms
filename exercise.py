class Sorter:
    def __init__(self, arr: list = None):
        
        if arr is None:
            arr = []
        self.arr = arr

    def sort_array(self) -> list:
        size: int = len(self.arr)

        for i in range(size):
            min_index: int = i 

            for j in range(i + 1, size):
                if self.arr[j] < self.arr[min_index]:
                    min_index = j

            self.arr[i], self.arr[min_index] = self.arr[min_index], self.arr[i]
        return self.arr

    def print_list(self) -> None:
      
        if not isinstance(self.arr, list):
            raise ValueError("Expected a list.")

        for i in self.arr:
            print(i, end=" ")
        print()

    def set_array(self, arr: list) -> None:

        self.arr = arr

    def get_array(self) -> list:
       
        return self.arr

def start() -> None:

    sorter = Sorter([0, 4, 5, 6, 1, 2, 3, 4])

    print("Original array: ", end="")
    sorter.print_list()

    sorter.sort_array()  

    print("Sorted array: ", end="")
    sorter.print_list()

if __name__ == "__main__":
    start()
