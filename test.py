class Node:

    def __init__(self, data):
        self.data = data
        self.head = None

    

class LinkedList:

    def __init__(self):
        self.head = None

    
    def add(self, data):

        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node
    
    def show(self):
        new = self.head
        
        while new:
            print(new.data, end=" -> ")
            new = new.next
        print(None)
    
    def remove(self):

        if self.head is None:
            return
        
        self.head = self.head.next

lista = LinkedList()

lista.add(1)
lista.add(2)
lista.add(3)
lista.add(4)
lista.add(5)

lista.show()

lista.remove()
lista.remove()

lista.show()

print("TESTE")