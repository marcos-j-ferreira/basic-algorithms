class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def insertAtBegin(self, data):

        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node 

    def show(self):
        atual = self.head

        while atual:
            print(atual.data, end=" -> ")
            atual = atual.next
        print(None)

lista = LinkedList()

lista.insertAtBegin(10)
lista.insertAtBegin(20)
lista.insertAtBegin(30)

lista.show()
